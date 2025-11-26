# IntervalsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**analyzed** | **datetime** |  | [optional] 
**icu_intervals** | [**List[Interval]**](Interval.md) |  | [optional] 
**icu_groups** | [**List[IntervalGroup]**](IntervalGroup.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.intervals_dto import IntervalsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IntervalsDTO from a JSON string
intervals_dto_instance = IntervalsDTO.from_json(json)
# print the JSON string representation of the object
print(IntervalsDTO.to_json())

# convert the object into a dict
intervals_dto_dict = intervals_dto_instance.to_dict()
# create an instance of IntervalsDTO from a dict
intervals_dto_from_dict = IntervalsDTO.from_dict(intervals_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


