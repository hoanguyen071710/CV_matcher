import sys
from typing import List, Any
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from googleapiclient import discovery


class GoogleConnector:
    def __init__(self, service_account_key_file: str):
        # self.scopes = scopes
        self.service_account_key_file = service_account_key_file
    def get_credential(self, scopes: List[str], service_account_key_file: str) -> ServiceAccountCredentials:
        """Creates a Credential object with the correct OAuth2 authorization.
        Uses the service account key stored in SERVICE_ACCOUNT_KEY_FILE.
        Returns:
        Credentials, the user's credential.
    """
        credential = ServiceAccountCredentials.from_json_keyfile_name(
        service_account_key_file, scopes)
            
        if not credential or credential.invalid:
            print('Unable to authenticate using service account key.')
            sys.exit()
        return credential
    
    def get_service(self, api_name: str, api_version: str, scopes: List[str]) -> Any:
        """Creates a service endpoint for the zero-touch enrollment API.
        Builds and returns an authorized API client service for v1 of the API. Use
        the service endpoint to call the API methods.
        Returns:
        A service Resource object with methods for interacting with the service.
        """
        http_auth = self.get_credential(scopes, self.service_account_key_file).authorize(httplib2.Http())
        return discovery.build(api_name, api_version, http=http_auth)