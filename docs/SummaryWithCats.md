# SummaryWithCats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**time** | **int** |  | [optional] 
**moving_time** | **int** |  | [optional] 
**elapsed_time** | **int** |  | [optional] 
**calories** | **int** |  | [optional] 
**total_elevation_gain** | **float** |  | [optional] 
**training_load** | **int** |  | [optional] 
**srpe** | **int** |  | [optional] 
**distance** | **float** |  | [optional] 
**eftp** | **float** |  | [optional] 
**eftp_per_kg** | **float** |  | [optional] 
**var_date** | **str** |  | [optional] 
**athlete_id** | **str** |  | [optional] 
**athlete_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**fitness** | **float** |  | [optional] 
**fatigue** | **float** |  | [optional] 
**form** | **float** |  | [optional] 
**ramp_rate** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**time_in_zones** | **List[int]** |  | [optional] 
**time_in_zones_tot** | **int** |  | [optional] 
**by_category** | [**List[CategorySummary]**](CategorySummary.md) |  | [optional] 
**most_recent_wellness_id** | **str** |  | [optional] 

## Example

```python
from intervals_icu_client.models.summary_with_cats import SummaryWithCats

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryWithCats from a JSON string
summary_with_cats_instance = SummaryWithCats.from_json(json)
# print the JSON string representation of the object
print(SummaryWithCats.to_json())

# convert the object into a dict
summary_with_cats_dict = summary_with_cats_instance.to_dict()
# create an instance of SummaryWithCats from a dict
summary_with_cats_from_dict = SummaryWithCats.from_dict(summary_with_cats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


