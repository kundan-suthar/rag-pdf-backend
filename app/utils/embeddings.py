from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
import os
from pinecone import Pinecone

load_dotenv()

embeddingModel = OpenAIEmbeddings(model="text-embedding-3-small", api_key=os.environ["OPENAI_API_KEY"])

pc = Pinecone(api_key=os.environ["PINECONE_DEFAULT_APIKEY"])

INDEX_NAME = "rag-pdf"
index = pc.Index(INDEX_NAME)
