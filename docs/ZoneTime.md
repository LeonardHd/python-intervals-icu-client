# ZoneTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**secs** | **int** |  | [optional] 

## Example

```python
from intervals_icu_client.models.zone_time import ZoneTime

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneTime from a JSON string
zone_time_instance = ZoneTime.from_json(json)
# print the JSON string representation of the object
print(ZoneTime.to_json())

# convert the object into a dict
zone_time_dict = zone_time_instance.to_dict()
# create an instance of ZoneTime from a dict
zone_time_from_dict = ZoneTime.from_dict(zone_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


