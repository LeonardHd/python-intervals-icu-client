# ActivityPowerCurve


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**start_date_local** | **str** |  | [optional] 
**weight** | **float** |  | [optional] 
**watts** | **List[int]** |  | [optional] 

## Example

```python
from intervals_icu_client.models.activity_power_curve import ActivityPowerCurve

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityPowerCurve from a JSON string
activity_power_curve_instance = ActivityPowerCurve.from_json(json)
# print the JSON string representation of the object
print(ActivityPowerCurve.to_json())

# convert the object into a dict
activity_power_curve_dict = activity_power_curve_instance.to_dict()
# create an instance of ActivityPowerCurve from a dict
activity_power_curve_from_dict = ActivityPowerCurve.from_dict(activity_power_curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


