from unittest.mock import patch, MagicMock

from CV_matcher.connector.GoogleDriveConnector import GoogleDriveConnector


mock_path = "test.txt"

@patch("CV_matcher.connector.GoogleDriveConnector.GoogleConnector.get_service")
# @patch("CV_matcher.connector.GoogleDriveConnector.service_account_key_file")
def test_get_service(mock_get_service):

    connector = GoogleDriveConnector(mock_path)

    service = connector.get_service()

    mock_get_service.assert_called_with("drive", "v3", ["https://www.googleapis.com/auth/drive"])
