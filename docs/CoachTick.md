# CoachTick


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from intervals_icu_client.models.coach_tick import CoachTick

# TODO update the JSON string below
json = "{}"
# create an instance of CoachTick from a JSON string
coach_tick_instance = CoachTick.from_json(json)
# print the JSON string representation of the object
print(CoachTick.to_json())

# convert the object into a dict
coach_tick_dict = coach_tick_instance.to_dict()
# create an instance of CoachTick from a dict
coach_tick_from_dict = CoachTick.from_dict(coach_tick_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


