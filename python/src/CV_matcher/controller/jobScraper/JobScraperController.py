from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Optional, Union, List
import traceback

from ..constants import API
from ...service.jobScraper.JobScraper import JobScraper
from ...model.dao.ExtractConfigDAO import ExtractConfigDAO
from ...utils import Utils
from ...service.configService import ConfigService


router = APIRouter(prefix=API)


class Config(BaseModel):
    site_name: Optional[str] = None
    search_term: Optional[str] = None
    location: Optional[str] = None
    distance: Optional[int] = 50
    is_remote: bool = False
    job_type: Optional[str] = None
    easy_apply: Optional[bool] = None
    results_wanted: int = 15
    country_indeed: str = "vietnam"
    hyperlinks: bool = False
    proxies: Optional[Union[List[str], str]] = None
    description_format: str = "markdown"
    linkedin_fetch_description: Optional[bool] = False
    linkedin_company_ids: Optional[List[int]] = None
    offset: Optional[int] = 0
    hours_old: Optional[int] = None
    enforce_annual_salary: bool = False
    verbose: int = 2
    kwargs: Optional[dict[str, Any]] = None


@router.post("/job_scraper/scrape")
async def jobScraper(config: Config):
    try:
        scraper = JobScraper(config.model_dump())
        scraper.scrape()
        return {"status": "200"}
    except Exception as e:
        print(traceback.format_exc())
        return {"status": "500", "message": str(e)}

@router.post("/job_scraper/config/create")
async def createConfig(config: Config):
    try:
        configService = ConfigService(config.model_dump())
        configService.insert_config()
        return {"status": "200", "message": "Config created"}
    except Exception as e:
        print(traceback.format_exc())
        return {"status": "500", "message": str(e)}