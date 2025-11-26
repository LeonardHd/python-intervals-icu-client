# HRRecovery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_index** | **int** |  | [optional] 
**end_index** | **int** |  | [optional] 
**start_time** | **int** |  | [optional] 
**end_time** | **int** |  | [optional] 
**start_bpm** | **int** |  | [optional] 
**end_bpm** | **int** |  | [optional] 
**average_watts** | **int** |  | [optional] 
**hrr** | **int** |  | [optional] 

## Example

```python
from intervals_icu_client.models.hr_recovery import HRRecovery

# TODO update the JSON string below
json = "{}"
# create an instance of HRRecovery from a JSON string
hr_recovery_instance = HRRecovery.from_json(json)
# print the JSON string representation of the object
print(HRRecovery.to_json())

# convert the object into a dict
hr_recovery_dict = hr_recovery_instance.to_dict()
# create an instance of HRRecovery from a dict
hr_recovery_from_dict = HRRecovery.from_dict(hr_recovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


