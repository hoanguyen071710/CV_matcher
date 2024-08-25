from typing import Any, Optional, Union, List
from pydantic import BaseModel


class Config(BaseModel):
    site_name: Optional[Union[str, List[str]]] = None
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

# class Config(BaseModel):
#     id: int
#     site: str
#     job_url: HttpUrl
#     job_url_direct: Optional[HttpUrl] = None
#     title: str
#     company: str
#     location: str
#     job_type: str
#     date_posted: date
#     salary_source: Optional[str] = None
#     interval: Optional[str] = None
#     min_amount: Optional[float] = None
#     max_amount: Optional[float] = None
#     currency: Optional[constr(max_length=3)] = None  # Assuming currency is a 3-letter code
#     is_remote: Optional[bool] = None
#     job_level: Optional[str] = None
#     job_function: Optional[str] = None
#     company_industry: Optional[str] = None
#     listing_type: Optional[str] = None
#     emails: Optional[str] = None  # Could be further validated for email format
#     description: Optional[str] = None
#     company_url: Optional[HttpUrl] = None
#     company_url_direct: Optional[HttpUrl] = None
#     company_addresses: Optional[str] = None
#     company_num_employees: Optional[int] = None
#     company_revenue: Optional[str] = None
#     company_description: Optional[str] = None
#     logo_photo_url: Optional[HttpUrl] = None
#     banner_photo_url: Optional[HttpUrl] = None
#     ceo_name: Optional[str] = None
#     ceo_photo_url: Optional[HttpUrl] = None
