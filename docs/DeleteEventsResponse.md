# DeleteEventsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events_deleted** | **int** |  | [optional] 

## Example

```python
from intervals_icu_client.models.delete_events_response import DeleteEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteEventsResponse from a JSON string
delete_events_response_instance = DeleteEventsResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteEventsResponse.to_json())

# convert the object into a dict
delete_events_response_dict = delete_events_response_instance.to_dict()
# create an instance of DeleteEventsResponse from a dict
delete_events_response_from_dict = DeleteEventsResponse.from_dict(delete_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


