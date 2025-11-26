# intervals_icu_client.CustomItemsApi

All URIs are relative to *https://intervals.icu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_item**](CustomItemsApi.md#create_custom_item) | **POST** /api/v1/athlete/{id}/custom-item | Create a custom item
[**delete_custom_item**](CustomItemsApi.md#delete_custom_item) | **DELETE** /api/v1/athlete/{id}/custom-item/{itemId} | Delete a custom item
[**get_custom_item**](CustomItemsApi.md#get_custom_item) | **GET** /api/v1/athlete/{id}/custom-item/{itemId} | Get a custom item
[**list_custom_items**](CustomItemsApi.md#list_custom_items) | **GET** /api/v1/athlete/{id}/custom-item | List custom items (charts, custom fields etc.)
[**update_custom_item**](CustomItemsApi.md#update_custom_item) | **PUT** /api/v1/athlete/{id}/custom-item/{itemId} | Update a custom item
[**update_custom_item_image**](CustomItemsApi.md#update_custom_item_image) | **POST** /api/v1/athlete/{id}/custom-item/{itemId}/image | Upload a new image for a custom item as multipart/form-data
[**update_custom_item_indexes**](CustomItemsApi.md#update_custom_item_indexes) | **PUT** /api/v1/athlete/{id}/custom-item-indexes | Re-order custom items


# **create_custom_item**
> NewCustomItem create_custom_item(id, custom_item)

Create a custom item

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.custom_item import CustomItem
from intervals_icu_client.models.new_custom_item import NewCustomItem
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
    api_instance = intervals_icu_client.CustomItemsApi(api_client)
    id = 'id_example' # str | 
    custom_item = intervals_icu_client.CustomItem() # CustomItem | 

    try:
        # Create a custom item
        api_response = api_instance.create_custom_item(id, custom_item)
        print("The response of CustomItemsApi->create_custom_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomItemsApi->create_custom_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **custom_item** | [**CustomItem**](CustomItem.md)|  | 

### Return type

[**NewCustomItem**](NewCustomItem.md)

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

# **delete_custom_item**
> delete_custom_item(id, item_id)

Delete a custom item

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
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
    api_instance = intervals_icu_client.CustomItemsApi(api_client)
    id = 'id_example' # str | 
    item_id = 56 # int | 

    try:
        # Delete a custom item
        api_instance.delete_custom_item(id, item_id)
    except Exception as e:
        print("Exception when calling CustomItemsApi->delete_custom_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **item_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_item**
> CustomItem get_custom_item(id, item_id)

Get a custom item

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.custom_item import CustomItem
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
    api_instance = intervals_icu_client.CustomItemsApi(api_client)
    id = 'id_example' # str | 
    item_id = 56 # int | 

    try:
        # Get a custom item
        api_response = api_instance.get_custom_item(id, item_id)
        print("The response of CustomItemsApi->get_custom_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomItemsApi->get_custom_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **item_id** | **int**|  | 

### Return type

[**CustomItem**](CustomItem.md)

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

# **list_custom_items**
> List[CustomItem] list_custom_items(id)

List custom items (charts, custom fields etc.)

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.custom_item import CustomItem
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
    api_instance = intervals_icu_client.CustomItemsApi(api_client)
    id = 'id_example' # str | 

    try:
        # List custom items (charts, custom fields etc.)
        api_response = api_instance.list_custom_items(id)
        print("The response of CustomItemsApi->list_custom_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomItemsApi->list_custom_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[CustomItem]**](CustomItem.md)

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

# **update_custom_item**
> CustomItem update_custom_item(id, item_id, custom_item)

Update a custom item

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.custom_item import CustomItem
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
    api_instance = intervals_icu_client.CustomItemsApi(api_client)
    id = 'id_example' # str | 
    item_id = 56 # int | 
    custom_item = intervals_icu_client.CustomItem() # CustomItem | 

    try:
        # Update a custom item
        api_response = api_instance.update_custom_item(id, item_id, custom_item)
        print("The response of CustomItemsApi->update_custom_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomItemsApi->update_custom_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **item_id** | **int**|  | 
 **custom_item** | [**CustomItem**](CustomItem.md)|  | 

### Return type

[**CustomItem**](CustomItem.md)

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

# **update_custom_item_image**
> CustomItem update_custom_item_image(id, item_id, upload_wellness_request=upload_wellness_request)

Upload a new image for a custom item as multipart/form-data

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.custom_item import CustomItem
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
    api_instance = intervals_icu_client.CustomItemsApi(api_client)
    id = 'id_example' # str | 
    item_id = 56 # int | 
    upload_wellness_request = intervals_icu_client.UploadWellnessRequest() # UploadWellnessRequest |  (optional)

    try:
        # Upload a new image for a custom item as multipart/form-data
        api_response = api_instance.update_custom_item_image(id, item_id, upload_wellness_request=upload_wellness_request)
        print("The response of CustomItemsApi->update_custom_item_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomItemsApi->update_custom_item_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **item_id** | **int**|  | 
 **upload_wellness_request** | [**UploadWellnessRequest**](UploadWellnessRequest.md)|  | [optional] 

### Return type

[**CustomItem**](CustomItem.md)

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

# **update_custom_item_indexes**
> update_custom_item_indexes(id, custom_item)

Re-order custom items

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.custom_item import CustomItem
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
    api_instance = intervals_icu_client.CustomItemsApi(api_client)
    id = 'id_example' # str | 
    custom_item = [intervals_icu_client.CustomItem()] # List[CustomItem] | 

    try:
        # Re-order custom items
        api_instance.update_custom_item_indexes(id, custom_item)
    except Exception as e:
        print("Exception when calling CustomItemsApi->update_custom_item_indexes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **custom_item** | [**List[CustomItem]**](CustomItem.md)|  | 

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

