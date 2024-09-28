from typing import List, Any, Dict, Union
from enum import Enum

from .GoogleConnector import GoogleConnector


class ResourceEnumQuery(Enum):
    folder = "name = '{}' and mimeType = 'application/vnd.google-apps.folder'"
    file = "name = '{}' and mimeType = 'text/plain'"
    all_resource = "name = '{}'"

class GoogleDriveConnector(GoogleConnector):
    def __init__(self, service_account_key_file: str):
        super().__init__(service_account_key_file)
        self.scopes = ["https://www.googleapis.com/auth/drive"]
        self.api_name = "drive"
        self.api_version = "v3"
        self.service = self.get_service()
    
    def get_service(self) -> Any:
        return super().get_service(self.api_name, self.api_version, self.scopes)
    
    def list_files_or_folders_by_name(self, name: str, resource_type: str) -> List[Dict[str, Any]]:
        return self.service.files().list(
            q=ResourceEnumQuery[resource_type].value.format(name)
        ).execute()["files"]
    
    def check_resource_exists(self, name: str, resource_type: str):
        res_list = self.list_files_or_folders_by_name(name, resource_type)
        if len(res_list) == 0:
            return None
        return res_list[0]

    # def create_folder(self, folder_name: str):
    #     folder = self.check_folder_exists(folder_name)
    #     if folder is None:
    #         fileMetadata = {
    #             "name": folder_name,
    #             "mimeType": "application/vnd.google-apps.folder",
    #         }
    #         return self.service.files().create(body=fileMetadata, fields="*").execute()
    #     else:
    #         return folder
    
# # Sample create folder payload
# samepleCreateFolderPayloadResponse = {'kind': 'drive#file',
#  'id': '1_Nsx0qHuFRQ-d-YkG9oBtHzPMV2LdlEd',
#  'name': 'TestFolder2',
#  'mimeType': 'application/vnd.google-apps.folder',
#  'starred': False,
#  'trashed': False,
#  'explicitlyTrashed': False,
#  'parents': ['0AJFhs_2s2z7fUk9PVA'],
#  'spaces': ['drive'],
#  'version': '1',
#  'webViewLink': 'https://drive.google.com/drive/folders/1_Nsx0qHuFRQ-d-YkG9oBtHzPMV2LdlEd',
#  'iconLink': 'https://drive-thirdparty.googleusercontent.com/16/type/application/vnd.google-apps.folder+48',
#  'hasThumbnail': False,
#  'thumbnailVersion': '0',
#  'viewedByMe': False,
#  'createdTime': '2024-09-19T17:42:47.638Z',
#  'modifiedTime': '2024-09-19T17:42:47.638Z',
#  'modifiedByMeTime': '2024-09-19T17:42:47.638Z',
#  'modifiedByMe': True,
#  'owners': [{'kind': 'drive#user',
#    'displayName': 'cv-matcher@lunar-tine-389403.iam.gserviceaccount.com',
#    'photoLink': 'https://lh3.googleusercontent.com/a/ACg8ocIKpsC3LeVxlydy61W-c7NJvsrErlGoYJFyFmzgCSYv8xFOGnA=s64',
#    'me': True,
#    'permissionId': '14192239079814795331',
#    'emailAddress': 'cv-matcher@lunar-tine-389403.iam.gserviceaccount.com'}],
#  'lastModifyingUser': {'kind': 'drive#user',
#   'displayName': 'cv-matcher@lunar-tine-389403.iam.gserviceaccount.com',
#   'photoLink': 'https://lh3.googleusercontent.com/a/ACg8ocIKpsC3LeVxlydy61W-c7NJvsrErlGoYJFyFmzgCSYv8xFOGnA=s64',
#   'me': True,
#   'permissionId': '14192239079814795331',
#   'emailAddress': 'cv-matcher@lunar-tine-389403.iam.gserviceaccount.com'},
#  'shared': False,
#  'ownedByMe': True,
#  'capabilities': {'canAcceptOwnership': False,
#   'canAddChildren': True,
#   'canAddMyDriveParent': False,
#   'canChangeCopyRequiresWriterPermission': False,
#   'canChangeSecurityUpdateEnabled': False,
#   'canChangeViewersCanCopyContent': False,
#   'canComment': True,
#   'canCopy': False,
#   'canDelete': True,
#   'canDownload': True,
#   'canEdit': True,
#   'canListChildren': True,
#   'canModifyContent': True,
#   'canModifyContentRestriction': False,
#   'canModifyEditorContentRestriction': False,
#   'canModifyOwnerContentRestriction': False,
#   'canModifyLabels': False,
#   'canMoveChildrenWithinDrive': True,
#   'canMoveItemIntoTeamDrive': True,
#   'canMoveItemOutOfDrive': True,
#   'canMoveItemWithinDrive': True,
#   'canReadLabels': False,
#   'canReadRevisions': False,
#   'canRemoveChildren': True,
#   'canRemoveContentRestriction': False,
#   'canRemoveMyDriveParent': True,
#   'canRename': True,
#   'canShare': True,
#   'canTrash': True,
#   'canUntrash': True},
#  'viewersCanCopyContent': True,
#  'copyRequiresWriterPermission': False,
#  'writersCanShare': True,
#  'permissions': [{'kind': 'drive#permission',
#    'id': '14192239079814795331',
#    'type': 'user',
#    'emailAddress': 'cv-matcher@lunar-tine-389403.iam.gserviceaccount.com',
#    'role': 'owner',
#    'displayName': 'cv-matcher@lunar-tine-389403.iam.gserviceaccount.com',
#    'photoLink': 'https://lh3.googleusercontent.com/a/ACg8ocIKpsC3LeVxlydy61W-c7NJvsrErlGoYJFyFmzgCSYv8xFOGnA=s64',
#    'deleted': False,
#    'pendingOwner': False}],
#  'permissionIds': ['14192239079814795331'],
#  'folderColorRgb': '#8f8f8f',
#  'quotaBytesUsed': '0',
#  'isAppAuthorized': True,
#  'linkShareMetadata': {'securityUpdateEligible': False,
#   'securityUpdateEnabled': True}}