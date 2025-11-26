# Gear


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**athlete_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**purchased** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**distance** | **float** |  | [optional] 
**time** | **float** |  | [optional] 
**activities** | **int** |  | [optional] 
**use_elapsed_time** | **bool** |  | [optional] 
**retired** | **str** |  | [optional] 
**component_ids** | **List[str]** |  | [optional] 
**reminders** | [**List[GearReminder]**](GearReminder.md) |  | [optional] 
**activity_filters** | [**List[ActivityFilter]**](ActivityFilter.md) |  | [optional] 
**component** | **bool** |  | [optional] 

## Example

```python
from intervals_icu_client.models.gear import Gear

# TODO update the JSON string below
json = "{}"
# create an instance of Gear from a JSON string
gear_instance = Gear.from_json(json)
# print the JSON string representation of the object
print(Gear.to_json())

# convert the object into a dict
gear_dict = gear_instance.to_dict()
# create an instance of Gear from a dict
gear_from_dict = Gear.from_dict(gear_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


