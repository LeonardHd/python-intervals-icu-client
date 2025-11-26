# IcuAchievement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**watts** | **int** |  | [optional] 
**secs** | **int** |  | [optional] 
**value** | **int** |  | [optional] 
**distance** | **float** |  | [optional] 
**pace** | **float** |  | [optional] 
**point** | [**DataCurvePt**](DataCurvePt.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.icu_achievement import IcuAchievement

# TODO update the JSON string below
json = "{}"
# create an instance of IcuAchievement from a JSON string
icu_achievement_instance = IcuAchievement.from_json(json)
# print the JSON string representation of the object
print(IcuAchievement.to_json())

# convert the object into a dict
icu_achievement_dict = icu_achievement_instance.to_dict()
# create an instance of IcuAchievement from a dict
icu_achievement_from_dict = IcuAchievement.from_dict(icu_achievement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


