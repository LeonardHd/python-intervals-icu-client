# AthleteSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**profile_medium** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**sex** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from intervals_icu_client.models.athlete_search_result import AthleteSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of AthleteSearchResult from a JSON string
athlete_search_result_instance = AthleteSearchResult.from_json(json)
# print the JSON string representation of the object
print(AthleteSearchResult.to_json())

# convert the object into a dict
athlete_search_result_dict = athlete_search_result_instance.to_dict()
# create an instance of AthleteSearchResult from a dict
athlete_search_result_from_dict = AthleteSearchResult.from_dict(athlete_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


