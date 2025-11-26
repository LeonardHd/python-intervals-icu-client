# PushError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**var_date** | **datetime** |  | [optional] 

## Example

```python
from intervals_icu_client.models.push_error import PushError

# TODO update the JSON string below
json = "{}"
# create an instance of PushError from a JSON string
push_error_instance = PushError.from_json(json)
# print the JSON string representation of the object
print(PushError.to_json())

# convert the object into a dict
push_error_dict = push_error_instance.to_dict()
# create an instance of PushError from a dict
push_error_from_dict = PushError.from_dict(push_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


