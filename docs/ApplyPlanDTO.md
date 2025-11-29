# ApplyPlanDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date_local** | **str** |  | [optional] 
**folder_id** | **int** |  | [optional] 
**extra_workouts** | [**List[Workout]**](Workout.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.apply_plan_dto import ApplyPlanDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyPlanDTO from a JSON string
apply_plan_dto_instance = ApplyPlanDTO.from_json(json)
# print the JSON string representation of the object
print(ApplyPlanDTO.to_json())

# convert the object into a dict
apply_plan_dto_dict = apply_plan_dto_instance.to_dict()
# create an instance of ApplyPlanDTO from a dict
apply_plan_dto_from_dict = ApplyPlanDTO.from_dict(apply_plan_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


