# ActivityStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**data2** | **object** |  | [optional] 
**value_type_is_array** | **bool** |  | [optional] 
**anomalies** | [**List[Anomaly]**](Anomaly.md) |  | [optional] 
**custom** | **bool** |  | [optional] 

## Example

```python
from intervals_icu_client.models.activity_stream import ActivityStream

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityStream from a JSON string
activity_stream_instance = ActivityStream.from_json(json)
# print the JSON string representation of the object
print(ActivityStream.to_json())

# convert the object into a dict
activity_stream_dict = activity_stream_instance.to_dict()
# create an instance of ActivityStream from a dict
activity_stream_from_dict = ActivityStream.from_dict(activity_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


