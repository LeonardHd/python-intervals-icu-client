# DataCurve


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**after_kj** | **int** |  | [optional] 
**filters** | [**List[ActivityFilter]**](ActivityFilter.md) |  | [optional] 
**label** | **str** |  | [optional] 
**filter_label** | **str** |  | [optional] 
**percentile** | **float** |  | [optional] 
**start_date_local** | **str** |  | [optional] 
**end_date_local** | **str** |  | [optional] 
**days** | **int** |  | [optional] 
**moving_time** | **int** |  | [optional] 
**training_load** | **int** |  | [optional] 
**weight** | **float** |  | [optional] 
**secs** | **List[int]** |  | [optional] 
**distance** | **List[float]** |  | [optional] 
**values** | **List[int]** |  | [optional] 
**submax_values** | **List[List[int]]** |  | [optional] 
**submax_activity_id** | **List[List[str]]** |  | [optional] 
**start_index** | **List[int]** |  | [optional] 
**end_index** | **List[int]** |  | [optional] 
**activity_id** | **List[str]** |  | [optional] 

## Example

```python
from intervals_icu_client.models.data_curve import DataCurve

# TODO update the JSON string below
json = "{}"
# create an instance of DataCurve from a JSON string
data_curve_instance = DataCurve.from_json(json)
# print the JSON string representation of the object
print(DataCurve.to_json())

# convert the object into a dict
data_curve_dict = data_curve_instance.to_dict()
# create an instance of DataCurve from a dict
data_curve_from_dict = DataCurve.from_dict(data_curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


