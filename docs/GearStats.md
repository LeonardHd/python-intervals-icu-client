# GearStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance** | **float** |  | [optional] 
**elapsed_time** | **float** |  | [optional] 
**moving_time** | **float** |  | [optional] 
**activities** | **int** |  | [optional] 

## Example

```python
from intervals_icu_client.models.gear_stats import GearStats

# TODO update the JSON string below
json = "{}"
# create an instance of GearStats from a JSON string
gear_stats_instance = GearStats.from_json(json)
# print the JSON string representation of the object
print(GearStats.to_json())

# convert the object into a dict
gear_stats_dict = gear_stats_instance.to_dict()
# create an instance of GearStats from a dict
gear_stats_from_dict = GearStats.from_dict(gear_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


