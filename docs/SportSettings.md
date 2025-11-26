# SportSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**athlete_id** | **str** |  | [optional] 
**types** | **List[str]** |  | [optional] 
**warmup_time** | **int** |  | [optional] 
**cooldown_time** | **int** |  | [optional] 
**ftp** | **int** |  | [optional] 
**indoor_ftp** | **int** |  | [optional] 
**w_prime** | **int** |  | [optional] 
**p_max** | **int** |  | [optional] 
**power_zones** | **List[int]** |  | [optional] 
**sweet_spot_min** | **int** |  | [optional] 
**sweet_spot_max** | **int** |  | [optional] 
**power_spike_threshold** | **int** |  | [optional] 
**power_zone_names** | **List[str]** |  | [optional] 
**ftp_est_min_secs** | **int** |  | [optional] 
**use_laps_for_power_intervals** | **bool** |  | [optional] 
**keep_all_laps_for_power_intervals** | **bool** |  | [optional] 
**after_kj0** | **int** |  | [optional] 
**after_kj1** | **int** |  | [optional] 
**power_field** | **str** |  | [optional] 
**lthr** | **int** |  | [optional] 
**max_hr** | **int** |  | [optional] 
**hr_zones** | **List[int]** |  | [optional] 
**hr_zone_names** | **List[str]** |  | [optional] 
**hr_load_type** | **str** |  | [optional] 
**hrrc_min_percent** | **float** |  | [optional] 
**threshold_pace** | **float** |  | [optional] 
**pace_units** | **str** |  | [optional] 
**pace_zones** | **List[float]** |  | [optional] 
**pace_zone_names** | **List[str]** |  | [optional] 
**pace_load_type** | **str** |  | [optional] 
**gap_model** | **str** |  | [optional] 
**elevation_correction** | **str** |  | [optional] 
**use_gap_zone_times** | **bool** |  | [optional] 
**best_effort_distances** | **List[float]** |  | [optional] 
**pace_curve_start** | **float** |  | [optional] 
**load_order** | **str** |  | [optional] 
**tiz_order** | **str** |  | [optional] 
**workout_order** | **str** |  | [optional] 
**interval_display** | **str** |  | [optional] 
**default_gear_id** | **str** |  | [optional] 
**default_indoor_gear_id** | **str** |  | [optional] 
**extract_workouts** | **bool** |  | [optional] 
**show_pauses** | **int** |  | [optional] 
**ignore_velocity** | **bool** |  | [optional] 
**default_workout_time** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**mmp_model** | [**PowerModel**](PowerModel.md) |  | [optional] 
**display** | [**Display**](Display.md) |  | [optional] 
**activity_field_ids** | **List[int]** |  | [optional] 
**activity_charts** | [**ActivityCharts**](ActivityCharts.md) |  | [optional] 
**custom_field_ids** | **List[int]** |  | [optional] 
**custom_field_values** | **Dict[str, object]** |  | [optional] 
**custom_zones_ids** | **List[int]** |  | [optional] 
**other** | **bool** |  | [optional] 
**ise_ftp_supported** | **bool** |  | [optional] 
**use_distance_for_intervals** | **bool** |  | [optional] 

## Example

```python
from intervals_icu_client.models.sport_settings import SportSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SportSettings from a JSON string
sport_settings_instance = SportSettings.from_json(json)
# print the JSON string representation of the object
print(SportSettings.to_json())

# convert the object into a dict
sport_settings_dict = sport_settings_instance.to_dict()
# create an instance of SportSettings from a dict
sport_settings_from_dict = SportSettings.from_dict(sport_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


