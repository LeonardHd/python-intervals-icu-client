# ZoneSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**zones** | [**List[ZoneInfo]**](ZoneInfo.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.zone_set import ZoneSet

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneSet from a JSON string
zone_set_instance = ZoneSet.from_json(json)
# print the JSON string representation of the object
print(ZoneSet.to_json())

# convert the object into a dict
zone_set_dict = zone_set_instance.to_dict()
# create an instance of ZoneSet from a dict
zone_set_from_dict = ZoneSet.from_dict(zone_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


