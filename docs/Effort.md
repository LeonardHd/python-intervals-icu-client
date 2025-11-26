# Effort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_index** | **int** |  | [optional] 
**end_index** | **int** |  | [optional] 
**average** | **float** |  | [optional] 
**duration** | **int** |  | [optional] 
**distance** | **float** |  | [optional] 

## Example

```python
from intervals_icu_client.models.effort import Effort

# TODO update the JSON string below
json = "{}"
# create an instance of Effort from a JSON string
effort_instance = Effort.from_json(json)
# print the JSON string representation of the object
print(Effort.to_json())

# convert the object into a dict
effort_dict = effort_instance.to_dict()
# create an instance of Effort from a dict
effort_from_dict = Effort.from_dict(effort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


