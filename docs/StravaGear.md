# StravaGear


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**distance** | **float** |  | [optional] 
**primary** | **bool** |  | [optional] 

## Example

```python
from intervals_icu_client.models.strava_gear import StravaGear

# TODO update the JSON string below
json = "{}"
# create an instance of StravaGear from a JSON string
strava_gear_instance = StravaGear.from_json(json)
# print the JSON string representation of the object
print(StravaGear.to_json())

# convert the object into a dict
strava_gear_dict = strava_gear_instance.to_dict()
# create an instance of StravaGear from a dict
strava_gear_from_dict = StravaGear.from_dict(strava_gear_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


