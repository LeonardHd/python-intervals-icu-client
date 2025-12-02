from __future__ import annotations

from datetime import datetime, timedelta
from typing import Dict, Any

import pytest

from intervals_icu_client import ApiClient
from intervals_icu_client.api.activities_api import ActivitiesApi
from intervals_icu_client.models.activity import Activity


@pytest.mark.integration
@pytest.mark.functional
def test_create_and_update_manual_activity(
    api_client: ApiClient,
    athlete_id: str,
) -> None:
    """Arrange/Act/Assert: create a manual workout activity and then update it.

    Workflow:
    - Create a MANUAL run activity for the given athlete.
    - Verify basic properties on the created activity.
    - Update some editable fields (name, description, tags).
    - Fetch the activity again and verify the updates.

    This test requires a valid Intervals.icu API key and athlete id
    in the environment (see `tests/conftest.py`).
    """
    activities_api = ActivitiesApi(api_client)

    # Arrange
    # Use a near-future *local* time and format without timezone suffix
    start_dt = datetime.now() + timedelta(hours=1)
    start_iso = start_dt.replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%S")

    base_payload: Dict[str, Any] = {
        "start_date_local": start_iso,
        "type": "Run",
        "name": "Test Manual Run Activity",
        "description": "Created by python-intervals-icu-client functional test.",
        # minimal plausible values for a short manual run
        "elapsed_time": 600,
        "moving_time": 600,
        "distance": 2000,
        "source": "MANUAL",
    }

    activity = Activity(**base_payload)

    # Act 1: create, then ensure we always clean up the activity
    created = activities_api.create_manual_activity(
        id=athlete_id,
        activity=activity,
    )

    try:
        # Assert basic properties of created activity
        assert created is not None
        assert created.id is not None
        assert created.type == base_payload["type"]
        assert created.name == base_payload["name"]
        assert created.source == base_payload["source"]

        # Prepare an update: change name, description and add tags
        updated_name = created.name + " (updated)"
        updated_description = "Updated description from functional test."
        updated_tags = ["python-client", "functional-test"]

        update_payload = Activity(
            id=created.id,
            name=updated_name,
            description=updated_description,
            tags=updated_tags,
        )

        # Act 2: update the activity. We use the generic update_activity endpoint
        # which accepts a partial Activity object.
        updated = activities_api.update_activity(
            id=created.id,
            activity=update_payload,
        )

        # Assert: the returned activity reflects the updated fields
        assert updated.id == created.id
        assert updated.name == updated_name
        assert updated.description == updated_description
        # Tags may be returned as None or list; if present, should contain our tags
        if updated.tags is not None:
            for tag in updated_tags:
                assert tag in updated.tags

        # Act 3: fetch the activity again and verify persistence of updates
        fetched = activities_api.get_activity(
            id=updated.id,
        )

        assert isinstance(fetched.actual_instance, Activity)
        fetched_activity = fetched.actual_instance
        assert fetched_activity.id == created.id
        assert fetched_activity.name == updated_name
        assert fetched_activity.description == updated_description
        if fetched_activity.tags is not None:
            for tag in updated_tags:
                assert tag in fetched_activity.tags
    finally:
        # Act 4: delete the activity to keep the account clean
        if getattr(created, "id", None) is not None:
            activities_api.delete_activity(
                id=created.id,
            )
