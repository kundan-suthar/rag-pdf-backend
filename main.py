from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from config import origins



load_dotenv()

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          
    allow_credentials=True,          
    allow_methods=["*"],           
    allow_headers=["*"],           
)

@app.get("/")
def get_root():
    return {"message":"API is active"}