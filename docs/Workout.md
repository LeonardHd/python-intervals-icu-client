# Workout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**athlete_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**icu_training_load** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**indoor** | **bool** |  | [optional] 
**color** | **str** |  | [optional] 
**moving_time** | **int** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**joules** | **int** |  | [optional] 
**joules_above_ftp** | **int** |  | [optional] 
**workout_doc** | **Dict[str, object]** |  | [optional] 
**folder_id** | **int** |  | [optional] 
**day** | **int** |  | [optional] 
**days** | **int** |  | [optional] 
**plan_applied** | **datetime** |  | [optional] 
**hide_from_athlete** | **bool** |  | [optional] 
**target** | **str** |  | [optional] 
**targets** | **List[str]** |  | [optional] 
**carbs_per_hour** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**attachments** | [**List[Attachment]**](Attachment.md) |  | [optional] 
**time** | **str** |  | [optional] 
**sub_type** | **str** |  | [optional] 
**for_week** | **bool** |  | [optional] 
**distance** | **float** |  | [optional] 
**icu_intensity** | **float** |  | [optional] 

## Example

```python
from intervals_icu_client.models.workout import Workout

# TODO update the JSON string below
json = "{}"
# create an instance of Workout from a JSON string
workout_instance = Workout.from_json(json)
# print the JSON string representation of the object
print(Workout.to_json())

# convert the object into a dict
workout_dict = workout_instance.to_dict()
# create an instance of Workout from a dict
workout_from_dict = Workout.from_dict(workout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


