# Wellness


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**ctl** | **float** |  | [optional] 
**atl** | **float** |  | [optional] 
**ramp_rate** | **float** |  | [optional] 
**ctl_load** | **float** |  | [optional] 
**atl_load** | **float** |  | [optional] 
**sport_info** | [**List[SportInfo]**](SportInfo.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 
**weight** | **float** |  | [optional] 
**resting_hr** | **int** |  | [optional] 
**hrv** | **float** |  | [optional] 
**hrv_sdnn** | **float** |  | [optional] 
**menstrual_phase** | **str** |  | [optional] 
**menstrual_phase_predicted** | **str** |  | [optional] 
**kcal_consumed** | **int** |  | [optional] 
**sleep_secs** | **int** |  | [optional] 
**sleep_score** | **float** |  | [optional] 
**sleep_quality** | **int** |  | [optional] 
**avg_sleeping_hr** | **float** |  | [optional] 
**soreness** | **int** |  | [optional] 
**fatigue** | **int** |  | [optional] 
**stress** | **int** |  | [optional] 
**mood** | **int** |  | [optional] 
**motivation** | **int** |  | [optional] 
**injury** | **int** |  | [optional] 
**sp_o2** | **float** |  | [optional] 
**systolic** | **int** |  | [optional] 
**diastolic** | **int** |  | [optional] 
**hydration** | **int** |  | [optional] 
**hydration_volume** | **float** |  | [optional] 
**readiness** | **float** |  | [optional] 
**baevsky_si** | **float** |  | [optional] 
**blood_glucose** | **float** |  | [optional] 
**lactate** | **float** |  | [optional] 
**body_fat** | **float** |  | [optional] 
**abdomen** | **float** |  | [optional] 
**vo2max** | **float** |  | [optional] 
**comments** | **str** |  | [optional] 
**steps** | **int** |  | [optional] 
**respiration** | **float** |  | [optional] 
**locked** | **bool** |  | [optional] 
**temp_weight** | **bool** |  | [optional] 
**temp_resting_hr** | **bool** |  | [optional] 

## Example

```python
from intervals_icu_client.models.wellness import Wellness

# TODO update the JSON string below
json = "{}"
# create an instance of Wellness from a JSON string
wellness_instance = Wellness.from_json(json)
# print the JSON string representation of the object
print(Wellness.to_json())

# convert the object into a dict
wellness_dict = wellness_instance.to_dict()
# create an instance of Wellness from a dict
wellness_from_dict = Wellness.from_dict(wellness_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


