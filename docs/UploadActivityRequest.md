# UploadActivityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | Activity file | 

## Example

```python
from intervals_icu_client.models.upload_activity_request import UploadActivityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadActivityRequest from a JSON string
upload_activity_request_instance = UploadActivityRequest.from_json(json)
# print the JSON string representation of the object
print(UploadActivityRequest.to_json())

# convert the object into a dict
upload_activity_request_dict = upload_activity_request_instance.to_dict()
# create an instance of UploadActivityRequest from a dict
upload_activity_request_from_dict = UploadActivityRequest.from_dict(upload_activity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


