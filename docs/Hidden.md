# Hidden


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**icu_athlete_id** | **str** |  | [optional] 
**start_date_local** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from intervals_icu_client.models.hidden import Hidden

# TODO update the JSON string below
json = "{}"
# create an instance of Hidden from a JSON string
hidden_instance = Hidden.from_json(json)
# print the JSON string representation of the object
print(Hidden.to_json())

# convert the object into a dict
hidden_dict = hidden_instance.to_dict()
# create an instance of Hidden from a dict
hidden_from_dict = Hidden.from_dict(hidden_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


