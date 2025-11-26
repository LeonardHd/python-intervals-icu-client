# intervals_icu_client.EventsApi

All URIs are relative to *https://intervals.icu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event**](EventsApi.md#create_event) | **POST** /api/v1/athlete/{id}/events | Create an event on the athlete&#39;s calendar
[**create_multiple_events**](EventsApi.md#create_multiple_events) | **POST** /api/v1/athlete/{id}/events/bulk | Create multiple events on the athlete&#39;s calendar
[**delete_event**](EventsApi.md#delete_event) | **DELETE** /api/v1/athlete/{id}/events/{eventId} | Delete an event from an athlete&#39;s calendar
[**delete_events**](EventsApi.md#delete_events) | **DELETE** /api/v1/athlete/{id}/events | Delete a range of events from the athlete&#39;s calendar
[**delete_events_bulk**](EventsApi.md#delete_events_bulk) | **PUT** /api/v1/athlete/{id}/events/bulk-delete | Delete events from an athlete&#39;s calendar by id or external_id
[**download_workout1**](EventsApi.md#download_workout1) | **GET** /api/v1/athlete/{id}/events/{eventId}/download{ext} | Download a planned workout in zwo, mrc, erg or fit format
[**download_workouts**](EventsApi.md#download_workouts) | **GET** /api/v1/athlete/{id}/workouts.zip | Download one or more workouts from the athlete&#39;s calendar in a zip file
[**duplicate_events**](EventsApi.md#duplicate_events) | **POST** /api/v1/athlete/{id}/duplicate-events | Duplicate one or more events on the athlete&#39;s calendar
[**list_events**](EventsApi.md#list_events) | **GET** /api/v1/athlete/{id}/events{format} | List events (planned workouts, notes etc.) on the athlete&#39;s calendar, add .csv for CSV output
[**list_fitness_model_events**](EventsApi.md#list_fitness_model_events) | **GET** /api/v1/athlete/{id}/fitness-model-events | List events that influence the athlete&#39;s fitness calculation in ascending date order
[**list_tags1**](EventsApi.md#list_tags1) | **GET** /api/v1/athlete/{id}/event-tags | List all tags that have been applied to events on the athlete&#39;s calendar
[**mark_event_as_done**](EventsApi.md#mark_event_as_done) | **POST** /api/v1/athlete/{id}/events/{eventId}/mark-done | Create a manual activity to match a planned workout
[**show_event**](EventsApi.md#show_event) | **GET** /api/v1/athlete/{id}/events/{eventId} | Get an event
[**update_event**](EventsApi.md#update_event) | **PUT** /api/v1/athlete/{id}/events/{eventId} | Update an event
[**update_events**](EventsApi.md#update_events) | **PUT** /api/v1/athlete/{id}/events | Update all events for a date range at once. Only hide_from_athlete and athlete_cannot_edit can be updated


# **create_event**
> Event create_event(id, upsert_on_uid, event_ex)

Create an event on the athlete's calendar

This endpoint accepts workouts in native Intervals.icu format ('description' field) as well as zwo, mrc, erg and fit files (use 'file_contents' or 'file_contents_base64')

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.event import Event
from intervals_icu_client.models.event_ex import EventEx
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
    api_instance = intervals_icu_client.EventsApi(api_client)
    id = 'id_example' # str | 
    upsert_on_uid = True # bool | Update event with matching uid instead of creating a new one
    event_ex = intervals_icu_client.EventEx() # EventEx | 

    try:
        # Create an event on the athlete's calendar
        api_response = api_instance.create_event(id, upsert_on_uid, event_ex)
        print("The response of EventsApi->create_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->create_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **upsert_on_uid** | **bool**| Update event with matching uid instead of creating a new one | 
 **event_ex** | [**EventEx**](EventEx.md)|  | 

### Return type

[**Event**](Event.md)

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

# **create_multiple_events**
> List[Event] create_multiple_events(id, upsert_on_uid, update_plan_applied, event_ex, upsert=upsert)

Create multiple events on the athlete's calendar

This endpoint accepts workouts in native Intervals.icu format ('description' field) as well as zwo, mrc, erg and fit files (use 'file_contents' or 'file_contents_base64')

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.event import Event
from intervals_icu_client.models.event_ex import EventEx
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
    api_instance = intervals_icu_client.EventsApi(api_client)
    id = 'id_example' # str | 
    upsert_on_uid = True # bool | Update events with matching uid instead of creating new ones, ignored if upsert=true. For Events with category=TARGET existing matching targets for the date and type are updated
    update_plan_applied = True # bool | Give all events created or updated the same new plan_applied date (now)
    event_ex = [intervals_icu_client.EventEx()] # List[EventEx] | 
    upsert = False # bool | Update events with matching external_id and created by the same OAuth application instead of creating new ones (optional) (default to False)

    try:
        # Create multiple events on the athlete's calendar
        api_response = api_instance.create_multiple_events(id, upsert_on_uid, update_plan_applied, event_ex, upsert=upsert)
        print("The response of EventsApi->create_multiple_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->create_multiple_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **upsert_on_uid** | **bool**| Update events with matching uid instead of creating new ones, ignored if upsert&#x3D;true. For Events with category&#x3D;TARGET existing matching targets for the date and type are updated | 
 **update_plan_applied** | **bool**| Give all events created or updated the same new plan_applied date (now) | 
 **event_ex** | [**List[EventEx]**](EventEx.md)|  | 
 **upsert** | **bool**| Update events with matching external_id and created by the same OAuth application instead of creating new ones | [optional] [default to False]

### Return type

[**List[Event]**](Event.md)

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

# **delete_event**
> Dict[str, object] delete_event(id, event_id, others=others, not_before=not_before)

Delete an event from an athlete's calendar

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
    api_instance = intervals_icu_client.EventsApi(api_client)
    id = 'id_example' # str | 
    event_id = 56 # int | 
    others = True # bool | If true then other events added at the same time are also deleted (optional)
    not_before = 'not_before_example' # str | Do not delete other events on the calendar before this local date (ISO-8601) (optional)

    try:
        # Delete an event from an athlete's calendar
        api_response = api_instance.delete_event(id, event_id, others=others, not_before=not_before)
        print("The response of EventsApi->delete_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->delete_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **event_id** | **int**|  | 
 **others** | **bool**| If true then other events added at the same time are also deleted | [optional] 
 **not_before** | **str**| Do not delete other events on the calendar before this local date (ISO-8601) | [optional] 

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

# **delete_events**
> delete_events(id, oldest, category, newest=newest, created_by_id=created_by_id)

Delete a range of events from the athlete's calendar

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
    api_instance = intervals_icu_client.EventsApi(api_client)
    id = 'id_example' # str | 
    oldest = 'oldest_example' # str | Local date (ISO-8601) of oldest event to delete
    category = ['category_example'] # List[str] | Comma separated list of event categories to delete (e.g. WORKOUT)
    newest = 'newest_example' # str | Local date (ISO-8601) of newest event to delete (inclusive, default is all future events) (optional)
    created_by_id = 'created_by_id_example' # str | If provided only events created by this athlete (created_by_id field) are deleted (optional)

    try:
        # Delete a range of events from the athlete's calendar
        api_instance.delete_events(id, oldest, category, newest=newest, created_by_id=created_by_id)
    except Exception as e:
        print("Exception when calling EventsApi->delete_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **oldest** | **str**| Local date (ISO-8601) of oldest event to delete | 
 **category** | [**List[str]**](str.md)| Comma separated list of event categories to delete (e.g. WORKOUT) | 
 **newest** | **str**| Local date (ISO-8601) of newest event to delete (inclusive, default is all future events) | [optional] 
 **created_by_id** | **str**| If provided only events created by this athlete (created_by_id field) are deleted | [optional] 

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

# **delete_events_bulk**
> DeleteEventsResponse delete_events_bulk(id, doomed_event)

Delete events from an athlete's calendar by id or external_id

Delete events by id or by external_id. If external_id is supplied then the event must have been created by the calling OAuth application. If both id and external_id are supplied then external_id is used. Events that do not exist are ignored.

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.delete_events_response import DeleteEventsResponse
from intervals_icu_client.models.doomed_event import DoomedEvent
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
    api_instance = intervals_icu_client.EventsApi(api_client)
    id = 'id_example' # str | 
    doomed_event = [intervals_icu_client.DoomedEvent()] # List[DoomedEvent] | 

    try:
        # Delete events from an athlete's calendar by id or external_id
        api_response = api_instance.delete_events_bulk(id, doomed_event)
        print("The response of EventsApi->delete_events_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->delete_events_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **doomed_event** | [**List[DoomedEvent]**](DoomedEvent.md)|  | 

### Return type

[**DeleteEventsResponse**](DeleteEventsResponse.md)

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

# **download_workout1**
> download_workout1(id, event_id, ext)

Download a planned workout in zwo, mrc, erg or fit format

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
    api_instance = intervals_icu_client.EventsApi(api_client)
    id = 'id_example' # str | 
    event_id = 56 # int | 
    ext = 'ext_example' # str | 

    try:
        # Download a planned workout in zwo, mrc, erg or fit format
        api_instance.download_workout1(id, event_id, ext)
    except Exception as e:
        print("Exception when calling EventsApi->download_workout1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **event_id** | **int**|  | 
 **ext** | **str**|  | 

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

# **download_workouts**
> download_workouts(id, ext, oldest, newest, power_range=power_range, hr_range=hr_range, pace_range=pace_range, locale=locale)

Download one or more workouts from the athlete's calendar in a zip file

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
    api_instance = intervals_icu_client.EventsApi(api_client)
    id = 'id_example' # str | 
    ext = 'ext_example' # str | Format: zwo, mrc, erg or fit
    oldest = 'oldest_example' # str | Local date (ISO-8601) of oldest workout
    newest = 'newest_example' # str | Local date (ISO-8601) of newest workout (inclusive)
    power_range = 3.4 # float |  (optional)
    hr_range = 3.4 # float |  (optional)
    pace_range = 3.4 # float |  (optional)
    locale = 'locale_example' # str |  (optional)

    try:
        # Download one or more workouts from the athlete's calendar in a zip file
        api_instance.download_workouts(id, ext, oldest, newest, power_range=power_range, hr_range=hr_range, pace_range=pace_range, locale=locale)
    except Exception as e:
        print("Exception when calling EventsApi->download_workouts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ext** | **str**| Format: zwo, mrc, erg or fit | 
 **oldest** | **str**| Local date (ISO-8601) of oldest workout | 
 **newest** | **str**| Local date (ISO-8601) of newest workout (inclusive) | 
 **power_range** | **float**|  | [optional] 
 **hr_range** | **float**|  | [optional] 
 **pace_range** | **float**|  | [optional] 
 **locale** | **str**|  | [optional] 

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

# **duplicate_events**
> List[Event] duplicate_events(id, duplicate_events_dto)

Duplicate one or more events on the athlete's calendar

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.duplicate_events_dto import DuplicateEventsDTO
from intervals_icu_client.models.event import Event
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
    api_instance = intervals_icu_client.EventsApi(api_client)
    id = 'id_example' # str | 
    duplicate_events_dto = intervals_icu_client.DuplicateEventsDTO() # DuplicateEventsDTO | 

    try:
        # Duplicate one or more events on the athlete's calendar
        api_response = api_instance.duplicate_events(id, duplicate_events_dto)
        print("The response of EventsApi->duplicate_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->duplicate_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **duplicate_events_dto** | [**DuplicateEventsDTO**](DuplicateEventsDTO.md)|  | 

### Return type

[**List[Event]**](Event.md)

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

# **list_events**
> List[Event] list_events(id, format, oldest=oldest, newest=newest, category=category, limit=limit, calendar_id=calendar_id, ext=ext, power_range=power_range, hr_range=hr_range, pace_range=pace_range, locale=locale, resolve=resolve)

List events (planned workouts, notes etc.) on the athlete's calendar, add .csv for CSV output

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.event import Event
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
    api_instance = intervals_icu_client.EventsApi(api_client)
    id = 'id_example' # str | 
    format = 'format_example' # str | 
    oldest = 'oldest_example' # str | Local date (ISO-8601) for oldest event to return, default is today in the athletes timezone (optional)
    newest = 'newest_example' # str | Local date (ISO-8601) for newest event to return (inclusive), default is oldest plus 6 days (optional)
    category = ['category_example'] # List[str] | Comma separated list of categories to filter for (e.g. WORKOUT,NOTES) (optional)
    limit = 56 # int | Max number of events to return (default is all events) (optional)
    calendar_id = 56 # int |  (optional)
    ext = 'ext_example' # str | Convert workouts to this format (zwo, mrc, erg or fit) and add workout_filename and workout_file_base64 to workout object (optional)
    power_range = 3.4 # float | Percentage used to convert fixed power targets into a range for outdoor workouts only (default is 2.5 or whatever is configured in the Garmin box in /settings) (optional)
    hr_range = 3.4 # float | Percentage used to convert fixed HR targets into a range (default is 1.5 or whatever is configured in the Garmin box in /settings) (optional)
    pace_range = 3.4 # float | Percentage used to convert fixed pace targets into a range (default is 2.5 or whatever is configured in the Garmin box in /settings) (optional)
    locale = 'locale_example' # str | Locale (en, es, de etc.) to use for workouts with steps in multiple languages (optional)
    resolve = False # bool | Resolve power, heart rate and pace targets to watts, bpm and m/s respectively (optional) (default to False)

    try:
        # List events (planned workouts, notes etc.) on the athlete's calendar, add .csv for CSV output
        api_response = api_instance.list_events(id, format, oldest=oldest, newest=newest, category=category, limit=limit, calendar_id=calendar_id, ext=ext, power_range=power_range, hr_range=hr_range, pace_range=pace_range, locale=locale, resolve=resolve)
        print("The response of EventsApi->list_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->list_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **format** | **str**|  | 
 **oldest** | **str**| Local date (ISO-8601) for oldest event to return, default is today in the athletes timezone | [optional] 
 **newest** | **str**| Local date (ISO-8601) for newest event to return (inclusive), default is oldest plus 6 days | [optional] 
 **category** | [**List[str]**](str.md)| Comma separated list of categories to filter for (e.g. WORKOUT,NOTES) | [optional] 
 **limit** | **int**| Max number of events to return (default is all events) | [optional] 
 **calendar_id** | **int**|  | [optional] 
 **ext** | **str**| Convert workouts to this format (zwo, mrc, erg or fit) and add workout_filename and workout_file_base64 to workout object | [optional] 
 **power_range** | **float**| Percentage used to convert fixed power targets into a range for outdoor workouts only (default is 2.5 or whatever is configured in the Garmin box in /settings) | [optional] 
 **hr_range** | **float**| Percentage used to convert fixed HR targets into a range (default is 1.5 or whatever is configured in the Garmin box in /settings) | [optional] 
 **pace_range** | **float**| Percentage used to convert fixed pace targets into a range (default is 2.5 or whatever is configured in the Garmin box in /settings) | [optional] 
 **locale** | **str**| Locale (en, es, de etc.) to use for workouts with steps in multiple languages | [optional] 
 **resolve** | **bool**| Resolve power, heart rate and pace targets to watts, bpm and m/s respectively | [optional] [default to False]

### Return type

[**List[Event]**](Event.md)

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

# **list_fitness_model_events**
> List[Event] list_fitness_model_events(id)

List events that influence the athlete's fitness calculation in ascending date order

These have category FITNESS_DAYS (days for fitness and fatigue), SET_FITNESS (set starting fitness and fatigue) and SET_EFTP (set eFTP)

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.event import Event
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
    api_instance = intervals_icu_client.EventsApi(api_client)
    id = 'id_example' # str | 

    try:
        # List events that influence the athlete's fitness calculation in ascending date order
        api_response = api_instance.list_fitness_model_events(id)
        print("The response of EventsApi->list_fitness_model_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->list_fitness_model_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[Event]**](Event.md)

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

# **list_tags1**
> List[str] list_tags1(id)

List all tags that have been applied to events on the athlete's calendar

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
    api_instance = intervals_icu_client.EventsApi(api_client)
    id = 'id_example' # str | 

    try:
        # List all tags that have been applied to events on the athlete's calendar
        api_response = api_instance.list_tags1(id)
        print("The response of EventsApi->list_tags1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->list_tags1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**List[str]**

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

# **mark_event_as_done**
> Activity mark_event_as_done(id, event_id)

Create a manual activity to match a planned workout

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.activity import Activity
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
    api_instance = intervals_icu_client.EventsApi(api_client)
    id = 'id_example' # str | 
    event_id = 56 # int | 

    try:
        # Create a manual activity to match a planned workout
        api_response = api_instance.mark_event_as_done(id, event_id)
        print("The response of EventsApi->mark_event_as_done:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->mark_event_as_done: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **event_id** | **int**|  | 

### Return type

[**Activity**](Activity.md)

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

# **show_event**
> Event show_event(id, event_id)

Get an event

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.event import Event
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
    api_instance = intervals_icu_client.EventsApi(api_client)
    id = 'id_example' # str | 
    event_id = 56 # int | 

    try:
        # Get an event
        api_response = api_instance.show_event(id, event_id)
        print("The response of EventsApi->show_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->show_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **event_id** | **int**|  | 

### Return type

[**Event**](Event.md)

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

# **update_event**
> Event update_event(id, event_id, event_ex)

Update an event

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.event import Event
from intervals_icu_client.models.event_ex import EventEx
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
    api_instance = intervals_icu_client.EventsApi(api_client)
    id = 'id_example' # str | 
    event_id = 56 # int | 
    event_ex = intervals_icu_client.EventEx() # EventEx | 

    try:
        # Update an event
        api_response = api_instance.update_event(id, event_id, event_ex)
        print("The response of EventsApi->update_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->update_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **event_id** | **int**|  | 
 **event_ex** | [**EventEx**](EventEx.md)|  | 

### Return type

[**Event**](Event.md)

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

# **update_events**
> List[Event] update_events(id, oldest, newest, event)

Update all events for a date range at once. Only hide_from_athlete and athlete_cannot_edit can be updated

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.event import Event
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
    api_instance = intervals_icu_client.EventsApi(api_client)
    id = 'id_example' # str | 
    oldest = 'oldest_example' # str | Local date (ISO-8601) of oldest event to update
    newest = 'newest_example' # str | Local date (ISO-8601) of newest event to update (inclusive)
    event = intervals_icu_client.Event() # Event | 

    try:
        # Update all events for a date range at once. Only hide_from_athlete and athlete_cannot_edit can be updated
        api_response = api_instance.update_events(id, oldest, newest, event)
        print("The response of EventsApi->update_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->update_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **oldest** | **str**| Local date (ISO-8601) of oldest event to update | 
 **newest** | **str**| Local date (ISO-8601) of newest event to update (inclusive) | 
 **event** | [**Event**](Event.md)|  | 

### Return type

[**List[Event]**](Event.md)

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

