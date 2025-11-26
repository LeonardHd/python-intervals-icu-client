# ActivityHRCurvePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secs** | **List[int]** |  | [optional] 
**curves** | [**List[ActivityHRCurve]**](ActivityHRCurve.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.activity_hr_curve_payload import ActivityHRCurvePayload

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityHRCurvePayload from a JSON string
activity_hr_curve_payload_instance = ActivityHRCurvePayload.from_json(json)
# print the JSON string representation of the object
print(ActivityHRCurvePayload.to_json())

# convert the object into a dict
activity_hr_curve_payload_dict = activity_hr_curve_payload_instance.to_dict()
# create an instance of ActivityHRCurvePayload from a dict
activity_hr_curve_payload_from_dict = ActivityHRCurvePayload.from_dict(activity_hr_curve_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


