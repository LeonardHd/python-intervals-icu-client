# AthleteProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**athlete** | [**AthleteSearchResult**](AthleteSearchResult.md) |  | [optional] 
**shared_folders** | [**List[Folder]**](Folder.md) |  | [optional] 
**custom_items** | [**List[CustomItem]**](CustomItem.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.athlete_profile import AthleteProfile

# TODO update the JSON string below
json = "{}"
# create an instance of AthleteProfile from a JSON string
athlete_profile_instance = AthleteProfile.from_json(json)
# print the JSON string representation of the object
print(AthleteProfile.to_json())

# convert the object into a dict
athlete_profile_dict = athlete_profile_instance.to_dict()
# create an instance of AthleteProfile from a dict
athlete_profile_from_dict = AthleteProfile.from_dict(athlete_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


