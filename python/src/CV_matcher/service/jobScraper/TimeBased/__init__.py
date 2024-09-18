from typing import List
import pandas as pd

from ....controller.jobScraper.JobScraperController import Config
from ..JobScraper import JobScraper
from ....db.PostgresConnection import PostgresConnection
# from ....model.dao.Utils import Utils
from ....model.dao.ExtractConfigDAO import ExtractConfigDAO
from ....model.entities.ExtractConfig import ExtractConfig
from ....utils import Utils


class TimeBasedScrape:
    def __init__(self) -> None:
        self.configs = self.get_config_from_db()
    
    def scrape(self) -> pd.DataFrame:
        for cfg in self.configs:
            des_cfg = Utils.deserialize_model(cfg[0])
            print("Scraping with config " + des_cfg)
            jobScraper = JobScraper(des_cfg)
            jobScraper.scrape()
    
    def get_config_from_db(self) -> Config:
        conn = PostgresConnection("localhost", 54320, "postgres", "postgres", "postgres")
        if Utils.check_if_table_exists(
            conn, 
            ExtractConfig.__tablename__,
            ExtractConfig.__table_args__["schema"]
        ) == False:
            raise Exception("Config table does not exist")

        configDAO = ExtractConfigDAO(conn)
        return configDAO.get_all()

    