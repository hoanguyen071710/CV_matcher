from typing import List

from .GoogleConnector import GoogleConnector


class GoogleDriveConnector(GoogleConnector):
    def __init__(self, service_account_key_file: str):
        super().__init__(service_account_key_file)
        self.scopes = ["https://www.googleapis.com/auth/drive"]
        self.api_name = "drive"
        self.api_version = "v3"
    
    def get_service(self):
        return super().get_service(self.api_name, self.api_version, self.scopes)
