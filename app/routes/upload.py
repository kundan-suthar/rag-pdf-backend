from fastapi import APIRouter,HTTPException, UploadFile
from app.utils.storage import saveFile


router = APIRouter()

@router.post("/")
async def uploadFile(fileUpload:UploadFile):
    try:
        savePath = saveFile(fileUpload)
        return savePath
    except Exception as e:
        raise HTTPException(status_code=500, detail="file upload failed")