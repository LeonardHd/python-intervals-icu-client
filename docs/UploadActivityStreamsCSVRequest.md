# UploadActivityStreamsCSVRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | Activity streams CSV file | 

## Example

```python
from intervals_icu_client.models.upload_activity_streams_csv_request import UploadActivityStreamsCSVRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadActivityStreamsCSVRequest from a JSON string
upload_activity_streams_csv_request_instance = UploadActivityStreamsCSVRequest.from_json(json)
# print the JSON string representation of the object
print(UploadActivityStreamsCSVRequest.to_json())

# convert the object into a dict
upload_activity_streams_csv_request_dict = upload_activity_streams_csv_request_instance.to_dict()
# create an instance of UploadActivityStreamsCSVRequest from a dict
upload_activity_streams_csv_request_from_dict = UploadActivityStreamsCSVRequest.from_dict(upload_activity_streams_csv_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


