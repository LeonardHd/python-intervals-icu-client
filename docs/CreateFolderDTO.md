# CreateFolderDTO


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
**copy_folder_id** | **int** |  | [optional] 

## Example

```python
from intervals_icu_client.models.create_folder_dto import CreateFolderDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFolderDTO from a JSON string
create_folder_dto_instance = CreateFolderDTO.from_json(json)
# print the JSON string representation of the object
print(CreateFolderDTO.to_json())

# convert the object into a dict
create_folder_dto_dict = create_folder_dto_instance.to_dict()
# create an instance of CreateFolderDTO from a dict
create_folder_dto_from_dict = CreateFolderDTO.from_dict(create_folder_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


