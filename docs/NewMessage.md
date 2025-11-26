# NewMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**athlete_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**activity_id** | **str** |  | [optional] 
**start_index** | **int** |  | [optional] 
**end_index** | **int** |  | [optional] 
**answer** | **str** |  | [optional] 
**activity** | [**Activity**](Activity.md) |  | [optional] 
**attachment_url** | **str** |  | [optional] 
**attachment_mime_type** | **str** |  | [optional] 
**deleted** | **datetime** |  | [optional] 
**deleted_by_id** | **str** |  | [optional] 
**join_group_id** | **int** |  | [optional] 
**accept_coaching_group_id** | **int** |  | [optional] 
**seen** | **bool** |  | [optional] 
**chat_id** | **int** |  | [optional] 
**to_athlete_id** | **str** |  | [optional] 
**to_activity_id** | **str** |  | [optional] 
**ask_a_coach** | **bool** |  | [optional] 
**attachment_id** | **str** |  | [optional] 

## Example

```python
from intervals_icu_client.models.new_message import NewMessage

# TODO update the JSON string below
json = "{}"
# create an instance of NewMessage from a JSON string
new_message_instance = NewMessage.from_json(json)
# print the JSON string representation of the object
print(NewMessage.to_json())

# convert the object into a dict
new_message_dict = new_message_instance.to_dict()
# create an instance of NewMessage from a dict
new_message_from_dict = NewMessage.from_dict(new_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


