# ChatMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**athlete_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**profile_medium** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**coach** | **bool** |  | [optional] 
**plan** | **str** |  | [optional] 
**accepted_coaching_group** | **datetime** |  | [optional] 

## Example

```python
from intervals_icu_client.models.chat_member import ChatMember

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMember from a JSON string
chat_member_instance = ChatMember.from_json(json)
# print the JSON string representation of the object
print(ChatMember.to_json())

# convert the object into a dict
chat_member_dict = chat_member_instance.to_dict()
# create an instance of ChatMember from a dict
chat_member_from_dict = ChatMember.from_dict(chat_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


