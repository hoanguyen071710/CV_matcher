from typing import List
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String, Boolean, Integer, ARRAY
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .Base import Base

class ExtractConfig(Base):
    __tablename__ = "ExtractConfig"

    id: Mapped[int] = mapped_column(primary_key=True)
    site_name: Mapped[str] = mapped_column(String(255))
    search_term: Mapped[str] = mapped_column(String(255))
    location: Mapped[str] = mapped_column(String(255))
    distance: Mapped[str] = mapped_column(String(255))
    is_remote: Mapped[bool] = mapped_column(Boolean)
    job_type: Mapped[str] = mapped_column(String(255))
    easy_apply: Mapped[bool] = mapped_column(Boolean)
    results_wanted: Mapped[str] = mapped_column(Integer)
    country_indeed: Mapped[str] = mapped_column(String(255))
    hyperlinks: Mapped[bool] = mapped_column(Boolean)
    proxies: Mapped[str] = mapped_column(String(255))
    description_format: Mapped[str] = mapped_column(String(255))
    linkedin_fetch_description: Mapped[bool] = mapped_column(Boolean)
    linkedin_company_ids: Mapped[list] = mapped_column(ARRAY(String))
    offset: Mapped[int] = mapped_column(Integer)
    hours_old: Mapped[int] = mapped_column(Integer)
    enforce_annual_hire: Mapped[bool] = mapped_column(Boolean)
    verbose: Mapped[int] = mapped_column(Integer)
    kwargs: Mapped[dict] = mapped_column(JSONB)



# class Config(BaseModel):
#     site_name: Optional[Union[str, List[str]]] = None
#     search_term: Optional[str] = None
#     location: Optional[str] = None
#     distance: Optional[int] = 50
#     is_remote: bool = False
#     job_type: Optional[str] = None
#     easy_apply: Optional[bool] = None
#     results_wanted: int = 15
#     country_indeed: str = "vietnam"
#     hyperlinks: bool = False
#     proxies: Optional[Union[List[str], str]] = None
#     description_format: str = "markdown"
#     linkedin_fetch_description: Optional[bool] = False
#     linkedin_company_ids: Optional[List[int]] = None
#     offset: Optional[int] = 0
#     hours_old: Optional[int] = None
#     enforce_annual_salary: bool = False
#     verbose: int = 2
#     kwargs: Optional[dict[str, Any]] = None