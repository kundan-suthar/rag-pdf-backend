from fastapi import APIRouter,   HTTPException

router = APIRouter()

@router.post("/")
async def uploadFile():
    try:
        return {"message":"routes test success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="file upload failed")