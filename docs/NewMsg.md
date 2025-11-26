# NewMsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**new_chat** | [**Chat**](Chat.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.new_msg import NewMsg

# TODO update the JSON string below
json = "{}"
# create an instance of NewMsg from a JSON string
new_msg_instance = NewMsg.from_json(json)
# print the JSON string representation of the object
print(NewMsg.to_json())

# convert the object into a dict
new_msg_dict = new_msg_instance.to_dict()
# create an instance of NewMsg from a dict
new_msg_from_dict = NewMsg.from_dict(new_msg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


