from fastapi import UploadFile
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

uploadDir = Path('documents')
def saveFile(fileUpload:UploadFile) -> Path:
    savePath = uploadDir / fileUpload.filename
    with open(savePath, "wb") as f:
        f.write(fileUpload.file.read())
    return savePath

def chunkDocument(filePath:Path):
    loader = PyPDFLoader(file_path=filePath)
    docs = loader.load()
    textSplitter = RecursiveCharacterTextSplitter( chunk_size=1000, chunk_overlap=200)
    chunks = textSplitter.split_documents(docs)
    return chunks
