# SharedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**external_id** | **str** |  | [optional] 
**athlete_id** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**types** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**start_date_local** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 
**chat_id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**closing_date_local** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**lat** | **float** |  | [optional] 
**lon** | **float** |  | [optional] 
**route_file** | **str** |  | [optional] 
**polyline** | **str** |  | [optional] 
**usage_count** | **int** |  | [optional] 
**owner** | [**AthleteSearchResult**](AthleteSearchResult.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.shared_event import SharedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SharedEvent from a JSON string
shared_event_instance = SharedEvent.from_json(json)
# print the JSON string representation of the object
print(SharedEvent.to_json())

# convert the object into a dict
shared_event_dict = shared_event_instance.to_dict()
# create an instance of SharedEvent from a dict
shared_event_from_dict = SharedEvent.from_dict(shared_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


