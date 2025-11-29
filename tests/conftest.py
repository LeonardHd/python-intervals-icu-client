import os
from typing import Generator
from intervals_icu_client.configuration import Configuration
import pytest


from intervals_icu_client import ApiClient

@pytest.fixture
def athlete_id(
    load_dotenv: None,
) -> str:
    """Provides the ATHLETE_ID from the environment."""
    return os.environ["ATHLETE_ID"]

@pytest.fixture
def api_client(
    load_dotenv: None,
) -> Generator[ApiClient, None, None]:
    """Provides an ApiClient configured with the INTERVALS_ICU_API_KEY from the environment."""
    api_key = os.environ["INTERVALS_ICU_API_KEY"]
    configuration = Configuration(
          username="API_KEY",
          password=api_key,
    )

    with ApiClient(configuration) as api_client:
        yield api_client

@pytest.fixture()
def load_dotenv() -> None:
    """Automatically load environment variables from a .env file for all tests."""
    from dotenv import load_dotenv as dotenv_load

    dotenv_load()