from fastapi import APIRouter,   HTTPException

router = APIRouter()

@router.post("/")
async def QueryRequest():
    try:
        return {"message":"Query Request Test"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Query Failed")