# EventEx


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**start_date_local** | **str** |  | [optional] 
**icu_training_load** | **int** |  | [optional] 
**icu_atl** | **float** |  | [optional] 
**icu_ctl** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**carbs_used** | **int** |  | [optional] 
**ss_p_max** | **float** |  | [optional] 
**ss_w_prime** | **float** |  | [optional] 
**ss_cp** | **float** |  | [optional] 
**calendar_id** | **int** |  | [optional] 
**uid** | **str** |  | [optional] 
**athlete_id** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**end_date_local** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**indoor** | **bool** |  | [optional] 
**color** | **str** |  | [optional] 
**moving_time** | **int** |  | [optional] 
**icu_ftp** | **int** |  | [optional] 
**w_prime** | **int** |  | [optional] 
**p_max** | **int** |  | [optional] 
**atl_days** | **int** |  | [optional] 
**ctl_days** | **int** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**not_on_fitness_chart** | **bool** |  | [optional] 
**show_as_note** | **bool** |  | [optional] 
**show_on_ctl_line** | **bool** |  | [optional] 
**for_week** | **bool** |  | [optional] 
**target** | **str** |  | [optional] 
**joules** | **int** |  | [optional] 
**joules_above_ftp** | **int** |  | [optional] 
**push_errors** | [**List[PushError]**](PushError.md) |  | [optional] 
**athlete_cannot_edit** | **bool** |  | [optional] 
**hide_from_athlete** | **bool** |  | [optional] 
**structure_read_only** | **bool** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**shared_event_id** | **int** |  | [optional] 
**entered** | **bool** |  | [optional] 
**carbs_per_hour** | **int** |  | [optional] 
**sub_type** | **str** |  | [optional] 
**distance** | **float** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**attachments** | [**List[Attachment]**](Attachment.md) |  | [optional] 
**oauth_client_id** | **int** |  | [optional] 
**external_id** | **str** |  | [optional] 
**load_target** | **int** |  | [optional] 
**time_target** | **int** |  | [optional] 
**distance_target** | **float** |  | [optional] 
**plan_athlete_id** | **str** |  | [optional] 
**plan_folder_id** | **int** |  | [optional] 
**plan_workout_id** | **int** |  | [optional] 
**plan_applied** | **datetime** |  | [optional] 
**workout** | [**Workout**](Workout.md) |  | [optional] 
**file_contents** | **str** |  | [optional] 
**file_contents_base64** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**icu_intensity** | **float** |  | [optional] 
**strain_score** | **float** |  | [optional] 

## Example

```python
from intervals_icu_client.models.event_ex import EventEx

# TODO update the JSON string below
json = "{}"
# create an instance of EventEx from a JSON string
event_ex_instance = EventEx.from_json(json)
# print the JSON string representation of the object
print(EventEx.to_json())

# convert the object into a dict
event_ex_dict = event_ex_instance.to_dict()
# create an instance of EventEx from a dict
event_ex_from_dict = EventEx.from_dict(event_ex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


