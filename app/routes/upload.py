from fastapi import APIRouter,HTTPException, UploadFile
from app.utils.storage import saveFile, chunkDocument
from app.utils.embeddings import embeddingModel, index
import uuid

router = APIRouter()

@router.post("/")
async def uploadFile(fileUpload:UploadFile):
    try:
        savePath = saveFile(fileUpload)
        chunkDocs = chunkDocument(savePath)
        chunks = [chunkDoc.page_content for chunkDoc in chunkDocs]
        vectors = await embeddingModel.aembed_documents(chunks)

        toUpsert=[]
        
        for i,vector in enumerate(vectors):
            metadata ={
                "filename":fileUpload.filename,
                "chunkId":i,
                "text":chunkDocs[i].page_content
            }
            toUpsert.append({
                "id":f"{fileUpload.filename}_{i}_{uuid.uuid4()}",
                "values":vector,
                "metadata":metadata
            })

        index.upsert(vectors=toUpsert)
        
        return {
            "status": "success",
            "filename": fileUpload.filename,
            "chunks": len(vectors)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="file upload failed")