from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.config import origins
from pinecone import Pinecone
import os
from pathlib import Path


from app.routes.upload import router as uploadRouter
from app.routes.query import router as queryRouter

load_dotenv()

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          
    allow_credentials=True,          
    allow_methods=["*"],           
    allow_headers=["*"],           
)

pc = Pinecone(api_key=os.environ["PINECONE_DEFAULT_APIKEY"])

INDEX_NAME="rag-pdf"
DIMENSION=1536

if INDEX_NAME not in [i["name"] for i in pc.list_indexes()]:
    pc.create_index(
        name=INDEX_NAME,
        dimension=DIMENSION,
        metric="cosine",
        spec={"serverless": {"cloud": "aws", "region": "us-east-1"}}
    )

index = pc.Index(INDEX_NAME)

documentDirectory = Path("documents")
documentDirectory.mkdir(exist_ok=True)

app.include_router(uploadRouter, prefix='/upload')
app.include_router(queryRouter, prefix='/ask')