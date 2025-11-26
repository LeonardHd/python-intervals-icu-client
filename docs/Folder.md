# Folder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**athlete_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**children** | [**List[Workout]**](Workout.md) |  | [optional] 
**visibility** | **str** |  | [optional] 
**start_date_local** | **str** |  | [optional] 
**rollout_weeks** | **int** |  | [optional] 
**auto_rollout_day** | **int** |  | [optional] 
**read_only_workouts** | **bool** |  | [optional] 
**starting_ctl** | **int** |  | [optional] 
**starting_atl** | **int** |  | [optional] 
**activity_types** | **List[str]** |  | [optional] 
**num_workouts** | **int** |  | [optional] 
**duration_weeks** | **int** |  | [optional] 
**hours_per_week_min** | **int** |  | [optional] 
**hours_per_week_max** | **int** |  | [optional] 
**workout_targets** | **List[str]** |  | [optional] 
**blurb** | **str** |  | [optional] 
**can_edit** | **bool** |  | [optional] 
**shared_with_count** | **int** |  | [optional] 
**share_token** | **str** |  | [optional] 
**owner** | [**AthleteSearchResult**](AthleteSearchResult.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.folder import Folder

# TODO update the JSON string below
json = "{}"
# create an instance of Folder from a JSON string
folder_instance = Folder.from_json(json)
# print the JSON string representation of the object
print(Folder.to_json())

# convert the object into a dict
folder_dict = folder_instance.to_dict()
# create an instance of Folder from a dict
folder_from_dict = Folder.from_dict(folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


