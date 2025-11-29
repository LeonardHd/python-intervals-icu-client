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
    # Contains three activities (swim, bike, run) on 2023-08-19
    race_day = date(2023, 8, 19).isoformat()

    # Act
    activities = activities_api.list_activities(
        id=athlete_id,
        oldest=race_day,
        newest=race_day,
        limit=10,
    )

    # Assert
    assert activities is not None
    assert isinstance(activities, list)

    # Expect three activities on race_day: swim, bike, run
    assert len(activities) == 3

    swim, bike, run = sorted(activities, key=lambda a: a.start_date_local)

    # Run assertions
    assert run.id.startswith("i") and run.id[1:].isdigit()
    assert run.start_date_local == "2023-08-19T11:12:20"
    assert run.type == "Run"
    assert run.icu_ignore_time is False
    assert run.icu_ignore_power is False
    assert run.icu_training_load == 139
    assert run.icu_recording_time == 6945
    assert run.elapsed_time == 6947
    assert run.name == "Run"
    assert run.start_date == "2023-08-19T09:12:20Z"
    assert run.distance == 21449.219
    assert run.icu_distance == 21449.219
    assert run.moving_time == 6923
    assert run.total_elevation_gain == 207.0
    assert run.total_elevation_loss == 207.0
    assert run.commute is False
    assert run.race is False
    assert run.max_speed == 4.794175
    assert run.average_speed == 3.0662918
    assert run.has_heartrate is True
    assert run.max_heartrate == 167
    assert run.average_heartrate == 159
    assert run.average_cadence == 88.27917
    assert run.average_temp == 33.057224
    assert run.min_temp == 31
    assert run.max_temp == 36
    assert run.gap == 3.1495068
    assert run.gap_model == "STRAVA_RUN"
    assert run.use_elevation_correction is True
    assert run.device_name == "StravaGPX"
    assert run.external_id == "Run.gpx"
    assert run.file_sport_index == 0
    assert run.file_type == "gpx"
    assert run.icu_athlete_id.startswith("i") and run.icu_athlete_id[1:].isdigit()
    assert run.icu_hr_zones == [145, 153, 162, 171, 176, 181, 190]
    assert run.lthr == 172
    assert run.icu_weight == 70.0
    assert run.icu_sweet_spot_min == 0
    assert run.icu_sweet_spot_max == 0
    assert run.icu_warmup_time == 300
    assert run.icu_cooldown_time == 300
    assert run.skyline_chart_bytes == "CAcSAuUNGgFbIgEDKAI="
    assert run.stream_types == [
        "time",
        "cadence",
        "heartrate",
        "distance",
        "altitude",
        "latlng",
        "velocity_smooth",
        "temp",
        "fixed_altitude",
    ]
    assert run.has_weather is False
    assert run.has_segments is False
    assert run.icu_hr_zone_times == [55, 357, 6323, 183, 0, 0, 0]
    assert run.use_gap_zone_times is True
    assert run.tiz_order == "POWER_HR_PACE"
    assert run.polarization_index == 0.0
    assert run.icu_lap_count == 0
    assert run.icu_median_time_delta == 4
    assert run.source == "UPLOAD"
    assert run.average_altitude == 254.19943
    assert run.min_altitude == 250.0
    assert run.max_altitude == 263.0
    assert run.hr_load == 139
    assert run.hr_load_type == "HRSS"
    assert run.pace == 3.098255
    assert run.athlete_max_hr == 190
    assert run.group is not None
    assert run.icu_intensity == 84.883354
    assert run.average_stride == 1.0528831

    # Bike assertions
    assert bike.id.startswith("i") and bike.id[1:].isdigit()
    assert bike.start_date_local == "2023-08-19T08:07:55"
    assert bike.type == "Ride"
    assert bike.icu_ignore_time is False
    assert bike.icu_ignore_power is False
    assert bike.icu_training_load == 132
    assert bike.icu_ftp == 250
    assert bike.icu_recording_time == 10692
    assert bike.elapsed_time == 10694
    assert bike.name == "Bike Ride"
    assert bike.start_date == "2023-08-19T06:07:55Z"
    assert bike.distance == 87094.67
    assert bike.icu_distance == 87094.67
    assert bike.moving_time == 10692
    assert bike.total_elevation_gain == 1053.4004
    assert bike.total_elevation_loss == 1079.0004
    assert bike.commute is False
    assert bike.race is False
    assert bike.max_speed == 18.05982
    assert bike.average_speed == 8.623534
    assert bike.has_heartrate is True
    assert bike.max_heartrate == 164
    assert bike.average_heartrate == 137
    assert bike.average_cadence == 69.434044
    assert bike.average_temp == 26.660313
    assert bike.min_temp == 23
    assert bike.max_temp == 30
    assert bike.gap is None
    assert bike.gap_model == "NONE"
    assert bike.use_elevation_correction is False
    assert bike.device_name == "StravaGPX"
    assert bike.external_id == "Bike_Ride.gpx"
    assert bike.file_sport_index == 0
    assert bike.file_type == "gpx"
    assert bike.icu_athlete_id.startswith("i") and bike.icu_athlete_id[1:].isdigit()
    assert bike.icu_hr_zones == [138, 153, 160, 171, 176, 181, 190]
    assert bike.lthr == 172
    assert bike.icu_weight == 70.0
    assert bike.icu_power_zones == [55, 75, 90, 105, 120, 150, 999]
    assert bike.icu_sweet_spot_min == 84
    assert bike.icu_sweet_spot_max == 97
    assert bike.icu_warmup_time == 1200
    assert bike.icu_cooldown_time == 600
    assert bike.skyline_chart_bytes == "CAcSArciGgFPIgEBKAI="
    assert bike.stream_types == [
        "time",
        "cadence",
        "heartrate",
        "distance",
        "altitude",
        "latlng",
        "velocity_smooth",
        "temp",
    ]
    assert bike.has_weather is False
    assert bike.has_segments is False
    assert bike.icu_hr_zone_times == [4456, 5937, 270, 29, 0, 0, 0]
    assert bike.tiz_order == "POWER_HR_PACE"
    assert bike.polarization_index == 0.0
    assert bike.icu_lap_count == 0
    assert bike.icu_median_time_delta == 2
    assert bike.source == "UPLOAD"
    assert bike.average_altitude == 372.85672
    assert bike.min_altitude == 238.6
    assert bike.max_altitude == 534.6
    assert bike.hr_load == 132
    assert bike.hr_load_type == "HRSS"
    assert bike.pace == 8.14578
    assert bike.athlete_max_hr == 190
    assert bike.group is not None
    assert bike.icu_intensity == 66.666664
    assert bike.average_stride == 3.5195038

    # Swim assertions
    assert swim.id.startswith("i") and swim.id[1:].isdigit()
    assert swim.start_date_local == "2023-08-19T07:12:20"
    assert swim.type == "Swim"
    assert swim.icu_ignore_time is False
    assert swim.icu_ignore_power is False
    assert swim.icu_training_load == 40
    assert swim.icu_recording_time == 3050
    assert swim.elapsed_time == 3051
    assert swim.name == "Swim"
    assert swim.start_date == "2023-08-19T05:12:20Z"
    assert swim.distance == 2404.21
    assert swim.icu_distance == 2404.21
    assert swim.moving_time == 3050
    assert swim.total_elevation_gain == 0.0
    assert swim.total_elevation_loss == 0.0
    assert swim.commute is False
    assert swim.race is False
    assert swim.max_speed == 519.98553
    assert swim.average_speed == 0.787749
    assert swim.has_heartrate is True
    assert swim.max_heartrate == 156
    assert swim.average_heartrate == 141
    assert swim.average_cadence == 27.282652
    assert swim.average_temp == 26.102228
    assert swim.min_temp == 26
    assert swim.max_temp == 31
    assert swim.gap is None
    assert swim.gap_model == "NONE"
    assert swim.use_elevation_correction is False
    assert swim.device_name == "StravaGPX"
    assert swim.external_id == "Swim.gpx"
    assert swim.file_sport_index == 0
    assert swim.file_type == "gpx"
    assert swim.icu_athlete_id.startswith("i") and swim.icu_athlete_id[1:].isdigit()
    assert swim.threshold_pace == 0.8333333
    assert swim.icu_hr_zones == [145, 153, 162, 171, 176, 181, 190]
    assert swim.lthr == 172
    assert swim.icu_weight == 70.0
    assert swim.icu_sweet_spot_min == 0
    assert swim.icu_sweet_spot_max == 0
    assert swim.icu_warmup_time == 300
    assert swim.icu_cooldown_time == 300
    assert swim.skyline_chart_bytes == "CAcSAuwXGgFRIgEBKAI="
    assert swim.stream_types == [
        "time",
        "cadence",
        "heartrate",
        "distance",
        "altitude",
        "latlng",
        "velocity_smooth",
        "temp",
    ]
    assert swim.has_weather is False
    assert swim.has_segments is False
    assert swim.icu_hr_zone_times == [2032, 992, 28, 0, 0, 0, 0]
    assert swim.tiz_order == "POWER_HR_PACE"
    assert swim.polarization_index == 0.0
    assert swim.icu_lap_count == 0
    assert swim.icu_median_time_delta == 1
    assert swim.source == "UPLOAD"
    assert swim.average_altitude == 270.6
    assert swim.min_altitude == 270.6
    assert swim.max_altitude == 270.6
    assert swim.hr_load == 40
    assert swim.pace_load == 72
    assert swim.hr_load_type == "HRSS"
    assert swim.pace_load_type == "SWIM"
    assert swim.pace == 0.7882656
    assert swim.athlete_max_hr == 190
    assert swim.group is not None
    assert swim.icu_intensity == 68.7118
    assert swim.average_stride == 0.8667767
