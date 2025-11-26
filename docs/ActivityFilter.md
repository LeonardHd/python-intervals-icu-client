# ActivityFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**field_id** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**operator** | **str** |  | [optional] 
**value** | **object** |  | [optional] 
**var_not** | **bool** |  | [optional] 

## Example

```python
from intervals_icu_client.models.activity_filter import ActivityFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityFilter from a JSON string
activity_filter_instance = ActivityFilter.from_json(json)
# print the JSON string representation of the object
print(ActivityFilter.to_json())

# convert the object into a dict
activity_filter_dict = activity_filter_instance.to_dict()
# create an instance of ActivityFilter from a dict
activity_filter_from_dict = ActivityFilter.from_dict(activity_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


