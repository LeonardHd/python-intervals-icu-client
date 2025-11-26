# intervals_icu_client.SharedEventsApi

All URIs are relative to *https://intervals.icu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shared_event**](SharedEventsApi.md#create_shared_event) | **POST** /api/v1/shared-event | Create a shared event (e.g. race)
[**delete_shared_event**](SharedEventsApi.md#delete_shared_event) | **DELETE** /api/v1/shared-event/{id} | Delete a shared event (e.g. race)
[**get_shared_event**](SharedEventsApi.md#get_shared_event) | **GET** /api/v1/shared-event/{id} | Get a shared event (e.g. race)
[**update_shared_event**](SharedEventsApi.md#update_shared_event) | **PUT** /api/v1/shared-event/{id} | Update a shared event (e.g. race)


# **create_shared_event**
> SharedEvent create_shared_event(shared_event, link_to_event_id=link_to_event_id)

Create a shared event (e.g. race)

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.shared_event import SharedEvent
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
    api_instance = intervals_icu_client.SharedEventsApi(api_client)
    shared_event = intervals_icu_client.SharedEvent() # SharedEvent | 
    link_to_event_id = 56 # int |  (optional)

    try:
        # Create a shared event (e.g. race)
        api_response = api_instance.create_shared_event(shared_event, link_to_event_id=link_to_event_id)
        print("The response of SharedEventsApi->create_shared_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharedEventsApi->create_shared_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_event** | [**SharedEvent**](SharedEvent.md)|  | 
 **link_to_event_id** | **int**|  | [optional] 

### Return type

[**SharedEvent**](SharedEvent.md)

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

# **delete_shared_event**
> delete_shared_event(id)

Delete a shared event (e.g. race)

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
    api_instance = intervals_icu_client.SharedEventsApi(api_client)
    id = 56 # int | 

    try:
        # Delete a shared event (e.g. race)
        api_instance.delete_shared_event(id)
    except Exception as e:
        print("Exception when calling SharedEventsApi->delete_shared_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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

# **get_shared_event**
> SharedEvent get_shared_event(id)

Get a shared event (e.g. race)

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.shared_event import SharedEvent
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
    api_instance = intervals_icu_client.SharedEventsApi(api_client)
    id = 56 # int | 

    try:
        # Get a shared event (e.g. race)
        api_response = api_instance.get_shared_event(id)
        print("The response of SharedEventsApi->get_shared_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharedEventsApi->get_shared_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SharedEvent**](SharedEvent.md)

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

# **update_shared_event**
> SharedEvent update_shared_event(id, shared_event)

Update a shared event (e.g. race)

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.shared_event import SharedEvent
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
    api_instance = intervals_icu_client.SharedEventsApi(api_client)
    id = 56 # int | 
    shared_event = intervals_icu_client.SharedEvent() # SharedEvent | 

    try:
        # Update a shared event (e.g. race)
        api_response = api_instance.update_shared_event(id, shared_event)
        print("The response of SharedEventsApi->update_shared_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharedEventsApi->update_shared_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **shared_event** | [**SharedEvent**](SharedEvent.md)|  | 

### Return type

[**SharedEvent**](SharedEvent.md)

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

