# AthleteTrainingPlanUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**training_plan_id** | **int** |  | [optional] 
**training_plan_start_date** | **str** |  | [optional] 
**training_plan_alias** | **str** |  | [optional] 

## Example

```python
from intervals_icu_client.models.athlete_training_plan_update import AthleteTrainingPlanUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AthleteTrainingPlanUpdate from a JSON string
athlete_training_plan_update_instance = AthleteTrainingPlanUpdate.from_json(json)
# print the JSON string representation of the object
print(AthleteTrainingPlanUpdate.to_json())

# convert the object into a dict
athlete_training_plan_update_dict = athlete_training_plan_update_instance.to_dict()
# create an instance of AthleteTrainingPlanUpdate from a dict
athlete_training_plan_update_from_dict = AthleteTrainingPlanUpdate.from_dict(athlete_training_plan_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


