# HRLoadModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**icu_training_load** | **int** |  | [optional] 
**training_data_count** | **int** |  | [optional] 

## Example

```python
from intervals_icu_client.models.hr_load_model import HRLoadModel

# TODO update the JSON string below
json = "{}"
# create an instance of HRLoadModel from a JSON string
hr_load_model_instance = HRLoadModel.from_json(json)
# print the JSON string representation of the object
print(HRLoadModel.to_json())

# convert the object into a dict
hr_load_model_dict = hr_load_model_instance.to_dict()
# create an instance of HRLoadModel from a dict
hr_load_model_from_dict = HRLoadModel.from_dict(hr_load_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


