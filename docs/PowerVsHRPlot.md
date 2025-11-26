# PowerVsHRPlot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_size** | **int** |  | [optional] 
**warmup** | **int** |  | [optional] 
**cooldown** | **int** |  | [optional] 
**elapsed_time** | **int** |  | [optional] 
**hr_lag** | **int** |  | [optional] 
**power_hr** | **float** |  | [optional] 
**power_hr_first** | **float** |  | [optional] 
**power_hr_second** | **float** |  | [optional] 
**decoupling** | **float** |  | [optional] 
**power_hr_z2** | **float** |  | [optional] 
**median_cadence_z2** | **int** |  | [optional] 
**avg_cadence_z2** | **int** |  | [optional] 
**hr_z2_bucket_count** | **int** |  | [optional] 
**start** | **int** |  | [optional] 
**mid** | **int** |  | [optional] 
**end** | **int** |  | [optional] 
**series** | [**List[Bucket]**](Bucket.md) |  | [optional] 
**curves** | [**List[Curve]**](Curve.md) |  | [optional] 
**ratio_coefficients** | **List[float]** |  | [optional] 

## Example

```python
from intervals_icu_client.models.power_vs_hr_plot import PowerVsHRPlot

# TODO update the JSON string below
json = "{}"
# create an instance of PowerVsHRPlot from a JSON string
power_vs_hr_plot_instance = PowerVsHRPlot.from_json(json)
# print the JSON string representation of the object
print(PowerVsHRPlot.to_json())

# convert the object into a dict
power_vs_hr_plot_dict = power_vs_hr_plot_instance.to_dict()
# create an instance of PowerVsHRPlot from a dict
power_vs_hr_plot_from_dict = PowerVsHRPlot.from_dict(power_vs_hr_plot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


