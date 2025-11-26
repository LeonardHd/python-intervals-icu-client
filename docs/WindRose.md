# WindRose


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_speed** | **List[float]** |  | [optional] 
**count** | **List[int]** |  | [optional] 

## Example

```python
from intervals_icu_client.models.wind_rose import WindRose

# TODO update the JSON string below
json = "{}"
# create an instance of WindRose from a JSON string
wind_rose_instance = WindRose.from_json(json)
# print the JSON string representation of the object
print(WindRose.to_json())

# convert the object into a dict
wind_rose_dict = wind_rose_instance.to_dict()
# create an instance of WindRose from a dict
wind_rose_from_dict = WindRose.from_dict(wind_rose_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


