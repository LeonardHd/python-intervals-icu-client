# ActivityMini


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**start_date_local** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from intervals_icu_client.models.activity_mini import ActivityMini

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityMini from a JSON string
activity_mini_instance = ActivityMini.from_json(json)
# print the JSON string representation of the object
print(ActivityMini.to_json())

# convert the object into a dict
activity_mini_dict = activity_mini_instance.to_dict()
# create an instance of ActivityMini from a dict
activity_mini_from_dict = ActivityMini.from_dict(activity_mini_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


