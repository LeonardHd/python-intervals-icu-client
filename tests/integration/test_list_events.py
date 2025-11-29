import os
from datetime import date

import pytest

from intervals_icu_client import ApiClient, Configuration
from intervals_icu_client.api.events_api import EventsApi


@pytest.mark.integration
def test_list_events_returns_events_or_empty_list(
    api_client: ApiClient,
    athlete_id: str,
) -> None:
    """Arrange/Act/Assert: list all events for today.

    This test requires a valid Intervals.icu API key in the environment.
    """
    # Arrange
    events_api = EventsApi(api_client)
    # the specific date includes a variety of event types for most athletes
    event_date = date(2025, 11, 29).isoformat()

    # Act
    events = events_api.list_events(
        id=athlete_id,
        oldest=event_date,
        newest=event_date,
        limit=10,
        format="json",
    )

    # Assert
    assert events is not None
    assert isinstance(events, list)
    expected_id = 81864387
    expected_name = "Easy Run"
    expected_start_date_local = "2025-11-29T00:00:00"

    matching = [e for e in events if getattr(e, "id", None) == expected_id]
    assert matching, "Expected workout event with id 81864387 not found in list_events results"

    event = matching[0]
    assert event.name == expected_name
    assert event.start_date_local == expected_start_date_local
    assert event.category == "WORKOUT"
    assert event.type == "Run"

    # Assert workout steps structure
    workout_doc = event.workout_doc
    assert workout_doc is not None, "Expected workout_doc on workout event"

    steps = workout_doc.steps
    assert steps is not None and isinstance(steps, list) and steps, "Expected non-empty workout steps list"

    # Check first step has expected basic structure
    first_step = steps[0]
    assert first_step['distance'] == 10000
    assert first_step['duration'] == 3100
    assert 'pace' in first_step
    assert first_step['pace']['units'] == 'secs'
    assert first_step['pace']['value'] == 310
    

