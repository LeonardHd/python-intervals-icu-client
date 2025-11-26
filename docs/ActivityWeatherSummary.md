# ActivityWeatherSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_index** | **int** |  | [optional] 
**end_index** | **int** |  | [optional] 
**start_secs** | **int** |  | [optional] 
**end_secs** | **int** |  | [optional] 
**moving_time** | **int** |  | [optional] 
**whole_activity** | **bool** |  | [optional] 
**wind_speed** | [**WindRose**](WindRose.md) |  | [optional] 
**wind_gust** | [**WindRose**](WindRose.md) |  | [optional] 
**apparent_wind_speed** | [**WindRose**](WindRose.md) |  | [optional] 
**apparent_wind_gust** | [**WindRose**](WindRose.md) |  | [optional] 
**average_temp** | **float** |  | [optional] 
**min_temp** | **int** |  | [optional] 
**max_temp** | **int** |  | [optional] 
**average_weather_temp** | **float** |  | [optional] 
**min_weather_temp** | **float** |  | [optional] 
**max_weather_temp** | **float** |  | [optional] 
**average_feels_like** | **float** |  | [optional] 
**min_feels_like** | **float** |  | [optional] 
**max_feels_like** | **float** |  | [optional] 
**average_wind_speed** | **float** |  | [optional] 
**min_wind_speed** | **float** |  | [optional] 
**max_wind_speed** | **float** |  | [optional] 
**average_wind_gust** | **float** |  | [optional] 
**min_wind_gust** | **float** |  | [optional] 
**max_wind_gust** | **float** |  | [optional] 
**prevailing_wind_deg** | **int** |  | [optional] 
**average_yaw** | **float** |  | [optional] 
**headwind_percent** | **float** |  | [optional] 
**tailwind_percent** | **float** |  | [optional] 
**max_rain** | **float** |  | [optional] 
**max_showers** | **float** |  | [optional] 
**max_snow** | **float** |  | [optional] 
**average_clouds** | **int** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from intervals_icu_client.models.activity_weather_summary import ActivityWeatherSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityWeatherSummary from a JSON string
activity_weather_summary_instance = ActivityWeatherSummary.from_json(json)
# print the JSON string representation of the object
print(ActivityWeatherSummary.to_json())

# convert the object into a dict
activity_weather_summary_dict = activity_weather_summary_instance.to_dict()
# create an instance of ActivityWeatherSummary from a dict
activity_weather_summary_from_dict = ActivityWeatherSummary.from_dict(activity_weather_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


