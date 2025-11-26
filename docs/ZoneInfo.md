# ZoneInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**start** | **float** |  | [optional] 
**end** | **float** |  | [optional] 
**start_value** | **float** |  | [optional] 
**end_value** | **float** |  | [optional] 
**secs** | **int** |  | [optional] 

## Example

```python
from intervals_icu_client.models.zone_info import ZoneInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneInfo from a JSON string
zone_info_instance = ZoneInfo.from_json(json)
# print the JSON string representation of the object
print(ZoneInfo.to_json())

# convert the object into a dict
zone_info_dict = zone_info_instance.to_dict()
# create an instance of ZoneInfo from a dict
zone_info_from_dict = ZoneInfo.from_dict(zone_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


