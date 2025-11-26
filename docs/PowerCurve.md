# PowerCurve


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
**values** | **List[int]** |  | [optional] 
**submax_values** | **List[List[int]]** |  | [optional] 
**submax_activity_id** | **List[List[str]]** |  | [optional] 
**start_index** | **List[int]** |  | [optional] 
**end_index** | **List[int]** |  | [optional] 
**activity_id** | **List[str]** |  | [optional] 
**watts_per_kg** | **List[float]** |  | [optional] 
**wkg_activity_id** | **List[str]** |  | [optional] 
**submax_watts_per_kg** | **List[List[float]]** |  | [optional] 
**submax_wkg_activity_id** | **List[List[str]]** |  | [optional] 
**power_models** | [**List[PowerModel]**](PowerModel.md) |  | [optional] 
**ranks** | [**Dict[str, Rank]**](Rank.md) |  | [optional] 
**map_plot** | [**Plot**](Plot.md) |  | [optional] 
**stream_type** | **str** |  | [optional] 
**stream_name** | **str** |  | [optional] 
**watts** | **List[int]** |  | [optional] 
**vo2max_5m** | **float** |  | [optional] 
**compound_score_5m** | **float** |  | [optional] 

## Example

```python
from intervals_icu_client.models.power_curve import PowerCurve

# TODO update the JSON string below
json = "{}"
# create an instance of PowerCurve from a JSON string
power_curve_instance = PowerCurve.from_json(json)
# print the JSON string representation of the object
print(PowerCurve.to_json())

# convert the object into a dict
power_curve_dict = power_curve_instance.to_dict()
# create an instance of PowerCurve from a dict
power_curve_from_dict = PowerCurve.from_dict(power_curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


