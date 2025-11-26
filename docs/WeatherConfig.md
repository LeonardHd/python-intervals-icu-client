# WeatherConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forecasts** | [**List[Forecast]**](Forecast.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.weather_config import WeatherConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WeatherConfig from a JSON string
weather_config_instance = WeatherConfig.from_json(json)
# print the JSON string representation of the object
print(WeatherConfig.to_json())

# convert the object into a dict
weather_config_dict = weather_config_instance.to_dict()
# create an instance of WeatherConfig from a dict
weather_config_from_dict = WeatherConfig.from_dict(weather_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


