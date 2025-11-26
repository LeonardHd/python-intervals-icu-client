# ActivityPowerCurvePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_kj** | **int** |  | [optional] 
**secs** | **List[int]** |  | [optional] 
**curves** | [**List[ActivityPowerCurve]**](ActivityPowerCurve.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.activity_power_curve_payload import ActivityPowerCurvePayload

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityPowerCurvePayload from a JSON string
activity_power_curve_payload_instance = ActivityPowerCurvePayload.from_json(json)
# print the JSON string representation of the object
print(ActivityPowerCurvePayload.to_json())

# convert the object into a dict
activity_power_curve_payload_dict = activity_power_curve_payload_instance.to_dict()
# create an instance of ActivityPowerCurvePayload from a dict
activity_power_curve_payload_from_dict = ActivityPowerCurvePayload.from_dict(activity_power_curve_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


