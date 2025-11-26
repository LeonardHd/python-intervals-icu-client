# PaceDistancesDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distances** | **List[float]** |  | [optional] 
**defaults** | **List[float]** |  | [optional] 

## Example

```python
from intervals_icu_client.models.pace_distances_dto import PaceDistancesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PaceDistancesDTO from a JSON string
pace_distances_dto_instance = PaceDistancesDTO.from_json(json)
# print the JSON string representation of the object
print(PaceDistancesDTO.to_json())

# convert the object into a dict
pace_distances_dto_dict = pace_distances_dto_instance.to_dict()
# create an instance of PaceDistancesDTO from a dict
pace_distances_dto_from_dict = PaceDistancesDTO.from_dict(pace_distances_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


