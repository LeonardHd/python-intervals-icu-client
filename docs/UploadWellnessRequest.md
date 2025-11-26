# UploadWellnessRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** |  | 

## Example

```python
from intervals_icu_client.models.upload_wellness_request import UploadWellnessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadWellnessRequest from a JSON string
upload_wellness_request_instance = UploadWellnessRequest.from_json(json)
# print the JSON string representation of the object
print(UploadWellnessRequest.to_json())

# convert the object into a dict
upload_wellness_request_dict = upload_wellness_request_instance.to_dict()
# create an instance of UploadWellnessRequest from a dict
upload_wellness_request_from_dict = UploadWellnessRequest.from_dict(upload_wellness_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


