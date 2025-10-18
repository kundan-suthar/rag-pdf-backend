from fastapi import APIRouter,HTTPException, UploadFile
from app.utils.storage import saveFile, chunkDocument

router = APIRouter()

@router.post("/")
async def uploadFile(fileUpload:UploadFile):
    try:
        savePath = saveFile(fileUpload)
        chunkDocs = chunkDocument(savePath)
        chunks = [chunkDoc.page_content for chunkDoc in chunkDocs]
        
        return chunks
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="file upload failed")