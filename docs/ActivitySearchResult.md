# ActivitySearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**start_date_local** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**race** | **bool** |  | [optional] 
**distance** | **float** |  | [optional] 
**moving_time** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from intervals_icu_client.models.activity_search_result import ActivitySearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of ActivitySearchResult from a JSON string
activity_search_result_instance = ActivitySearchResult.from_json(json)
# print the JSON string representation of the object
print(ActivitySearchResult.to_json())

# convert the object into a dict
activity_search_result_dict = activity_search_result_instance.to_dict()
# create an instance of ActivitySearchResult from a dict
activity_search_result_from_dict = ActivitySearchResult.from_dict(activity_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


