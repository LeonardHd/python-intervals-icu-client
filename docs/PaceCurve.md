# PaceCurve


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
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
**distance** | **List[float]** |  | [optional] 
**values** | **List[int]** |  | [optional] 
**submax_values** | **List[List[int]]** |  | [optional] 
**submax_activity_id** | **List[List[str]]** |  | [optional] 
**start_index** | **List[int]** |  | [optional] 
**end_index** | **List[int]** |  | [optional] 
**activity_id** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 
**pace_models** | [**List[PaceModel]**](PaceModel.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.pace_curve import PaceCurve

# TODO update the JSON string below
json = "{}"
# create an instance of PaceCurve from a JSON string
pace_curve_instance = PaceCurve.from_json(json)
# print the JSON string representation of the object
print(PaceCurve.to_json())

# convert the object into a dict
pace_curve_dict = pace_curve_instance.to_dict()
# create an instance of PaceCurve from a dict
pace_curve_from_dict = PaceCurve.from_dict(pace_curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


