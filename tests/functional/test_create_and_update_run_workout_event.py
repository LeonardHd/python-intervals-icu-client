from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any, Dict

import pytest

from intervals_icu_client import ApiClient
from intervals_icu_client.api.events_api import EventsApi
from intervals_icu_client.models.event_ex import EventEx


@pytest.mark.integration
@pytest.mark.functional
def test_create_and_update_running_workout_with_workout_steps(
    api_client: ApiClient,
    athlete_id: str,
) -> None:

    events_api = EventsApi(api_client)

    # Arrange
    start_dt = datetime.now() + timedelta(hours=1)
    start_iso = start_dt.replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%S")

    event_create_req = EventEx(
        category="WORKOUT",
        name="Test Running Workout (create/update)",
        start_date_local=start_iso,
        type="Run",
        description=(
            "\n"
            "- 2m 5:20 Pace\n"
            "\n"
            "Active 3x\n"
            "- active 2km 5:10-5:30 Pace\n"
            "- 2m 6:00 Pace intensity=recovery"
        ),
    )

    created = None
    try:
        # Act 1: create event
        created = events_api.create_event(
            id=athlete_id,
            upsert_on_uid=True,
            event_ex=event_create_req,
        )

        assert created.id is not None

        # Assert workout steps on created event
        assert created.workout_doc is not None
        assert created.workout_doc.steps is not None
        assert len(created.workout_doc.steps) == 2

        warmup_step = created.workout_doc.steps[0]
        assert warmup_step['duration'] == 120

        interval_block = created.workout_doc.steps[1]
        assert interval_block['reps'] == 3
        assert interval_block['steps'] is not None
        assert len(interval_block['steps']) == 2
        assert interval_block['steps'][0]['distance'] == 2000
        assert interval_block['steps'][1]['duration'] == 120
        assert interval_block['steps'][1]['intensity'] == "recovery"

        # Act 2: update event with an additional recovery step defined by description
        update_request = EventEx(
            category=created.category,
            name=created.name,
            start_date_local=created.start_date_local,
            type=created.type,
            description=(
                created.description
                + "\n"
                + "\n- 1m 6:30 Pace intensity=recovery"
            ),
        )

        updated = events_api.update_event(
            id=athlete_id,
            event_id=created.id,
            event_ex=update_request,
        )

        assert updated.id == created.id
        assert updated.workout_doc is not None
        assert updated.workout_doc.steps is not None
        # Now expect an extra recovery step at the end
        assert len(updated.workout_doc.steps) == 3
        extra_step = updated.workout_doc.steps[-1]
        assert extra_step['duration'] == 60
        assert extra_step['intensity'] == "recovery"
    finally:
        if created is not None and created.id is not None:
            events_api.delete_event(id=athlete_id, event_id=created.id)


