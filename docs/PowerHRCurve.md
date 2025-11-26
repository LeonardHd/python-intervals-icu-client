# PowerHRCurve


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**athlete_id** | **str** |  | [optional] 
**start** | **str** |  | [optional] 
**end** | **str** |  | [optional] 
**min_watts** | **int** |  | [optional] 
**max_watts** | **int** |  | [optional] 
**bucket_size** | **int** |  | [optional] 
**bpm** | **List[int]** |  | [optional] 
**cadence** | **List[int]** |  | [optional] 
**minutes** | **List[int]** |  | [optional] 
**lthr** | **int** |  | [optional] 
**max_hr** | **int** |  | [optional] 
**ftp** | **int** |  | [optional] 

## Example

```python
from intervals_icu_client.models.power_hr_curve import PowerHRCurve

# TODO update the JSON string below
json = "{}"
# create an instance of PowerHRCurve from a JSON string
power_hr_curve_instance = PowerHRCurve.from_json(json)
# print the JSON string representation of the object
print(PowerHRCurve.to_json())

# convert the object into a dict
power_hr_curve_dict = power_hr_curve_instance.to_dict()
# create an instance of PowerHRCurve from a dict
power_hr_curve_from_dict = PowerHRCurve.from_dict(power_hr_curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


