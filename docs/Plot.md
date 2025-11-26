# Plot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_bpm** | **int** |  | [optional] 
**min_bpm** | **int** |  | [optional] 
**secs** | **List[int]** |  | [optional] 
**cumulative_secs** | **List[int]** |  | [optional] 

## Example

```python
from intervals_icu_client.models.plot import Plot

# TODO update the JSON string below
json = "{}"
# create an instance of Plot from a JSON string
plot_instance = Plot.from_json(json)
# print the JSON string representation of the object
print(Plot.to_json())

# convert the object into a dict
plot_dict = plot_instance.to_dict()
# create an instance of Plot from a dict
plot_from_dict = Plot.from_dict(plot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


