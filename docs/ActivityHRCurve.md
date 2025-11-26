# ActivityHRCurve


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**start_date_local** | **str** |  | [optional] 
**weight** | **float** |  | [optional] 
**bpm** | **List[int]** |  | [optional] 

## Example

```python
from intervals_icu_client.models.activity_hr_curve import ActivityHRCurve

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityHRCurve from a JSON string
activity_hr_curve_instance = ActivityHRCurve.from_json(json)
# print the JSON string representation of the object
print(ActivityHRCurve.to_json())

# convert the object into a dict
activity_hr_curve_dict = activity_hr_curve_instance.to_dict()
# create an instance of ActivityHRCurve from a dict
activity_hr_curve_from_dict = ActivityHRCurve.from_dict(activity_hr_curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


