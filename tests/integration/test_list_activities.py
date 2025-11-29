from datetime import date

import pytest

from intervals_icu_client import ApiClient
from intervals_icu_client.api.activities_api import ActivitiesApi


@pytest.mark.integration
def test_list_activities_returns_activities_or_empty_list(
    api_client: ApiClient,
    athlete_id: str,
) -> None:
    """Arrange/Act/Assert: list all activities for today.

    This test requires a valid Intervals.icu API key in the environment.
    """
    # Arrange
    activities_api = ActivitiesApi(api_client)
    today = date.today().isoformat()

    # Act
    activities = activities_api.list_activities(
        id=athlete_id,
        oldest=today,
        newest=today,
        limit=10,
    )

    # Assert
    assert activities is not None
    assert isinstance(activities, list)
