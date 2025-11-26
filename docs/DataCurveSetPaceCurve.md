# DataCurveSetPaceCurve


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[DataCurve]**](DataCurve.md) |  | [optional] 
**activities** | [**Dict[str, Activity]**](Activity.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.data_curve_set_pace_curve import DataCurveSetPaceCurve

# TODO update the JSON string below
json = "{}"
# create an instance of DataCurveSetPaceCurve from a JSON string
data_curve_set_pace_curve_instance = DataCurveSetPaceCurve.from_json(json)
# print the JSON string representation of the object
print(DataCurveSetPaceCurve.to_json())

# convert the object into a dict
data_curve_set_pace_curve_dict = data_curve_set_pace_curve_instance.to_dict()
# create an instance of DataCurveSetPaceCurve from a dict
data_curve_set_pace_curve_from_dict = DataCurveSetPaceCurve.from_dict(data_curve_set_pace_curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


