# Chat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**coaching_group** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**picture** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**pub** | **bool** |  | [optional] 
**join_policy** | **str** |  | [optional] 
**sidebar_logo** | **str** |  | [optional] 
**sidebar_color** | **str** |  | [optional] 
**sidebar_dark** | **bool** |  | [optional] 
**sidebar_top_color** | **str** |  | [optional] 
**hide_members** | **bool** |  | [optional] 
**members_cannot_chat** | **bool** |  | [optional] 
**primary_group** | **bool** |  | [optional] 
**coins** | **float** |  | [optional] 
**members** | [**List[ChatMember]**](ChatMember.md) |  | [optional] 
**athlete_id** | **str** |  | [optional] 
**activity_id** | **str** |  | [optional] 
**other_athlete_id** | **str** |  | [optional] 
**other_athlete_sex** | **str** |  | [optional] 
**follows_you** | **str** |  | [optional] 
**you_follow** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**new_message_count** | **int** |  | [optional] 
**kicked** | **datetime** |  | [optional] 
**kicked_by_id** | **str** |  | [optional] 
**last_seen_message_id** | **int** |  | [optional] 
**mute_until** | **datetime** |  | [optional] 
**shared_folders** | [**List[Folder]**](Folder.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.chat import Chat

# TODO update the JSON string below
json = "{}"
# create an instance of Chat from a JSON string
chat_instance = Chat.from_json(json)
# print the JSON string representation of the object
print(Chat.to_json())

# convert the object into a dict
chat_dict = chat_instance.to_dict()
# create an instance of Chat from a dict
chat_from_dict = Chat.from_dict(chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


