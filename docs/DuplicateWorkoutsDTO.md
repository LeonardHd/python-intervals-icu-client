# DuplicateWorkoutsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_copies** | **int** |  | [optional] 
**weeks_between** | **int** |  | [optional] 
**workout_ids** | **List[int]** |  | [optional] 

## Example

```python
from intervals_icu_client.models.duplicate_workouts_dto import DuplicateWorkoutsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateWorkoutsDTO from a JSON string
duplicate_workouts_dto_instance = DuplicateWorkoutsDTO.from_json(json)
# print the JSON string representation of the object
print(DuplicateWorkoutsDTO.to_json())

# convert the object into a dict
duplicate_workouts_dto_dict = duplicate_workouts_dto_instance.to_dict()
# create an instance of DuplicateWorkoutsDTO from a dict
duplicate_workouts_dto_from_dict = DuplicateWorkoutsDTO.from_dict(duplicate_workouts_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


