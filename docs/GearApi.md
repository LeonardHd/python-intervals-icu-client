# intervals_icu_client.GearApi

All URIs are relative to *https://intervals.icu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calc_distance_etc**](GearApi.md#calc_distance_etc) | **GET** /api/v1/athlete/{id}/gear/{gearId}/calc | Recalculate gear stats
[**create_gear**](GearApi.md#create_gear) | **POST** /api/v1/athlete/{id}/gear | Create a new gear or component
[**create_reminder**](GearApi.md#create_reminder) | **POST** /api/v1/athlete/{id}/gear/{gearId}/reminder | Create a new reminder
[**delete_gear**](GearApi.md#delete_gear) | **DELETE** /api/v1/athlete/{id}/gear/{gearId} | Delete a gear or component
[**delete_reminder**](GearApi.md#delete_reminder) | **DELETE** /api/v1/athlete/{id}/gear/{gearId}/reminder/{reminderId} | Delete a reminder
[**list_gear**](GearApi.md#list_gear) | **GET** /api/v1/athlete/{id}/gear{ext} | List athlete gear (use .csv for CSV format)
[**replace_gear**](GearApi.md#replace_gear) | **POST** /api/v1/athlete/{id}/gear/{gearId}/replace | Retire a component and replace it with a copy with the same reminders etc.
[**update_gear**](GearApi.md#update_gear) | **PUT** /api/v1/athlete/{id}/gear/{gearId} | Update a gear or component
[**update_reminder**](GearApi.md#update_reminder) | **PUT** /api/v1/athlete/{id}/gear/{gearId}/reminder/{reminderId} | Update a reminder


# **calc_distance_etc**
> GearStats calc_distance_etc(id, gear_id)

Recalculate gear stats

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.gear_stats import GearStats
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
    api_instance = intervals_icu_client.GearApi(api_client)
    id = 'id_example' # str | 
    gear_id = 'gear_id_example' # str | 

    try:
        # Recalculate gear stats
        api_response = api_instance.calc_distance_etc(id, gear_id)
        print("The response of GearApi->calc_distance_etc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GearApi->calc_distance_etc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **gear_id** | **str**|  | 

### Return type

[**GearStats**](GearStats.md)

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

# **create_gear**
> Gear create_gear(id, gear)

Create a new gear or component

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.gear import Gear
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
    api_instance = intervals_icu_client.GearApi(api_client)
    id = 'id_example' # str | 
    gear = intervals_icu_client.Gear() # Gear | 

    try:
        # Create a new gear or component
        api_response = api_instance.create_gear(id, gear)
        print("The response of GearApi->create_gear:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GearApi->create_gear: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **gear** | [**Gear**](Gear.md)|  | 

### Return type

[**Gear**](Gear.md)

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

# **create_reminder**
> Gear create_reminder(id, gear_id, gear_reminder)

Create a new reminder

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.gear import Gear
from intervals_icu_client.models.gear_reminder import GearReminder
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
    api_instance = intervals_icu_client.GearApi(api_client)
    id = 'id_example' # str | 
    gear_id = 'gear_id_example' # str | 
    gear_reminder = intervals_icu_client.GearReminder() # GearReminder | 

    try:
        # Create a new reminder
        api_response = api_instance.create_reminder(id, gear_id, gear_reminder)
        print("The response of GearApi->create_reminder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GearApi->create_reminder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **gear_id** | **str**|  | 
 **gear_reminder** | [**GearReminder**](GearReminder.md)|  | 

### Return type

[**Gear**](Gear.md)

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

# **delete_gear**
> delete_gear(id, gear_id)

Delete a gear or component

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
    api_instance = intervals_icu_client.GearApi(api_client)
    id = 'id_example' # str | 
    gear_id = 'gear_id_example' # str | 

    try:
        # Delete a gear or component
        api_instance.delete_gear(id, gear_id)
    except Exception as e:
        print("Exception when calling GearApi->delete_gear: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **gear_id** | **str**|  | 

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

# **delete_reminder**
> Gear delete_reminder(id, gear_id, reminder_id)

Delete a reminder

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.gear import Gear
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
    api_instance = intervals_icu_client.GearApi(api_client)
    id = 'id_example' # str | 
    gear_id = 'gear_id_example' # str | 
    reminder_id = 56 # int | 

    try:
        # Delete a reminder
        api_response = api_instance.delete_reminder(id, gear_id, reminder_id)
        print("The response of GearApi->delete_reminder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GearApi->delete_reminder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **gear_id** | **str**|  | 
 **reminder_id** | **int**|  | 

### Return type

[**Gear**](Gear.md)

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

# **list_gear**
> List[Gear] list_gear(id, ext)

List athlete gear (use .csv for CSV format)

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.gear import Gear
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
    api_instance = intervals_icu_client.GearApi(api_client)
    id = 'id_example' # str | 
    ext = 'ext_example' # str | 

    try:
        # List athlete gear (use .csv for CSV format)
        api_response = api_instance.list_gear(id, ext)
        print("The response of GearApi->list_gear:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GearApi->list_gear: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ext** | **str**|  | 

### Return type

[**List[Gear]**](Gear.md)

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

# **replace_gear**
> List[Gear] replace_gear(id, gear_id, gear)

Retire a component and replace it with a copy with the same reminders etc.

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.gear import Gear
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
    api_instance = intervals_icu_client.GearApi(api_client)
    id = 'id_example' # str | 
    gear_id = 'gear_id_example' # str | 
    gear = intervals_icu_client.Gear() # Gear | 

    try:
        # Retire a component and replace it with a copy with the same reminders etc.
        api_response = api_instance.replace_gear(id, gear_id, gear)
        print("The response of GearApi->replace_gear:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GearApi->replace_gear: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **gear_id** | **str**|  | 
 **gear** | [**Gear**](Gear.md)|  | 

### Return type

[**List[Gear]**](Gear.md)

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

# **update_gear**
> Gear update_gear(id, gear_id, gear)

Update a gear or component

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.gear import Gear
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
    api_instance = intervals_icu_client.GearApi(api_client)
    id = 'id_example' # str | 
    gear_id = 'gear_id_example' # str | 
    gear = intervals_icu_client.Gear() # Gear | 

    try:
        # Update a gear or component
        api_response = api_instance.update_gear(id, gear_id, gear)
        print("The response of GearApi->update_gear:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GearApi->update_gear: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **gear_id** | **str**|  | 
 **gear** | [**Gear**](Gear.md)|  | 

### Return type

[**Gear**](Gear.md)

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

# **update_reminder**
> Gear update_reminder(id, gear_id, reminder_id, reset, snooze_days, gear_reminder)

Update a reminder

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.gear import Gear
from intervals_icu_client.models.gear_reminder import GearReminder
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
    api_instance = intervals_icu_client.GearApi(api_client)
    id = 'id_example' # str | 
    gear_id = 'gear_id_example' # str | 
    reminder_id = 56 # int | 
    reset = True # bool | 
    snooze_days = 56 # int | 
    gear_reminder = intervals_icu_client.GearReminder() # GearReminder | 

    try:
        # Update a reminder
        api_response = api_instance.update_reminder(id, gear_id, reminder_id, reset, snooze_days, gear_reminder)
        print("The response of GearApi->update_reminder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GearApi->update_reminder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **gear_id** | **str**|  | 
 **reminder_id** | **int**|  | 
 **reset** | **bool**|  | 
 **snooze_days** | **int**|  | 
 **gear_reminder** | [**GearReminder**](GearReminder.md)|  | 

### Return type

[**Gear**](Gear.md)

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

