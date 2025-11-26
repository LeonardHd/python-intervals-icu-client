# Interval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_index** | **int** |  | [optional] 
**distance** | **float** |  | [optional] 
**moving_time** | **int** |  | [optional] 
**elapsed_time** | **int** |  | [optional] 
**average_watts** | **int** |  | [optional] 
**average_watts_alt** | **int** |  | [optional] 
**average_watts_alt_acc** | **int** |  | [optional] 
**min_watts** | **int** |  | [optional] 
**max_watts** | **int** |  | [optional] 
**average_watts_kg** | **float** |  | [optional] 
**max_watts_kg** | **float** |  | [optional] 
**intensity** | **int** |  | [optional] 
**w5s_variability** | **float** |  | [optional] 
**weighted_average_watts** | **int** |  | [optional] 
**training_load** | **float** |  | [optional] 
**joules** | **int** |  | [optional] 
**joules_above_ftp** | **int** |  | [optional] 
**decoupling** | **float** |  | [optional] 
**avg_lr_balance** | **float** |  | [optional] 
**average_dfa_a1** | **float** |  | [optional] 
**average_epoc** | **float** |  | [optional] 
**wbal_start** | **int** |  | [optional] 
**wbal_end** | **int** |  | [optional] 
**average_respiration** | **float** |  | [optional] 
**average_tidal_volume** | **float** |  | [optional] 
**average_tidal_volume_min** | **float** |  | [optional] 
**zone** | **int** |  | [optional] 
**zone_min_watts** | **int** |  | [optional] 
**zone_max_watts** | **int** |  | [optional] 
**average_speed** | **float** |  | [optional] 
**min_speed** | **float** |  | [optional] 
**max_speed** | **float** |  | [optional] 
**gap** | **float** |  | [optional] 
**average_heartrate** | **int** |  | [optional] 
**min_heartrate** | **int** |  | [optional] 
**max_heartrate** | **int** |  | [optional] 
**average_cadence** | **float** |  | [optional] 
**min_cadence** | **int** |  | [optional] 
**max_cadence** | **int** |  | [optional] 
**average_torque** | **float** |  | [optional] 
**min_torque** | **float** |  | [optional] 
**max_torque** | **float** |  | [optional] 
**total_elevation_gain** | **float** |  | [optional] 
**min_altitude** | **float** |  | [optional] 
**max_altitude** | **float** |  | [optional] 
**average_gradient** | **float** |  | [optional] 
**average_smo2** | **float** |  | [optional] 
**average_thb** | **float** |  | [optional] 
**average_smo2_2** | **float** |  | [optional] 
**average_thb_2** | **float** |  | [optional] 
**average_temp** | **float** |  | [optional] 
**average_weather_temp** | **float** |  | [optional] 
**average_feels_like** | **float** |  | [optional] 
**average_wind_speed** | **float** |  | [optional] 
**average_wind_gust** | **float** |  | [optional] 
**prevailing_wind_deg** | **int** |  | [optional] 
**average_yaw** | **float** |  | [optional] 
**headwind_percent** | **float** |  | [optional] 
**tailwind_percent** | **float** |  | [optional] 
**strain_score** | **float** |  | [optional] 
**ss_p_max** | **float** |  | [optional] 
**ss_w_prime** | **float** |  | [optional] 
**ss_cp** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**end_index** | **int** |  | [optional] 
**group_id** | **str** |  | [optional] 
**segment_effort_ids** | **List[int]** |  | [optional] 
**start_time** | **int** |  | [optional] 
**end_time** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**average_stride** | **float** |  | [optional] 

## Example

```python
from intervals_icu_client.models.interval import Interval

# TODO update the JSON string below
json = "{}"
# create an instance of Interval from a JSON string
interval_instance = Interval.from_json(json)
# print the JSON string representation of the object
print(Interval.to_json())

# convert the object into a dict
interval_dict = interval_instance.to_dict()
# create an instance of Interval from a dict
interval_from_dict = Interval.from_dict(interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


