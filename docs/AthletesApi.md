# intervals_icu_client.AthletesApi

All URIs are relative to *https://intervals.icu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_athlete**](AthletesApi.md#get_athlete) | **GET** /api/v1/athlete/{id} | Get the athlete with sportSettings and custom_items
[**get_athlete_profile**](AthletesApi.md#get_athlete_profile) | **GET** /api/v1/athlete/{id}/profile | Get athlete profile info
[**get_athlete_summary**](AthletesApi.md#get_athlete_summary) | **GET** /api/v1/athlete/{id}/athlete-summary{ext} | Summary information for followed athletes
[**get_athlete_training_plan**](AthletesApi.md#get_athlete_training_plan) | **GET** /api/v1/athlete/{id}/training-plan | Get the athlete&#39;s training plan
[**get_settings**](AthletesApi.md#get_settings) | **GET** /api/v1/athlete/{id}/settings/{deviceClass} | Get the athlete&#39;s settings for phone, tablet or desktop
[**update_athlete**](AthletesApi.md#update_athlete) | **PUT** /api/v1/athlete/{id} | Update an athlete
[**update_athlete_plan**](AthletesApi.md#update_athlete_plan) | **PUT** /api/v1/athlete/{id}/training-plan | Change the athlete&#39;s training plan
[**update_athlete_plans**](AthletesApi.md#update_athlete_plans) | **PUT** /api/v1/athlete-plans | Change training plans for a list of athletes


# **get_athlete**
> WithSportSettings get_athlete(id)

Get the athlete with sportSettings and custom_items

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.with_sport_settings import WithSportSettings
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
    api_instance = intervals_icu_client.AthletesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get the athlete with sportSettings and custom_items
        api_response = api_instance.get_athlete(id)
        print("The response of AthletesApi->get_athlete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AthletesApi->get_athlete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WithSportSettings**](WithSportSettings.md)

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

# **get_athlete_profile**
> AthleteProfile get_athlete_profile(id)

Get athlete profile info

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.athlete_profile import AthleteProfile
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
    api_instance = intervals_icu_client.AthletesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get athlete profile info
        api_response = api_instance.get_athlete_profile(id)
        print("The response of AthletesApi->get_athlete_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AthletesApi->get_athlete_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AthleteProfile**](AthleteProfile.md)

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

# **get_athlete_summary**
> List[SummaryWithCats] get_athlete_summary(id, ext, start=start, end=end, tags=tags)

Summary information for followed athletes

Note that when this endpoint is called with a bearer token then only the athlete the token is for is returned

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.summary_with_cats import SummaryWithCats
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
    api_instance = intervals_icu_client.AthletesApi(api_client)
    id = 'id_example' # str | 
    ext = 'ext_example' # str | 
    start = 'start_example' # str | Local date and optional time (ISO-8601) for oldest data to return, default is 6 days ago (optional)
    end = 'end_example' # str | Local date and optional time (ISO-8601) for newest data to return, default is today (optional)
    tags = ['tags_example'] # List[str] | Optional list of athlete tags, only athletes with one of these tags are returned (optional)

    try:
        # Summary information for followed athletes
        api_response = api_instance.get_athlete_summary(id, ext, start=start, end=end, tags=tags)
        print("The response of AthletesApi->get_athlete_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AthletesApi->get_athlete_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ext** | **str**|  | 
 **start** | **str**| Local date and optional time (ISO-8601) for oldest data to return, default is 6 days ago | [optional] 
 **end** | **str**| Local date and optional time (ISO-8601) for newest data to return, default is today | [optional] 
 **tags** | [**List[str]**](str.md)| Optional list of athlete tags, only athletes with one of these tags are returned | [optional] 

### Return type

[**List[SummaryWithCats]**](SummaryWithCats.md)

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

# **get_athlete_training_plan**
> AthleteTrainingPlan get_athlete_training_plan(id)

Get the athlete's training plan

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.athlete_training_plan import AthleteTrainingPlan
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
    api_instance = intervals_icu_client.AthletesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get the athlete's training plan
        api_response = api_instance.get_athlete_training_plan(id)
        print("The response of AthletesApi->get_athlete_training_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AthletesApi->get_athlete_training_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AthleteTrainingPlan**](AthleteTrainingPlan.md)

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

# **get_settings**
> Dict[str, object] get_settings(id, device_class)

Get the athlete's settings for phone, tablet or desktop

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
    api_instance = intervals_icu_client.AthletesApi(api_client)
    id = 'id_example' # str | 
    device_class = 'device_class_example' # str | 

    try:
        # Get the athlete's settings for phone, tablet or desktop
        api_response = api_instance.get_settings(id, device_class)
        print("The response of AthletesApi->get_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AthletesApi->get_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **device_class** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **update_athlete**
> Athlete update_athlete(id, athlete_update_dto)

Update an athlete

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.athlete import Athlete
from intervals_icu_client.models.athlete_update_dto import AthleteUpdateDTO
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
    api_instance = intervals_icu_client.AthletesApi(api_client)
    id = 'id_example' # str | 
    athlete_update_dto = intervals_icu_client.AthleteUpdateDTO() # AthleteUpdateDTO | 

    try:
        # Update an athlete
        api_response = api_instance.update_athlete(id, athlete_update_dto)
        print("The response of AthletesApi->update_athlete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AthletesApi->update_athlete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **athlete_update_dto** | [**AthleteUpdateDTO**](AthleteUpdateDTO.md)|  | 

### Return type

[**Athlete**](Athlete.md)

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

# **update_athlete_plan**
> AthleteTrainingPlan update_athlete_plan(id, athlete_training_plan_update)

Change the athlete's training plan

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.athlete_training_plan import AthleteTrainingPlan
from intervals_icu_client.models.athlete_training_plan_update import AthleteTrainingPlanUpdate
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
    api_instance = intervals_icu_client.AthletesApi(api_client)
    id = 'id_example' # str | 
    athlete_training_plan_update = intervals_icu_client.AthleteTrainingPlanUpdate() # AthleteTrainingPlanUpdate | 

    try:
        # Change the athlete's training plan
        api_response = api_instance.update_athlete_plan(id, athlete_training_plan_update)
        print("The response of AthletesApi->update_athlete_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AthletesApi->update_athlete_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **athlete_training_plan_update** | [**AthleteTrainingPlanUpdate**](AthleteTrainingPlanUpdate.md)|  | 

### Return type

[**AthleteTrainingPlan**](AthleteTrainingPlan.md)

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

# **update_athlete_plans**
> object update_athlete_plans(athlete_training_plan_update)

Change training plans for a list of athletes

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.athlete_training_plan_update import AthleteTrainingPlanUpdate
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
    api_instance = intervals_icu_client.AthletesApi(api_client)
    athlete_training_plan_update = [intervals_icu_client.AthleteTrainingPlanUpdate()] # List[AthleteTrainingPlanUpdate] | 

    try:
        # Change training plans for a list of athletes
        api_response = api_instance.update_athlete_plans(athlete_training_plan_update)
        print("The response of AthletesApi->update_athlete_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AthletesApi->update_athlete_plans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **athlete_training_plan_update** | [**List[AthleteTrainingPlanUpdate]**](AthleteTrainingPlanUpdate.md)|  | 

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

