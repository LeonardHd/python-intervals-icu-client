# Event


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
**workout_doc** | [**WorkoutDoc**](WorkoutDoc.md) |  | [optional] 
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
**icu_intensity** | **float** |  | [optional] 
**strain_score** | **float** |  | [optional] 

## Example

```python
from intervals_icu_client.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


