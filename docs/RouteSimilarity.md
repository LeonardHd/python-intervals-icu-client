# RouteSimilarity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route** | [**AthleteRoute**](AthleteRoute.md) |  | [optional] 
**route_distance** | **float** |  | [optional] 
**route_activity_count** | **int** |  | [optional] 
**other** | [**AthleteRoute**](AthleteRoute.md) |  | [optional] 
**other_distance** | **float** |  | [optional] 
**other_activity_count** | **int** |  | [optional] 
**similarity** | **float** |  | [optional] 
**bounds** | **List[List[float]]** |  | [optional] 

## Example

```python
from intervals_icu_client.models.route_similarity import RouteSimilarity

# TODO update the JSON string below
json = "{}"
# create an instance of RouteSimilarity from a JSON string
route_similarity_instance = RouteSimilarity.from_json(json)
# print the JSON string representation of the object
print(RouteSimilarity.to_json())

# convert the object into a dict
route_similarity_dict = route_similarity_instance.to_dict()
# create an instance of RouteSimilarity from a dict
route_similarity_from_dict = RouteSimilarity.from_dict(route_similarity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


