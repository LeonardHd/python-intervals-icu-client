# GearReminder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**gear_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**distance** | **float** |  | [optional] 
**time** | **float** |  | [optional] 
**activities** | **int** |  | [optional] 
**days** | **int** |  | [optional] 
**last_reset** | **datetime** |  | [optional] 
**starting_distance** | **float** |  | [optional] 
**starting_time** | **float** |  | [optional] 
**starting_activities** | **int** |  | [optional] 
**snoozed_until** | **datetime** |  | [optional] 
**percent_used** | **float** |  | [optional] 
**distance_used** | **float** |  | [optional] 
**time_used** | **float** |  | [optional] 
**activities_used** | **int** |  | [optional] 
**days_used** | **int** |  | [optional] 

## Example

```python
from intervals_icu_client.models.gear_reminder import GearReminder

# TODO update the JSON string below
json = "{}"
# create an instance of GearReminder from a JSON string
gear_reminder_instance = GearReminder.from_json(json)
# print the JSON string representation of the object
print(GearReminder.to_json())

# convert the object into a dict
gear_reminder_dict = gear_reminder_instance.to_dict()
# create an instance of GearReminder from a dict
gear_reminder_from_dict = GearReminder.from_dict(gear_reminder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


