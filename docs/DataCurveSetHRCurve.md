# DataCurveSetHRCurve


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[DataCurve]**](DataCurve.md) |  | [optional] 
**activities** | [**Dict[str, Activity]**](Activity.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.data_curve_set_hr_curve import DataCurveSetHRCurve

# TODO update the JSON string below
json = "{}"
# create an instance of DataCurveSetHRCurve from a JSON string
data_curve_set_hr_curve_instance = DataCurveSetHRCurve.from_json(json)
# print the JSON string representation of the object
print(DataCurveSetHRCurve.to_json())

# convert the object into a dict
data_curve_set_hr_curve_dict = data_curve_set_hr_curve_instance.to_dict()
# create an instance of DataCurveSetHRCurve from a dict
data_curve_set_hr_curve_from_dict = DataCurveSetHRCurve.from_dict(data_curve_set_hr_curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


