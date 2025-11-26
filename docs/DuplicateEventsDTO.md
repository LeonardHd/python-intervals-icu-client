# DuplicateEventsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_copies** | **int** |  | [optional] 
**weeks_between** | **int** |  | [optional] 
**event_ids** | **List[int]** |  | [optional] 

## Example

```python
from intervals_icu_client.models.duplicate_events_dto import DuplicateEventsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateEventsDTO from a JSON string
duplicate_events_dto_instance = DuplicateEventsDTO.from_json(json)
# print the JSON string representation of the object
print(DuplicateEventsDTO.to_json())

# convert the object into a dict
duplicate_events_dto_dict = duplicate_events_dto_instance.to_dict()
# create an instance of DuplicateEventsDTO from a dict
duplicate_events_dto_from_dict = DuplicateEventsDTO.from_dict(duplicate_events_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


