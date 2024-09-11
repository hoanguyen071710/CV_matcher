from sqlalchemy.dialects.postgresql.base import PGInspector
from typing import Dict, List, Any
import sys
import hashlib
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from googleapiclient import discovery

from ..model.entities.ExtractConfig import ExtractConfig


class Utils:
    @staticmethod
    def check_if_table_exists(conn: any, table_name: str, schema: str) -> bool:
        engine = conn.getEngine()
        print("Checking if table {}.{} exists".format(schema, table_name))
        insp = PGInspector(bind=engine)
        return insp.has_table(
            table_name=table_name,
            schema=schema
        )
    
    @staticmethod
    def create_table(conn: any, table_name: str, model: any):
        engine = conn.getEngine()
        if not Utils.check_if_table_exists(conn, table_name):
            engine = conn.getEngine()
            model.__table__.create(engine)
            print("Table {} created".format(table_name))
            return False
        else:
            print("Table {} already exists".format(table_name))
            return True

    @staticmethod
    def get_credential(scopes: List[str], service_account_key_file: str) -> ServiceAccountCredentials:
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
    
    @staticmethod
    def get_service(api_name: str, api_version: str, scopes: List[str], service_account_key_file: str) -> Any:
        """Creates a service endpoint for the zero-touch enrollment API.
        Builds and returns an authorized API client service for v1 of the API. Use
        the service endpoint to call the API methods.
        Returns:
        A service Resource object with methods for interacting with the service.
        """
        http_auth = Utils.get_credential(scopes, service_account_key_file).authorize(httplib2.Http())
        return discovery.build(api_name, api_version, http=http_auth)

    @staticmethod
    def deserialize_model(model: object) -> Dict[str, Any]:
        return {k:v for k, v in model.__dict__.items() if k != '_sa_instance_state'}
    
    @staticmethod
    def hash_model_values(model: object) -> str:
        valListStr = [str(v).lower() for k, v in Utils.deserialize_model(model).items() if k != 'id']
        valStrEncoded = "_".join(valListStr).encode("utf-8")
        return hashlib.sha256(valStrEncoded).hexdigest()