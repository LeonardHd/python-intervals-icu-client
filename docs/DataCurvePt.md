# DataCurvePt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_index** | **int** |  | [optional] 
**end_index** | **int** |  | [optional] 
**secs** | **int** |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from intervals_icu_client.models.data_curve_pt import DataCurvePt

# TODO update the JSON string below
json = "{}"
# create an instance of DataCurvePt from a JSON string
data_curve_pt_instance = DataCurvePt.from_json(json)
# print the JSON string representation of the object
print(DataCurvePt.to_json())

# convert the object into a dict
data_curve_pt_dict = data_curve_pt_instance.to_dict()
# create an instance of DataCurvePt from a dict
data_curve_pt_from_dict = DataCurvePt.from_dict(data_curve_pt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


