# AthleteTrainingPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**athlete_id** | **str** |  | [optional] 
**training_plan_id** | **int** |  | [optional] 
**training_plan_start_date** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**training_plan_last_applied** | **datetime** |  | [optional] 
**training_plan** | [**Folder**](Folder.md) |  | [optional] 
**training_plan_alias** | **str** |  | [optional] 

## Example

```python
from intervals_icu_client.models.athlete_training_plan import AthleteTrainingPlan

# TODO update the JSON string below
json = "{}"
# create an instance of AthleteTrainingPlan from a JSON string
athlete_training_plan_instance = AthleteTrainingPlan.from_json(json)
# print the JSON string representation of the object
print(AthleteTrainingPlan.to_json())

# convert the object into a dict
athlete_training_plan_dict = athlete_training_plan_instance.to_dict()
# create an instance of AthleteTrainingPlan from a dict
athlete_training_plan_from_dict = AthleteTrainingPlan.from_dict(athlete_training_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


