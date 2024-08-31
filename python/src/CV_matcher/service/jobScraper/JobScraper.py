import logging
import pandas as pd
import polars as pl
from enum import Enum
from typing import List

from .jobspy import scrape_jobs
from ...connection.PostgresConnection import PostgresConnection
from ...model.entities.Job import Job
from ...model.dao.JobDAO import JobDAO
from ...model.dao.Utils import Utils


class JobScraperSite(Enum):
    LINKEDIN = "linkedin"
    INDEED = "indeed"
    ZIP_RECRUITER = "zip_recruiter"
    GLASSDOOR = "glassdoor"

class JobScraper:
    def __init__(self, config: dict) -> None:
        self.config = config
        

    def scrape(self) -> pd.DataFrame:
        pd_jobs = scrape_jobs(
            **self.config
        )
        print(pd_jobs.head(10))
        listOfModelJobs = self.convert_jobs_to_model(pd_jobs)
        self.write_jobs_to_db(listOfModelJobs)
    
    def scrape_bulk(self, configs: List[dict]) -> pd.DataFrame:
        for cfg in configs:
            self.scrape(cfg)

    def convert_jobs_to_model(self, jobs: pd.DataFrame) -> pd.DataFrame:
        listOfJobModels = [Job(**jobAttr) for jobAttr in jobs.to_dict(orient="records")]
        return listOfJobModels

    def write_jobs_to_db(self, jobs: List[Job]) -> None:
        conn = PostgresConnection("localhost", 54320, "postgres", "postgres", "postgres")
        if not Utils.check_if_table_exists(conn, Job.__table__.name):
            Utils.create_table(conn, Job.__table__.name, Job)

        jobDAO = JobDAO(conn)
        jobDAO.insert_all(jobs)
        