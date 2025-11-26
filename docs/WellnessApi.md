# intervals_icu_client.WellnessApi

All URIs are relative to *https://intervals.icu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_record**](WellnessApi.md#get_record) | **GET** /api/v1/athlete/{id}/wellness/{date} | Get wellness record for date (local ISO-8601 day)
[**list_wellness_records**](WellnessApi.md#list_wellness_records) | **GET** /api/v1/athlete/{id}/wellness{ext} | List wellness records for date range (use .csv for CSV format)
[**update_wellness**](WellnessApi.md#update_wellness) | **PUT** /api/v1/athlete/{id}/wellness/{date} | Update the wellness record for the date (ISO-8601)
[**update_wellness1**](WellnessApi.md#update_wellness1) | **PUT** /api/v1/athlete/{id}/wellness | Update a wellness record, id is the day (ISO-8601)
[**update_wellness_bulk**](WellnessApi.md#update_wellness_bulk) | **PUT** /api/v1/athlete/{id}/wellness-bulk | Update an array of wellness records all for the same athlete
[**upload_wellness**](WellnessApi.md#upload_wellness) | **POST** /api/v1/athlete/{id}/wellness | Upload wellness records in CSV format as multipart/form-data


# **get_record**
> Wellness get_record(id, var_date)

Get wellness record for date (local ISO-8601 day)

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.wellness import Wellness
from intervals_icu_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://intervals.icu
# See configuration.py for a list of all supported configuration parameters.
configuration = intervals_icu_client.Configuration(
    host = "https://intervals.icu"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: APIKey
configuration = intervals_icu_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization: AccessToken
configuration = intervals_icu_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with intervals_icu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = intervals_icu_client.WellnessApi(api_client)
    id = 'id_example' # str | 
    var_date = 'var_date_example' # str | 

    try:
        # Get wellness record for date (local ISO-8601 day)
        api_response = api_instance.get_record(id, var_date)
        print("The response of WellnessApi->get_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WellnessApi->get_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **var_date** | **str**|  | 

### Return type

[**Wellness**](Wellness.md)

### Authorization

[APIKey](../README.md#APIKey), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_wellness_records**
> List[Wellness] list_wellness_records(id, ext, oldest=oldest, newest=newest, cols=cols, fields=fields)

List wellness records for date range (use .csv for CSV format)

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.wellness import Wellness
from intervals_icu_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://intervals.icu
# See configuration.py for a list of all supported configuration parameters.
configuration = intervals_icu_client.Configuration(
    host = "https://intervals.icu"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: APIKey
configuration = intervals_icu_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization: AccessToken
configuration = intervals_icu_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with intervals_icu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = intervals_icu_client.WellnessApi(api_client)
    id = 'id_example' # str | 
    ext = 'ext_example' # str | 
    oldest = 'oldest_example' # str | Local date of oldest record (ISO-8601) (optional)
    newest = 'newest_example' # str | Local date of newest record (ISO-8601), inclusive (optional)
    cols = ['cols_example'] # List[str] | Comma separated list of column names to include in CSV (default is all) (optional)
    fields = ['fields_example'] # List[str] | Comma separated list of field names to include in the returned objects (default is all), also excludes null values (optional)

    try:
        # List wellness records for date range (use .csv for CSV format)
        api_response = api_instance.list_wellness_records(id, ext, oldest=oldest, newest=newest, cols=cols, fields=fields)
        print("The response of WellnessApi->list_wellness_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WellnessApi->list_wellness_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ext** | **str**|  | 
 **oldest** | **str**| Local date of oldest record (ISO-8601) | [optional] 
 **newest** | **str**| Local date of newest record (ISO-8601), inclusive | [optional] 
 **cols** | [**List[str]**](str.md)| Comma separated list of column names to include in CSV (default is all) | [optional] 
 **fields** | [**List[str]**](str.md)| Comma separated list of field names to include in the returned objects (default is all), also excludes null values | [optional] 

### Return type

[**List[Wellness]**](Wellness.md)

### Authorization

[APIKey](../README.md#APIKey), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wellness**
> Wellness update_wellness(id, var_date, wellness)

Update the wellness record for the date (ISO-8601)

Only fields provided are changed

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.wellness import Wellness
from intervals_icu_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://intervals.icu
# See configuration.py for a list of all supported configuration parameters.
configuration = intervals_icu_client.Configuration(
    host = "https://intervals.icu"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: APIKey
configuration = intervals_icu_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization: AccessToken
configuration = intervals_icu_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with intervals_icu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = intervals_icu_client.WellnessApi(api_client)
    id = 'id_example' # str | 
    var_date = 'var_date_example' # str | 
    wellness = intervals_icu_client.Wellness() # Wellness | 

    try:
        # Update the wellness record for the date (ISO-8601)
        api_response = api_instance.update_wellness(id, var_date, wellness)
        print("The response of WellnessApi->update_wellness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WellnessApi->update_wellness: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **var_date** | **str**|  | 
 **wellness** | [**Wellness**](Wellness.md)|  | 

### Return type

[**Wellness**](Wellness.md)

### Authorization

[APIKey](../README.md#APIKey), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wellness1**
> Wellness update_wellness1(id, wellness)

Update a wellness record, id is the day (ISO-8601)

Only fields provided are changed

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.wellness import Wellness
from intervals_icu_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://intervals.icu
# See configuration.py for a list of all supported configuration parameters.
configuration = intervals_icu_client.Configuration(
    host = "https://intervals.icu"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: APIKey
configuration = intervals_icu_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization: AccessToken
configuration = intervals_icu_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with intervals_icu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = intervals_icu_client.WellnessApi(api_client)
    id = 'id_example' # str | 
    wellness = intervals_icu_client.Wellness() # Wellness | 

    try:
        # Update a wellness record, id is the day (ISO-8601)
        api_response = api_instance.update_wellness1(id, wellness)
        print("The response of WellnessApi->update_wellness1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WellnessApi->update_wellness1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wellness** | [**Wellness**](Wellness.md)|  | 

### Return type

[**Wellness**](Wellness.md)

### Authorization

[APIKey](../README.md#APIKey), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wellness_bulk**
> update_wellness_bulk(id, wellness)

Update an array of wellness records all for the same athlete

The id of each record is the day (ISO-8601). Only fields provided are changed

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.wellness import Wellness
from intervals_icu_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://intervals.icu
# See configuration.py for a list of all supported configuration parameters.
configuration = intervals_icu_client.Configuration(
    host = "https://intervals.icu"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: APIKey
configuration = intervals_icu_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization: AccessToken
configuration = intervals_icu_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with intervals_icu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = intervals_icu_client.WellnessApi(api_client)
    id = 'id_example' # str | 
    wellness = [intervals_icu_client.Wellness()] # List[Wellness] | 

    try:
        # Update an array of wellness records all for the same athlete
        api_instance.update_wellness_bulk(id, wellness)
    except Exception as e:
        print("Exception when calling WellnessApi->update_wellness_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wellness** | [**List[Wellness]**](Wellness.md)|  | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_wellness**
> object upload_wellness(id, ignore_missing_fields=ignore_missing_fields, upload_wellness_request=upload_wellness_request)

Upload wellness records in CSV format as multipart/form-data

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.upload_wellness_request import UploadWellnessRequest
from intervals_icu_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://intervals.icu
# See configuration.py for a list of all supported configuration parameters.
configuration = intervals_icu_client.Configuration(
    host = "https://intervals.icu"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: APIKey
configuration = intervals_icu_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization: AccessToken
configuration = intervals_icu_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with intervals_icu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = intervals_icu_client.WellnessApi(api_client)
    id = 'id_example' # str | 
    ignore_missing_fields = False # bool |  (optional) (default to False)
    upload_wellness_request = intervals_icu_client.UploadWellnessRequest() # UploadWellnessRequest |  (optional)

    try:
        # Upload wellness records in CSV format as multipart/form-data
        api_response = api_instance.upload_wellness(id, ignore_missing_fields=ignore_missing_fields, upload_wellness_request=upload_wellness_request)
        print("The response of WellnessApi->upload_wellness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WellnessApi->upload_wellness: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ignore_missing_fields** | **bool**|  | [optional] [default to False]
 **upload_wellness_request** | [**UploadWellnessRequest**](UploadWellnessRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[APIKey](../README.md#APIKey), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

