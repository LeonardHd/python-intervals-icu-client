# WorkoutEx


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
**file_contents** | **str** |  | [optional] 
**file_contents_base64** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**distance** | **float** |  | [optional] 
**icu_intensity** | **float** |  | [optional] 

## Example

```python
from intervals_icu_client.models.workout_ex import WorkoutEx

# TODO update the JSON string below
json = "{}"
# create an instance of WorkoutEx from a JSON string
workout_ex_instance = WorkoutEx.from_json(json)
# print the JSON string representation of the object
print(WorkoutEx.to_json())

# convert the object into a dict
workout_ex_dict = workout_ex_instance.to_dict()
# create an instance of WorkoutEx from a dict
workout_ex_from_dict = WorkoutEx.from_dict(workout_ex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


