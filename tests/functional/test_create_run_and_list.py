from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Dict, Any

import pytest

from intervals_icu_client import ApiClient
from intervals_icu_client.api.events_api import EventsApi
from intervals_icu_client.models.event_ex import EventEx


@pytest.mark.integration
@pytest.mark.functional
def test_create_and_delete_running_workout_event(
    api_client: ApiClient,
    athlete_id: str,
) -> None:
    """Arrange/Act/Assert: create, verify, and delete a running workout event.

    Workflow:
    - Create a WORKOUT event for the given athlete.
    - Verify it can be listed by date.
    - Delete the event and confirm it no longer appears.
    """
    events_api = EventsApi(api_client)

    # Arrange
    # Use a near-future *local* time and format without timezone suffix
    start_dt = datetime.now() + timedelta(hours=1)
    start_iso = start_dt.replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%S")

    payload: Dict[str, Any] = {
        "name": "Test Running Workout",
        "category": "WORKOUT",
        "start_date_local": start_iso,
        "type": "Run",
        "description": "A test running workout created by IntervalsClient.",
        "athlete_id": athlete_id,
        "workout_doc": {},
    }

    event_ex = EventEx(**payload)

    # Act 1: create event
    created = events_api.create_event(
        id=athlete_id,
        upsert_on_uid=True,
        event_ex=event_ex,
    )

    # Assert basic properties of created event
    assert created is not None
    assert created.name == payload["name"]
    assert created.category == payload["category"]

    # Act 2: list events around the start date to find the created one
    date_only = start_iso.split("T", 1)[0]
    listed = events_api.list_events(
        id=athlete_id,
        oldest=date_only,
        newest=date_only,
        limit=50,
        format="json",
    )

    # Assert: created event is present in list
    assert isinstance(listed, list)
    matching = [e for e in listed if getattr(e, "id", None) == created.id]
    assert matching, "Created workout event should appear in list_events results"

    # Act 3: delete the event
    events_api.delete_event(id=athlete_id, event_id=created.id)

    # Assert: event no longer appears in list
    listed_after_delete = events_api.list_events(
        id=athlete_id,
        oldest=date_only,
        newest=date_only,
        limit=50,
        format="json",
    )
    assert isinstance(listed_after_delete, list)
    matching_after_delete = [e for e in listed_after_delete if getattr(e, "id", None) == created.id]
    assert not matching_after_delete, "Workout event should be gone after delete_event call"
