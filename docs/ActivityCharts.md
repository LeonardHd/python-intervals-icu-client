# ActivityCharts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | [**List[Pos]**](Pos.md) |  | [optional] 
**power** | [**List[Pos]**](Pos.md) |  | [optional] 
**hr** | [**List[Pos]**](Pos.md) |  | [optional] 
**pace** | [**List[Pos]**](Pos.md) |  | [optional] 
**data** | [**List[Pos]**](Pos.md) |  | [optional] 

## Example

```python
from intervals_icu_client.models.activity_charts import ActivityCharts

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityCharts from a JSON string
activity_charts_instance = ActivityCharts.from_json(json)
# print the JSON string representation of the object
print(ActivityCharts.to_json())

# convert the object into a dict
activity_charts_dict = activity_charts_instance.to_dict()
# create an instance of ActivityCharts from a dict
activity_charts_from_dict = ActivityCharts.from_dict(activity_charts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


