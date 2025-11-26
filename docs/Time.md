# Time


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_secs** | **int** |  | [optional] 
**end_secs** | **int** |  | [optional] 
**index** | **int** |  | [optional] 
**temp** | **float** |  | [optional] 
**feels_like** | **float** |  | [optional] 
**humidity** | **int** |  | [optional] 
**wind_speed** | **float** |  | [optional] 
**wind_deg** | **int** |  | [optional] 
**wind_gust** | **float** |  | [optional] 
**rain** | **float** |  | [optional] 
**showers** | **float** |  | [optional] 
**snow** | **float** |  | [optional] 
**clouds** | **int** |  | [optional] 
**pressure** | **float** |  | [optional] 
**weather_code** | **int** |  | [optional] 

## Example

```python
from intervals_icu_client.models.time import Time

# TODO update the JSON string below
json = "{}"
# create an instance of Time from a JSON string
time_instance = Time.from_json(json)
# print the JSON string representation of the object
print(Time.to_json())

# convert the object into a dict
time_dict = time_instance.to_dict()
# create an instance of Time from a dict
time_from_dict = Time.from_dict(time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


