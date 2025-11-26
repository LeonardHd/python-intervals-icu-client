# AthleteRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**athlete_id** | **str** |  | [optional] 
**route_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**rename_activities** | **bool** |  | [optional] 
**commute** | **bool** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**replaced_by_route_id** | **int** |  | [optional] 
**latlngs** | **List[List[float]]** |  | [optional] 

## Example

```python
from intervals_icu_client.models.athlete_route import AthleteRoute

# TODO update the JSON string below
json = "{}"
# create an instance of AthleteRoute from a JSON string
athlete_route_instance = AthleteRoute.from_json(json)
# print the JSON string representation of the object
print(AthleteRoute.to_json())

# convert the object into a dict
athlete_route_dict = athlete_route_instance.to_dict()
# create an instance of AthleteRoute from a dict
athlete_route_from_dict = AthleteRoute.from_dict(athlete_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


