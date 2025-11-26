# WeatherPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**times** | [**List[Time]**](Time.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.weather_point import WeatherPoint

# TODO update the JSON string below
json = "{}"
# create an instance of WeatherPoint from a JSON string
weather_point_instance = WeatherPoint.from_json(json)
# print the JSON string representation of the object
print(WeatherPoint.to_json())

# convert the object into a dict
weather_point_dict = weather_point_instance.to_dict()
# create an instance of WeatherPoint from a dict
weather_point_from_dict = WeatherPoint.from_dict(weather_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


