# IcuSegment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**start_index** | **int** |  | [optional] 
**end_index** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**segment_id** | **int** |  | [optional] 
**starred** | **bool** |  | [optional] 

## Example

```python
from intervals_icu_client.models.icu_segment import IcuSegment

# TODO update the JSON string below
json = "{}"
# create an instance of IcuSegment from a JSON string
icu_segment_instance = IcuSegment.from_json(json)
# print the JSON string representation of the object
print(IcuSegment.to_json())

# convert the object into a dict
icu_segment_dict = icu_segment_instance.to_dict()
# create an instance of IcuSegment from a dict
icu_segment_from_dict = IcuSegment.from_dict(icu_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


