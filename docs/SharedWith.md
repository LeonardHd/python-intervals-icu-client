# SharedWith


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**profile_medium** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**sex** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**can_edit** | **bool** |  | [optional] 

## Example

```python
from intervals_icu_client.models.shared_with import SharedWith

# TODO update the JSON string below
json = "{}"
# create an instance of SharedWith from a JSON string
shared_with_instance = SharedWith.from_json(json)
# print the JSON string representation of the object
print(SharedWith.to_json())

# convert the object into a dict
shared_with_dict = shared_with_instance.to_dict()
# create an instance of SharedWith from a dict
shared_with_from_dict = SharedWith.from_dict(shared_with_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


