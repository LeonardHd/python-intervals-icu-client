# PaceModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**critical_speed** | **float** |  | [optional] 
**d_prime** | **float** |  | [optional] 
**r2** | **float** |  | [optional] 
**input_point_indexes** | **List[int]** |  | [optional] 

## Example

```python
from intervals_icu_client.models.pace_model import PaceModel

# TODO update the JSON string below
json = "{}"
# create an instance of PaceModel from a JSON string
pace_model_instance = PaceModel.from_json(json)
# print the JSON string representation of the object
print(PaceModel.to_json())

# convert the object into a dict
pace_model_dict = pace_model_instance.to_dict()
# create an instance of PaceModel from a dict
pace_model_from_dict = PaceModel.from_dict(pace_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


