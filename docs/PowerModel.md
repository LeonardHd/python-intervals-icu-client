# PowerModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**critical_power** | **int** |  | [optional] 
**w_prime** | **int** |  | [optional] 
**p_max** | **int** |  | [optional] 
**input_point_indexes** | **List[int]** |  | [optional] 
**ftp** | **int** |  | [optional] 

## Example

```python
from intervals_icu_client.models.power_model import PowerModel

# TODO update the JSON string below
json = "{}"
# create an instance of PowerModel from a JSON string
power_model_instance = PowerModel.from_json(json)
# print the JSON string representation of the object
print(PowerModel.to_json())

# convert the object into a dict
power_model_dict = power_model_instance.to_dict()
# create an instance of PowerModel from a dict
power_model_from_dict = PowerModel.from_dict(power_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


