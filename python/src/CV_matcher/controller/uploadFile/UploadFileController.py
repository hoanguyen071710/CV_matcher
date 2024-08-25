import os
from fastapi import APIRouter, UploadFile

from ..constants import API
from ...service.uploadFile.UploadFileHandler import UploadFileHandler

# Anchor current path
currPath = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(currPath, '../../../resources/uploads')

router = APIRouter(prefix=API)

@router.post("/upload")
def uploadFile(uploadFile: UploadFile):
    uploadFileHandler = UploadFileHandler(uploadFile)
    uploadFileHandler.saveFile(os.path.join(UPLOAD_FOLDER, uploadFile.filename))

    return {"filename": uploadFile.filename}