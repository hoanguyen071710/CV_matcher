from fastapi import FastAPI

from .uploadFile import UploadFileController
from .jobScraper import JobScraperController


app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(UploadFileController.router)
app.include_router(JobScraperController.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)