# WithCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**athlete_id** | **str** |  | [optional] 
**route_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**rename_activities** | **bool** |  | [optional] 
**commute** | **bool** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**replaced_by_route_id** | **int** |  | [optional] 
**latlngs** | **List[List[float]]** |  | [optional] 
**distance** | **float** |  | [optional] 
**activity_count** | **int** |  | [optional] 
**most_recent_id** | **str** |  | [optional] 
**most_recent_start_date_local** | **str** |  | [optional] 
**most_recent_type** | **str** |  | [optional] 

## Example

```python
from intervals_icu_client.models.with_count import WithCount

# TODO update the JSON string below
json = "{}"
# create an instance of WithCount from a JSON string
with_count_instance = WithCount.from_json(json)
# print the JSON string representation of the object
print(WithCount.to_json())

# convert the object into a dict
with_count_dict = with_count_instance.to_dict()
# create an instance of WithCount from a dict
with_count_from_dict = WithCount.from_dict(with_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


