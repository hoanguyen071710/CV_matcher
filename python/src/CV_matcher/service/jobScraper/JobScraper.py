import os
import pandas as pd
import polars as pl
from enum import Enum
from typing import List
from datetime import datetime

from .jobspy import scrape_jobs
from ...db.PostgresConnection import PostgresConnection
from ...model.entities.Jobs import Jobs
from ...model.dao.JobsDAO import JobsDAO
from ...utils import Utils


class JobScraperSite(Enum):
    LINKEDIN = "linkedin"
    INDEED = "indeed"
    ZIP_RECRUITER = "zip_recruiter"
    GLASSDOOR = "glassdoor"

class JobScraper:
    def __init__(self, config: dict) -> None:
        self.config = config
        

    def scrape(self) -> None:
        pd_jobs = scrape_jobs(
            **self.config
        )
        pd_jobs = self.generate_id_df(pd_jobs)
        listOfModelJobs = self.convert_jobs_to_model(pd_jobs)
        # self.write_jobs_to_local(pd_jobs, self.config["search_term"], None)
        self.write_jobs_to_db(listOfModelJobs)
        return listOfModelJobs
    
    def scrape_bulk(self, configs: List[dict]) -> pd.DataFrame:
        for cfg in configs:
            self.scrape(cfg)

    def convert_jobs_to_model(self, jobs: pd.DataFrame) -> pd.DataFrame:
        listOfJobModels = [Jobs(**jobAttr) for jobAttr in jobs.to_dict(orient="records")]
        return listOfJobModels

    def write_jobs_to_db(self, jobs: List[Jobs]) -> None:
        conn = PostgresConnection("localhost", 54320, "postgres", "postgres", "postgres")
        if not Utils.check_if_table_exists(conn, Jobs.__table__.name, Jobs.__table_args__["schema"]):
            Utils.create_table(conn, Jobs.__table__.name, Jobs)

        jobDAO = JobsDAO(conn)
        jobDAO.insert(jobs)
    
    def write_jobs_to_local(self, jobs: pd.DataFrame, search_term: str, backup_path: str) -> None:
        if backup_path is None or backup_path == "":
            backup_path = "../../../resources/backupJobScraped"
        currPath = os.path.dirname(os.path.abspath(__file__))
        timeNow = datetime.now().strftime("%Y%m%d-%H%M%S")
        fileName = f"jobs-{timeNow}-{search_term}.csv"
        jobs.to_csv(
            os.path.join(currPath, backup_path, fileName),
        )

    def generate_id_df(self, jobs: pd.DataFrame) -> pd.DataFrame:
        jobs["id"] = jobs["id"].str.lower() + "_" + jobs["site"].str.lower()
        return jobs


    # def write_jobs_to_google_drive(self, jobs: pd.DataFrame, search_term: str, backup_path: str) -> None:
    #     service = Utils.get_service('drive', 'v3', SCOPES, SERVICE_ACCOUNT_KEY_FILE)