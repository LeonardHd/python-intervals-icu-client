# CustomItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**athlete_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**content** | **Dict[str, object]** |  | [optional] 
**usage_count** | **int** |  | [optional] 
**index** | **int** |  | [optional] 
**hide_script** | **bool** |  | [optional] 
**hidden_by_id** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**from_athlete** | [**AthleteSearchResult**](AthleteSearchResult.md) |  | [optional] 
**from_id** | **int** |  | [optional] 

## Example

```python
from intervals_icu_client.models.custom_item import CustomItem

# TODO update the JSON string below
json = "{}"
# create an instance of CustomItem from a JSON string
custom_item_instance = CustomItem.from_json(json)
# print the JSON string representation of the object
print(CustomItem.to_json())

# convert the object into a dict
custom_item_dict = custom_item_instance.to_dict()
# create an instance of CustomItem from a dict
custom_item_from_dict = CustomItem.from_dict(custom_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


