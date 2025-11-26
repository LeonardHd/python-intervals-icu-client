# SportInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**eftp** | **float** |  | [optional] 
**w_prime** | **float** |  | [optional] 
**p_max** | **float** |  | [optional] 

## Example

```python
from intervals_icu_client.models.sport_info import SportInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SportInfo from a JSON string
sport_info_instance = SportInfo.from_json(json)
# print the JSON string representation of the object
print(SportInfo.to_json())

# convert the object into a dict
sport_info_dict = sport_info_instance.to_dict()
# create an instance of SportInfo from a dict
sport_info_from_dict = SportInfo.from_dict(sport_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


