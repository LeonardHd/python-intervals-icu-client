# intervals_icu_client.SportsApi

All URIs are relative to *https://intervals.icu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_to_activities**](SportsApi.md#apply_to_activities) | **PUT** /api/v1/athlete/{athleteId}/sport-settings/{id}/apply | Apply sport settings to matching activities (updates zones), done asynchronously
[**create_settings**](SportsApi.md#create_settings) | **POST** /api/v1/athlete/{athleteId}/sport-settings | Create settings for a sport with default values
[**delete_settings**](SportsApi.md#delete_settings) | **DELETE** /api/v1/athlete/{athleteId}/sport-settings/{id} | Delete sport settings
[**get_settings1**](SportsApi.md#get_settings1) | **GET** /api/v1/athlete/{athleteId}/sport-settings/{id} | Get sport settings by id or activity type e.g. Run, Ride etc.
[**list_matching_activities**](SportsApi.md#list_matching_activities) | **GET** /api/v1/athlete/{athleteId}/sport-settings/{id}/matching-activities | List activities matching the settings
[**list_pace_distances**](SportsApi.md#list_pace_distances) | **GET** /api/v1/pace_distances | List pace curve distances
[**list_pace_distances_for_sport**](SportsApi.md#list_pace_distances_for_sport) | **GET** /api/v1/athlete/{athleteId}/sport-settings/{id}/pace_distances | List pace curve distances and best effort defaults for the sport
[**list_settings**](SportsApi.md#list_settings) | **GET** /api/v1/athlete/{athleteId}/sport-settings | List sport settings for the athlete
[**update_settings**](SportsApi.md#update_settings) | **PUT** /api/v1/athlete/{athleteId}/sport-settings/{id} | Update sport settings by id or activity type e.g. Run, Ride etc.
[**update_settings_multi**](SportsApi.md#update_settings_multi) | **PUT** /api/v1/athlete/{athleteId}/sport-settings | Update multiple sport settings


# **apply_to_activities**
> object apply_to_activities(athlete_id, id)

Apply sport settings to matching activities (updates zones), done asynchronously

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
    api_instance = intervals_icu_client.SportsApi(api_client)
    athlete_id = 'athlete_id_example' # str | 
    id = 'id_example' # str | 

    try:
        # Apply sport settings to matching activities (updates zones), done asynchronously
        api_response = api_instance.apply_to_activities(athlete_id, id)
        print("The response of SportsApi->apply_to_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SportsApi->apply_to_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **athlete_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

**object**

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

# **create_settings**
> SportSettings create_settings(athlete_id, sport_settings)

Create settings for a sport with default values

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.sport_settings import SportSettings
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
    api_instance = intervals_icu_client.SportsApi(api_client)
    athlete_id = 'athlete_id_example' # str | 
    sport_settings = intervals_icu_client.SportSettings() # SportSettings | 

    try:
        # Create settings for a sport with default values
        api_response = api_instance.create_settings(athlete_id, sport_settings)
        print("The response of SportsApi->create_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SportsApi->create_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **athlete_id** | **str**|  | 
 **sport_settings** | [**SportSettings**](SportSettings.md)|  | 

### Return type

[**SportSettings**](SportSettings.md)

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

# **delete_settings**
> object delete_settings(athlete_id, id)

Delete sport settings

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
    api_instance = intervals_icu_client.SportsApi(api_client)
    athlete_id = 'athlete_id_example' # str | 
    id = 56 # int | 

    try:
        # Delete sport settings
        api_response = api_instance.delete_settings(athlete_id, id)
        print("The response of SportsApi->delete_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SportsApi->delete_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **athlete_id** | **str**|  | 
 **id** | **int**|  | 

### Return type

**object**

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

# **get_settings1**
> SportSettings get_settings1(athlete_id, id)

Get sport settings by id or activity type e.g. Run, Ride etc.

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.sport_settings import SportSettings
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
    api_instance = intervals_icu_client.SportsApi(api_client)
    athlete_id = 'athlete_id_example' # str | 
    id = 'id_example' # str | 

    try:
        # Get sport settings by id or activity type e.g. Run, Ride etc.
        api_response = api_instance.get_settings1(athlete_id, id)
        print("The response of SportsApi->get_settings1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SportsApi->get_settings1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **athlete_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**SportSettings**](SportSettings.md)

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

# **list_matching_activities**
> List[ActivityMini] list_matching_activities(athlete_id, id)

List activities matching the settings

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.activity_mini import ActivityMini
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
    api_instance = intervals_icu_client.SportsApi(api_client)
    athlete_id = 'athlete_id_example' # str | 
    id = 'id_example' # str | 

    try:
        # List activities matching the settings
        api_response = api_instance.list_matching_activities(athlete_id, id)
        print("The response of SportsApi->list_matching_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SportsApi->list_matching_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **athlete_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**List[ActivityMini]**](ActivityMini.md)

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

# **list_pace_distances**
> PaceDistancesDTO list_pace_distances()

List pace curve distances

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.pace_distances_dto import PaceDistancesDTO
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
    api_instance = intervals_icu_client.SportsApi(api_client)

    try:
        # List pace curve distances
        api_response = api_instance.list_pace_distances()
        print("The response of SportsApi->list_pace_distances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SportsApi->list_pace_distances: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PaceDistancesDTO**](PaceDistancesDTO.md)

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

# **list_pace_distances_for_sport**
> PaceDistancesDTO list_pace_distances_for_sport(athlete_id, id)

List pace curve distances and best effort defaults for the sport

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.pace_distances_dto import PaceDistancesDTO
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
    api_instance = intervals_icu_client.SportsApi(api_client)
    athlete_id = 'athlete_id_example' # str | 
    id = 'id_example' # str | 

    try:
        # List pace curve distances and best effort defaults for the sport
        api_response = api_instance.list_pace_distances_for_sport(athlete_id, id)
        print("The response of SportsApi->list_pace_distances_for_sport:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SportsApi->list_pace_distances_for_sport: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **athlete_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**PaceDistancesDTO**](PaceDistancesDTO.md)

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

# **list_settings**
> List[SportSettings] list_settings(athlete_id)

List sport settings for the athlete

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.sport_settings import SportSettings
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
    api_instance = intervals_icu_client.SportsApi(api_client)
    athlete_id = 'athlete_id_example' # str | 

    try:
        # List sport settings for the athlete
        api_response = api_instance.list_settings(athlete_id)
        print("The response of SportsApi->list_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SportsApi->list_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **athlete_id** | **str**|  | 

### Return type

[**List[SportSettings]**](SportSettings.md)

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

# **update_settings**
> SportSettings update_settings(athlete_id, id, recalc_hr_zones, sport_settings)

Update sport settings by id or activity type e.g. Run, Ride etc.

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.sport_settings import SportSettings
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
    api_instance = intervals_icu_client.SportsApi(api_client)
    athlete_id = 'athlete_id_example' # str | 
    id = 'id_example' # str | 
    recalc_hr_zones = True # bool | 
    sport_settings = intervals_icu_client.SportSettings() # SportSettings | 

    try:
        # Update sport settings by id or activity type e.g. Run, Ride etc.
        api_response = api_instance.update_settings(athlete_id, id, recalc_hr_zones, sport_settings)
        print("The response of SportsApi->update_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SportsApi->update_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **athlete_id** | **str**|  | 
 **id** | **str**|  | 
 **recalc_hr_zones** | **bool**|  | 
 **sport_settings** | [**SportSettings**](SportSettings.md)|  | 

### Return type

[**SportSettings**](SportSettings.md)

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

# **update_settings_multi**
> List[SportSettings] update_settings_multi(athlete_id, recalc_hr_zones, sport_settings)

Update multiple sport settings

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.sport_settings import SportSettings
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
    api_instance = intervals_icu_client.SportsApi(api_client)
    athlete_id = 'athlete_id_example' # str | 
    recalc_hr_zones = True # bool | 
    sport_settings = [intervals_icu_client.SportSettings()] # List[SportSettings] | 

    try:
        # Update multiple sport settings
        api_response = api_instance.update_settings_multi(athlete_id, recalc_hr_zones, sport_settings)
        print("The response of SportsApi->update_settings_multi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SportsApi->update_settings_multi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **athlete_id** | **str**|  | 
 **recalc_hr_zones** | **bool**|  | 
 **sport_settings** | [**List[SportSettings]**](SportSettings.md)|  | 

### Return type

[**List[SportSettings]**](SportSettings.md)

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

