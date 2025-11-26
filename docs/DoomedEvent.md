# DoomedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**external_id** | **str** |  | [optional] 

## Example

```python
from intervals_icu_client.models.doomed_event import DoomedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DoomedEvent from a JSON string
doomed_event_instance = DoomedEvent.from_json(json)
# print the JSON string representation of the object
print(DoomedEvent.to_json())

# convert the object into a dict
doomed_event_dict = doomed_event_instance.to_dict()
# create an instance of DoomedEvent from a dict
doomed_event_from_dict = DoomedEvent.from_dict(doomed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


