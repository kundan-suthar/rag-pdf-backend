
from dotenv import load_dotenv
import os

load_dotenv()

prod_frontendURL = os.environ["FRONTEND_URL"]

origins = [
    "http://localhost:3000",
    prod_frontendURL   
]