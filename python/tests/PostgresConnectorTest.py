import pytest
from unittest.mock import patch
from sqlalchemy.engine import Engine
from CV_matcher.db.PostgresConnection import PostgresConnection


# Patch the create_engine method in the sqlalchemy module to prevent actual DB connection
# @patch("CV_matcher.db.PostgresConnection.create_engine")
@patch("sqlalchemy.engine.create_engine")
def test_postgres_connection(mock_create_engine):
    # Arrange
    host = "localhost"
    port = 5432
    user = "test_user"
    password = "test_password"
    database = "test_db"

    # Act
    conn = PostgresConnection(host, port, user, password, database)

    # Assert
    mock_create_engine.assert_called_once_with(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}", echo=True)
