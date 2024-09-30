from unittest.mock import patch, MagicMock
import pytest

from CV_matcher.connector.GoogleDriveConnector import GoogleDriveConnector


mock_path = "test.txt"

@patch("CV_matcher.connector.GoogleDriveConnector.GoogleConnector.get_service")
# @patch("CV_matcher.connector.GoogleDriveConnector.service_account_key_file")
def test_get_service(mock_get_service):

    connector = GoogleDriveConnector(mock_path)

    service = connector.get_service()

    mock_get_service.assert_called_with("drive", "v3", ["https://www.googleapis.com/auth/drive"])


@patch("CV_matcher.connector.GoogleDriveConnector.GoogleConnector.get_service")
def test_list_files_or_folders_by_name(mock_get_service):
    mock_service = MagicMock()

    mock_service.files.return_value.list.return_value.execute.return_value = {"files": [{"name": "test.txt"}]}

    mock_get_service.return_value = mock_service

    connector = GoogleDriveConnector(mock_path)

    assert connector.list_files_or_folders_by_name("test.txt", "file") == [{"name": "test.txt"}]


@patch.object(GoogleDriveConnector, "list_files_or_folders_by_name")
@patch("CV_matcher.connector.GoogleDriveConnector.GoogleConnector.get_service")
@pytest.mark.parametrize(
    "mock_return_value, expected_result",
    [
        ([{"name": "test.txt"}], {"name": "test.txt"}),  # Resource exists
        ([], None)  # Resource does not exist
    ]
)
def test_check_resource_exists(mock_get_service, mock_list_files_or_folders_by_name, mock_return_value, expected_result):
    mock_service = MagicMock()
    mock_get_service.return_value = mock_service
    mock_list_files_or_folders_by_name.return_value = mock_return_value
    connector = GoogleDriveConnector(mock_path)
    assert connector.check_resource_exists("test.txt", "file") == expected_result
