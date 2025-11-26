# ActivityWeather


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | [**List[WeatherPoint]**](WeatherPoint.md) |  | [optional] 
**closest_points** | [**List[Closest]**](Closest.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.activity_weather import ActivityWeather

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityWeather from a JSON string
activity_weather_instance = ActivityWeather.from_json(json)
# print the JSON string representation of the object
print(ActivityWeather.to_json())

# convert the object into a dict
activity_weather_dict = activity_weather_instance.to_dict()
# create an instance of ActivityWeather from a dict
activity_weather_from_dict = ActivityWeather.from_dict(activity_weather_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


