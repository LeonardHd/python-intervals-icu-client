# Anomaly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_index** | **int** |  | [optional] 
**end_index** | **int** |  | [optional] 
**value** | **int** |  | [optional] 
**value_end** | **int** |  | [optional] 

## Example

```python
from intervals_icu_client.models.anomaly import Anomaly

# TODO update the JSON string below
json = "{}"
# create an instance of Anomaly from a JSON string
anomaly_instance = Anomaly.from_json(json)
# print the JSON string representation of the object
print(Anomaly.to_json())

# convert the object into a dict
anomaly_dict = anomaly_instance.to_dict()
# create an instance of Anomaly from a dict
anomaly_from_dict = Anomaly.from_dict(anomaly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


