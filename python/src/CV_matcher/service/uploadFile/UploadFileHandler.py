from fastapi import UploadFile


class UploadFileHandler:
    def __init__(self, uploadFile: UploadFile):
        self._uploadFile = uploadFile

    def saveFile(self, filePath):
        with open(filePath, "wb") as f:
            f.write(self._uploadFile.file.read())
            f.close()
    
    def setFile(self, uploadFile: UploadFile):
        self._uploadFile = uploadFile
    
    def getFile(self):
        return self._uploadFile
    
    def getFileName(self):
        return self._uploadFile.filename

    
