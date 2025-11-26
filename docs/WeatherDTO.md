# WeatherDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forecasts** | [**List[Forecast]**](Forecast.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.weather_dto import WeatherDTO

# TODO update the JSON string below
json = "{}"
# create an instance of WeatherDTO from a JSON string
weather_dto_instance = WeatherDTO.from_json(json)
# print the JSON string representation of the object
print(WeatherDTO.to_json())

# convert the object into a dict
weather_dto_dict = weather_dto_instance.to_dict()
# create an instance of WeatherDTO from a dict
weather_dto_from_dict = WeatherDTO.from_dict(weather_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


