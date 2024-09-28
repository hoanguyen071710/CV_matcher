import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from CV_matcher.service.jobScraper.JobScraper import JobScraper
from CV_matcher.service.jobScraper.TimeBased import TimeBasedScrape
from CV_matcher.model.entities.Jobs import Jobs
from CV_matcher.model.entities.ExtractConfig import ExtractConfig
from CV_matcher.db.PostgresConnection import PostgresConnection

# Mock data for testing
mock_job_data = pd.DataFrame({
    "id": ["123", "456"],
    "title": ["Software Engineer", "Data Scientist"],
    "company": ["Company A", "Company B"],
    "location": ["New York", "San Francisco"],
    "site": ["linkedin", "indeed"]
})

mock_config = {
    "site": "linkedin",
    "search_term": "Software Engineer",
    "location": "New York"
}

mock_extract_config = {
    "site_name": "linkedin",
    "search_term": "Software Engineer",
    "location": "New York",
    "distance": 50,
    "is_remote": False
}

mock_extract_config_2 = {
    "site_name": "linkedin",
    "search_term": "Software Engineer",
    "location": "New York",
    "distance": 50,
    "is_remote": False
}

# Mock data for the test
mock_config_data = [
    (ExtractConfig(**mock_extract_config),),
    (ExtractConfig(**mock_extract_config_2),)
]


# Test case for the 'scrape' method
@patch("CV_matcher.service.jobScraper.JobScraper.scrape_jobs")
@patch.object(JobScraper, "generate_id_df")
@patch.object(JobScraper, "write_jobs_to_db")
def test_scrape(test_write_jobs_to_db, test_generate_id_df, test_scrape_jobs):
    # Arrange
    scraper = JobScraper(config=mock_config)

    # Act
    scraper.scrape()

    # Assert
    test_scrape_jobs.assert_called_once()
    test_generate_id_df.assert_called_once()
    test_write_jobs_to_db.assert_called_once()


# Test case for the 'generate_id_df' method
def test_generate_id_df():
    # Arrange
    scraper = JobScraper(config=mock_config)
    expected_result = mock_job_data.copy()
    expected_result["id"] = expected_result["id"].str.lower() + "_" + expected_result["site"].str.lower()

    # Act
    result = scraper.generate_id_df(mock_job_data)

    # Assert
    pd.testing.assert_frame_equal(result, expected_result)


# Test case for write jobs to db method
@patch("CV_matcher.service.jobScraper.JobScraper.PostgresConnection")
@patch("CV_matcher.service.jobScraper.JobScraper.JobsDAO")
@patch("CV_matcher.service.jobScraper.JobScraper.Utils")
def test_write_db(mock_Utils, mock_JobsDAO, mock_PostgresConnection):
    # Arrange
    scraper = JobScraper(config=mock_config)
    mock_jobs = [MagicMock(spec=Jobs), MagicMock(spec=Jobs)]

    mock_conn = mock_PostgresConnection.return_value
    mock_jobs_dao = mock_JobsDAO.return_value
    mock_Utils.check_if_table_exists.return_value = False

    scraper.write_jobs_to_db(mock_jobs)

    mock_PostgresConnection.assert_called_once_with("localhost", 54320, "postgres", "postgres", "postgres")
    mock_Utils.check_if_table_exists.assert_called_once_with(mock_conn, Jobs.__table__.name, Jobs.__table_args__["schema"])
    mock_Utils.create_table.assert_called_once_with(mock_conn, Jobs.__table__.name, Jobs)
    mock_jobs_dao.insert.assert_called_once_with(mock_jobs)


# Test case for 'convert_jobs_to_model' method
def test_convert_jobs_to_model():
    # Arrange
    scraper = JobScraper(config=mock_config)
    mock_jobs = [MagicMock(spec=Jobs), MagicMock(spec=Jobs)]

    # Act
    result = scraper.convert_jobs_to_model(mock_job_data)

    # Assert
    assert isinstance(result, list)
    assert len(result) == 2

# Test for the 'get_config_from_db' method
@patch("CV_matcher.service.jobScraper.TimeBased.Utils.check_if_table_exists")
@patch("CV_matcher.service.jobScraper.TimeBased.PostgresConnection")
@patch("CV_matcher.service.jobScraper.TimeBased.ExtractConfigDAO")
def test_get_config_from_db(mock_config_dao, mock_postgres_connection, mock_check_if_table_exists):
    # Arrange
    time_scraper = TimeBasedScrape()
    
    # Mocking the return value of check_if_table_exists
    mock_check_if_table_exists.return_value = True
    
    # Mocking the DAO to return mock config data
    mock_config_dao_instance = mock_config_dao.return_value
    mock_config_dao_instance.get_all.return_value = mock_config_data

    # Act
    result = time_scraper.get_config_from_db()

    # Assert
    # One called when calling get_config_from_db() when instance is created
    # One called when calling get_config_from_db() when checking results above
    assert mock_postgres_connection.call_count == 2
    assert mock_check_if_table_exists.call_count == 2
    assert mock_config_dao_instance.get_all.call_count == 2
    assert result == mock_config_data


@patch("CV_matcher.service.jobScraper.TimeBased.JobScraper")
@patch.object(TimeBasedScrape, "get_config_from_db", return_value=mock_config_data)
@patch("CV_matcher.service.jobScraper.TimeBased.Utils")
def test_scrape(mock_deserialize_model, mock_config_dao, mock_job_scraper):
    # Arrange
    tc = TimeBasedScrape()

    # Mocking the return value of deserialize_model
    mock_deserialize_model.deserialize_model.side_effect = [mock_extract_config, mock_extract_config_2]

    # Act
    tc.scrape()

    # Assert
    mock_deserialize_model.deserialize_model.assert_any_call(mock_config_data[0][0])
    mock_deserialize_model.deserialize_model.assert_any_call(mock_config_data[1][0])
    mock_job_scraper.assert_called_with(mock_extract_config)
    mock_job_scraper.assert_called_with(mock_extract_config_2)
    mock_config_dao.assert_called_once()
