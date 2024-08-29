from fastapi import APIRouter
from pydantic import BaseModel
import traceback

from ..constants import API
from ...service.jobScraper.JobScraper import JobScraper
from ...service.jobScraper.JobConfig.Config import Config


router = APIRouter(prefix=API)


@router.post("/job_scraper")
async def jobScraper(config: Config):
    try:
        scraper = JobScraper(config.model_dump())
        scraper.scrape()
        return {"status": "200"}
    except Exception as e:
        print(traceback.format_exc())
        return {"status": "500", "message": str(e)}


def convert_config_to_dict(config: Config) -> dict:
    return config.model_dump()