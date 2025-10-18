from fastapi import UploadFile
from pathlib import Path


uploadDir = Path('documents')
def saveFile(fileUpload:UploadFile) -> Path:
    savePath = uploadDir / fileUpload.filename
    with open(savePath, "wb") as f:
        f.write(fileUpload.file.read())
    return savePath