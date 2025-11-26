# intervals_icu_client.ActivitiesApi

All URIs are relative to *https://intervals.icu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_manual_activity**](ActivitiesApi.md#create_manual_activity) | **POST** /api/v1/athlete/{id}/activities/manual | Create a manual activity
[**delete_activity**](ActivitiesApi.md#delete_activity) | **DELETE** /api/v1/activity/{id} | Delete an activity
[**delete_intervals**](ActivitiesApi.md#delete_intervals) | **PUT** /api/v1/activity/{id}/delete-intervals | Delete intervals
[**download_activities_as_csv**](ActivitiesApi.md#download_activities_as_csv) | **GET** /api/v1/athlete/{id}/activities.csv | Download activities as CSV
[**download_activity_file**](ActivitiesApi.md#download_activity_file) | **GET** /api/v1/activity/{id}/file | Download original activity file, Strava activities not supported
[**download_activity_fit_file**](ActivitiesApi.md#download_activity_fit_file) | **GET** /api/v1/activity/{id}/fit-file | Download Intervals.icu generated activity fit file
[**download_activity_fit_files**](ActivitiesApi.md#download_activity_fit_files) | **POST** /api/v1/athlete/{id}/download-fit-files | Download zip of Intervals.icu generated activity fit files
[**download_activity_gpx_file**](ActivitiesApi.md#download_activity_gpx_file) | **GET** /api/v1/activity/{id}/gpx-file | Download Intervals.icu generated activity gpx file
[**find_best_efforts**](ActivitiesApi.md#find_best_efforts) | **GET** /api/v1/activity/{id}/best-efforts | Find best efforts in the activity
[**get_activities**](ActivitiesApi.md#get_activities) | **GET** /api/v1/athlete/{athleteId}/activities/{ids} | Fetch multiple activities by id. Missing activities are ignored
[**get_activity**](ActivitiesApi.md#get_activity) | **GET** /api/v1/activity/{id} | Get an activity
[**get_activity_hr_curve**](ActivitiesApi.md#get_activity_hr_curve) | **GET** /api/v1/activity/{id}/hr-curve{ext} | Get activity heart rate curve in JSON or CSV (use .csv ext) format
[**get_activity_map**](ActivitiesApi.md#get_activity_map) | **GET** /api/v1/activity/{id}/map | Get activity map data
[**get_activity_pace_curve**](ActivitiesApi.md#get_activity_pace_curve) | **GET** /api/v1/activity/{id}/pace-curve{ext} | Get activity pace curve in JSON or CSV (use .csv ext) format
[**get_activity_power_curve**](ActivitiesApi.md#get_activity_power_curve) | **GET** /api/v1/activity/{id}/power-curve{ext} | Get activity power curve in JSON or CSV (use .csv ext) format
[**get_activity_power_spike_model**](ActivitiesApi.md#get_activity_power_spike_model) | **GET** /api/v1/activity/{id}/power-spike-model | Get activity power spike detection model
[**get_activity_segments**](ActivitiesApi.md#get_activity_segments) | **GET** /api/v1/activity/{id}/segments | Get activity segments
[**get_activity_streams**](ActivitiesApi.md#get_activity_streams) | **GET** /api/v1/activity/{id}/streams{ext} | List streams for the activity
[**get_activity_weather_summary**](ActivitiesApi.md#get_activity_weather_summary) | **GET** /api/v1/activity/{id}/weather-summary | Get activity weather summary information
[**get_athlete_mmp_model**](ActivitiesApi.md#get_athlete_mmp_model) | **GET** /api/v1/athlete/{id}/mmp-model | Get the power model used to resolve %MMP steps in workouts for the athlete
[**get_gap_histogram**](ActivitiesApi.md#get_gap_histogram) | **GET** /api/v1/activity/{id}/gap-histogram | Get activity gradient adjusted pace histogram
[**get_hr_histogram**](ActivitiesApi.md#get_hr_histogram) | **GET** /api/v1/activity/{id}/hr-histogram | Get activity heart rate histogram
[**get_hr_training_load_model**](ActivitiesApi.md#get_hr_training_load_model) | **GET** /api/v1/activity/{id}/hr-load-model | Get activity heart rate training load model
[**get_interval_stats**](ActivitiesApi.md#get_interval_stats) | **GET** /api/v1/activity/{id}/interval-stats | Return interval like stats for part of the activity
[**get_intervals**](ActivitiesApi.md#get_intervals) | **GET** /api/v1/activity/{id}/intervals | Get activity intervals
[**get_pace_histogram**](ActivitiesApi.md#get_pace_histogram) | **GET** /api/v1/activity/{id}/pace-histogram | Get activity pace histogram
[**get_power_histogram**](ActivitiesApi.md#get_power_histogram) | **GET** /api/v1/activity/{id}/power-histogram | Get activity power histogram
[**get_power_hr_curve**](ActivitiesApi.md#get_power_hr_curve) | **GET** /api/v1/athlete/{id}/power-hr-curve | Get the athlete&#39;s power vs heart rate curve for a date range
[**get_power_vs_hr**](ActivitiesApi.md#get_power_vs_hr) | **GET** /api/v1/activity/{id}/power-vs-hr{ext} | Get activity power vs heart rate data in JSON or CSV (use .csv ext) format
[**get_time_at_hr**](ActivitiesApi.md#get_time_at_hr) | **GET** /api/v1/activity/{id}/time-at-hr | Get activity time at heart rate data
[**list_activities**](ActivitiesApi.md#list_activities) | **GET** /api/v1/athlete/{id}/activities | List activities for a date range in desc date order
[**list_activities_around**](ActivitiesApi.md#list_activities_around) | **GET** /api/v1/athlete/{id}/activities-around | List activities before and after another activity in closest first order
[**list_activity_hr_curves**](ActivitiesApi.md#list_activity_hr_curves) | **GET** /api/v1/athlete/{id}/activity-hr-curves{ext} | Get best HR for a range of durations for matching activities in the date range
[**list_activity_pace_curves**](ActivitiesApi.md#list_activity_pace_curves) | **GET** /api/v1/athlete/{id}/activity-pace-curves{ext} | Get best pace for a range of distances for matching activities in the date range
[**list_activity_power_curves**](ActivitiesApi.md#list_activity_power_curves) | **GET** /api/v1/athlete/{id}/activity-power-curves{ext} | Get best power for a range of durations for matching activities in the date range
[**list_activity_power_curves1**](ActivitiesApi.md#list_activity_power_curves1) | **GET** /api/v1/activity/{id}/power-curves{ext} | Get activity power curves for one or more streams in JSON or CSV (use .csv ext) format
[**list_athlete_hr_curves**](ActivitiesApi.md#list_athlete_hr_curves) | **GET** /api/v1/athlete/{id}/hr-curves{ext} | List best heart rate curves for the athlete
[**list_athlete_pace_curves**](ActivitiesApi.md#list_athlete_pace_curves) | **GET** /api/v1/athlete/{id}/pace-curves{ext} | List best pace curves for the athlete
[**list_athlete_power_curves**](ActivitiesApi.md#list_athlete_power_curves) | **GET** /api/v1/athlete/{id}/power-curves{ext} | List best power curves for the athlete
[**list_tags2**](ActivitiesApi.md#list_tags2) | **GET** /api/v1/athlete/{id}/activity-tags | List all tags that have been applied to the athlete&#39;s activities
[**search_for_activities**](ActivitiesApi.md#search_for_activities) | **GET** /api/v1/athlete/{id}/activities/search | Search for activities by name or tag, returns summary info
[**search_for_activities_full**](ActivitiesApi.md#search_for_activities_full) | **GET** /api/v1/athlete/{id}/activities/search-full | Search for activities by name or tag, returns full activities
[**search_for_intervals**](ActivitiesApi.md#search_for_intervals) | **GET** /api/v1/athlete/{id}/activities/interval-search | Find activities with intervals matching duration and intensity
[**split_interval**](ActivitiesApi.md#split_interval) | **PUT** /api/v1/activity/{id}/split-interval | Split an interval
[**update_activity**](ActivitiesApi.md#update_activity) | **PUT** /api/v1/activity/{id} | Update activity
[**update_activity_streams**](ActivitiesApi.md#update_activity_streams) | **PUT** /api/v1/activity/{id}/streams | Update streams for the activity from JSON
[**update_interval**](ActivitiesApi.md#update_interval) | **PUT** /api/v1/activity/{id}/intervals/{intervalId} | Update/create an interval
[**update_intervals**](ActivitiesApi.md#update_intervals) | **PUT** /api/v1/activity/{id}/intervals | Update intervals for an activity
[**upload_activity**](ActivitiesApi.md#upload_activity) | **POST** /api/v1/athlete/{id}/activities | Create new activities from an uploaded file (fit, tcx, gpx or zip or gz of the same) as multipart/form-data
[**upload_activity_streams_csv**](ActivitiesApi.md#upload_activity_streams_csv) | **PUT** /api/v1/activity/{id}/streams.csv | Update streams for the activity from CSV


# **create_manual_activity**
> Activity create_manual_activity(id, activity)

Create a manual activity

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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    activity = intervals_icu_client.Activity() # Activity | 

    try:
        # Create a manual activity
        api_response = api_instance.create_manual_activity(id, activity)
        print("The response of ActivitiesApi->create_manual_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->create_manual_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **activity** | [**Activity**](Activity.md)|  | 

### Return type

[**Activity**](Activity.md)

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

# **delete_activity**
> ActivityId delete_activity(id)

Delete an activity

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.activity_id import ActivityId
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete an activity
        api_response = api_instance.delete_activity(id)
        print("The response of ActivitiesApi->delete_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->delete_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ActivityId**](ActivityId.md)

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

# **delete_intervals**
> IntervalsDTO delete_intervals(id, interval)

Delete intervals

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.interval import Interval
from intervals_icu_client.models.intervals_dto import IntervalsDTO
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    interval = [intervals_icu_client.Interval()] # List[Interval] | 

    try:
        # Delete intervals
        api_response = api_instance.delete_intervals(id, interval)
        print("The response of ActivitiesApi->delete_intervals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->delete_intervals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **interval** | [**List[Interval]**](Interval.md)|  | 

### Return type

[**IntervalsDTO**](IntervalsDTO.md)

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

# **download_activities_as_csv**
> download_activities_as_csv(id)

Download activities as CSV

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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Download activities as CSV
        api_instance.download_activities_as_csv(id)
    except Exception as e:
        print("Exception when calling ActivitiesApi->download_activities_as_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **download_activity_file**
> download_activity_file(id)

Download original activity file, Strava activities not supported

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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Download original activity file, Strava activities not supported
        api_instance.download_activity_file(id)
    except Exception as e:
        print("Exception when calling ActivitiesApi->download_activity_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **download_activity_fit_file**
> download_activity_fit_file(id, power=power, hr=hr)

Download Intervals.icu generated activity fit file

Not supported for Strava activities

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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    power = True # bool | Include power data (optional) (default to True)
    hr = True # bool | Include heart rate data (optional) (default to True)

    try:
        # Download Intervals.icu generated activity fit file
        api_instance.download_activity_fit_file(id, power=power, hr=hr)
    except Exception as e:
        print("Exception when calling ActivitiesApi->download_activity_fit_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **power** | **bool**| Include power data | [optional] [default to True]
 **hr** | **bool**| Include heart rate data | [optional] [default to True]

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

# **download_activity_fit_files**
> download_activity_fit_files(id, ids, power=power, hr=hr)

Download zip of Intervals.icu generated activity fit files

Strava activities are not included

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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    ids = ['ids_example'] # List[str] | Activity id's to download
    power = True # bool | Include power data (optional) (default to True)
    hr = True # bool | Include heart rate data (optional) (default to True)

    try:
        # Download zip of Intervals.icu generated activity fit files
        api_instance.download_activity_fit_files(id, ids, power=power, hr=hr)
    except Exception as e:
        print("Exception when calling ActivitiesApi->download_activity_fit_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ids** | [**List[str]**](str.md)| Activity id&#39;s to download | 
 **power** | **bool**| Include power data | [optional] [default to True]
 **hr** | **bool**| Include heart rate data | [optional] [default to True]

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

# **download_activity_gpx_file**
> download_activity_gpx_file(id, power=power, hr=hr)

Download Intervals.icu generated activity gpx file

Not supported for Strava activities and activities without GPS data

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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    power = True # bool | Include power data (optional) (default to True)
    hr = True # bool | Include heart rate data (optional) (default to True)

    try:
        # Download Intervals.icu generated activity gpx file
        api_instance.download_activity_gpx_file(id, power=power, hr=hr)
    except Exception as e:
        print("Exception when calling ActivitiesApi->download_activity_gpx_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **power** | **bool**| Include power data | [optional] [default to True]
 **hr** | **bool**| Include heart rate data | [optional] [default to True]

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

# **find_best_efforts**
> BestEfforts find_best_efforts(id, stream, duration=duration, distance=distance, count=count, min_value=min_value, exclude_intervals=exclude_intervals, start_index=start_index, end_index=end_index)

Find best efforts in the activity

One of duration or distance is required

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.best_efforts import BestEfforts
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    stream = 'stream_example' # str | Stream to search
    duration = 56 # int | Duration of each effort in seconds (optional)
    distance = 3.4 # float | Distance of each effort in meters (optional)
    count = 8 # int | Number of efforts to return (optional) (default to 8)
    min_value = 3.4 # float | Minimum average value for each interval, intervals will expand if specified (optional)
    exclude_intervals = False # bool | If true portions of the stream that are included in work intervals are not considered (optional) (default to False)
    start_index = 0 # int | First point in stream to consider (optional) (default to 0)
    end_index = 0 # int | Last point in stream to consider (exclusive, default is whole stream) (optional) (default to 0)

    try:
        # Find best efforts in the activity
        api_response = api_instance.find_best_efforts(id, stream, duration=duration, distance=distance, count=count, min_value=min_value, exclude_intervals=exclude_intervals, start_index=start_index, end_index=end_index)
        print("The response of ActivitiesApi->find_best_efforts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->find_best_efforts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **stream** | **str**| Stream to search | 
 **duration** | **int**| Duration of each effort in seconds | [optional] 
 **distance** | **float**| Distance of each effort in meters | [optional] 
 **count** | **int**| Number of efforts to return | [optional] [default to 8]
 **min_value** | **float**| Minimum average value for each interval, intervals will expand if specified | [optional] 
 **exclude_intervals** | **bool**| If true portions of the stream that are included in work intervals are not considered | [optional] [default to False]
 **start_index** | **int**| First point in stream to consider | [optional] [default to 0]
 **end_index** | **int**| Last point in stream to consider (exclusive, default is whole stream) | [optional] [default to 0]

### Return type

[**BestEfforts**](BestEfforts.md)

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

# **get_activities**
> List[Activity] get_activities(athlete_id, ids, intervals=intervals)

Fetch multiple activities by id. Missing activities are ignored

Strava activities are returned as empty stubs

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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    athlete_id = 'athlete_id_example' # str | 
    ids = ['ids_example'] # List[str] | 
    intervals = True # bool | Include interval data (icu_intervals and icu_groups fields) (optional)

    try:
        # Fetch multiple activities by id. Missing activities are ignored
        api_response = api_instance.get_activities(athlete_id, ids, intervals=intervals)
        print("The response of ActivitiesApi->get_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **athlete_id** | **str**|  | 
 **ids** | [**List[str]**](str.md)|  | 
 **intervals** | **bool**| Include interval data (icu_intervals and icu_groups fields) | [optional] 

### Return type

[**List[Activity]**](Activity.md)

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

# **get_activity**
> GetActivityDefaultResponse get_activity(id, intervals=intervals)

Get an activity

An empty stub object is returned for Strava activities

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.get_activity_default_response import GetActivityDefaultResponse
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    intervals = True # bool | Include interval data (optional)

    try:
        # Get an activity
        api_response = api_instance.get_activity(id, intervals=intervals)
        print("The response of ActivitiesApi->get_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **intervals** | **bool**| Include interval data | [optional] 

### Return type

[**GetActivityDefaultResponse**](GetActivityDefaultResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_hr_curve**
> HRCurve get_activity_hr_curve(id, ext)

Get activity heart rate curve in JSON or CSV (use .csv ext) format

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.hr_curve import HRCurve
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    ext = 'ext_example' # str | 

    try:
        # Get activity heart rate curve in JSON or CSV (use .csv ext) format
        api_response = api_instance.get_activity_hr_curve(id, ext)
        print("The response of ActivitiesApi->get_activity_hr_curve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_activity_hr_curve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ext** | **str**|  | 

### Return type

[**HRCurve**](HRCurve.md)

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

# **get_activity_map**
> MapData get_activity_map(id, bounds=bounds, bounds_only=bounds_only, weather=weather)

Get activity map data

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.map_data import MapData
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    bounds = [3.4] # List[float] | Optional comma separated bounding box (left, top, right, bottom) to limit points returned (optional)
    bounds_only = False # bool | Only return the map bounds, not the latlngs (optional) (default to False)
    weather = False # bool | Include weather points if available (optional) (default to False)

    try:
        # Get activity map data
        api_response = api_instance.get_activity_map(id, bounds=bounds, bounds_only=bounds_only, weather=weather)
        print("The response of ActivitiesApi->get_activity_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_activity_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **bounds** | [**List[float]**](float.md)| Optional comma separated bounding box (left, top, right, bottom) to limit points returned | [optional] 
 **bounds_only** | **bool**| Only return the map bounds, not the latlngs | [optional] [default to False]
 **weather** | **bool**| Include weather points if available | [optional] [default to False]

### Return type

[**MapData**](MapData.md)

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

# **get_activity_pace_curve**
> PaceCurve get_activity_pace_curve(id, ext, gap=gap)

Get activity pace curve in JSON or CSV (use .csv ext) format

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.pace_curve import PaceCurve
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    ext = 'ext_example' # str | 
    gap = False # bool |  (optional) (default to False)

    try:
        # Get activity pace curve in JSON or CSV (use .csv ext) format
        api_response = api_instance.get_activity_pace_curve(id, ext, gap=gap)
        print("The response of ActivitiesApi->get_activity_pace_curve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_activity_pace_curve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ext** | **str**|  | 
 **gap** | **bool**|  | [optional] [default to False]

### Return type

[**PaceCurve**](PaceCurve.md)

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

# **get_activity_power_curve**
> PowerCurve get_activity_power_curve(id, ext, fatigue=fatigue)

Get activity power curve in JSON or CSV (use .csv ext) format

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.power_curve import PowerCurve
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    ext = 'ext_example' # str | 
    fatigue = 'fatigue_example' # str | Use kj0 or kj1 to get one of the athlete's predefined fatigued power curves (optional)

    try:
        # Get activity power curve in JSON or CSV (use .csv ext) format
        api_response = api_instance.get_activity_power_curve(id, ext, fatigue=fatigue)
        print("The response of ActivitiesApi->get_activity_power_curve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_activity_power_curve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ext** | **str**|  | 
 **fatigue** | **str**| Use kj0 or kj1 to get one of the athlete&#39;s predefined fatigued power curves | [optional] 

### Return type

[**PowerCurve**](PowerCurve.md)

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

# **get_activity_power_spike_model**
> PowerModel get_activity_power_spike_model(id)

Get activity power spike detection model

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.power_model import PowerModel
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get activity power spike detection model
        api_response = api_instance.get_activity_power_spike_model(id)
        print("The response of ActivitiesApi->get_activity_power_spike_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_activity_power_spike_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PowerModel**](PowerModel.md)

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

# **get_activity_segments**
> List[IcuSegment] get_activity_segments(id)

Get activity segments

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.icu_segment import IcuSegment
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get activity segments
        api_response = api_instance.get_activity_segments(id)
        print("The response of ActivitiesApi->get_activity_segments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_activity_segments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[IcuSegment]**](IcuSegment.md)

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

# **get_activity_streams**
> List[ActivityStream] get_activity_streams(id, ext, types=types, include_defaults=include_defaults)

List streams for the activity

Note that this endpoint will return 'fixed_watts' as 'watts'. If 'raw_watts' is asked for or types is null then the 'watts' stream is renamed to 'raw_watts'. If ext is .csv then CSV data is returned instead of JSON

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.activity_stream import ActivityStream
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    ext = 'ext_example' # str | 
    types = ['types_example'] # List[str] | Streams required (optional)
    include_defaults = False # bool | Include default streams in addition to any specified in types (optional) (default to False)

    try:
        # List streams for the activity
        api_response = api_instance.get_activity_streams(id, ext, types=types, include_defaults=include_defaults)
        print("The response of ActivitiesApi->get_activity_streams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_activity_streams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ext** | **str**|  | 
 **types** | [**List[str]**](str.md)| Streams required | [optional] 
 **include_defaults** | **bool**| Include default streams in addition to any specified in types | [optional] [default to False]

### Return type

[**List[ActivityStream]**](ActivityStream.md)

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

# **get_activity_weather_summary**
> ActivityWeatherSummary get_activity_weather_summary(id, start_index=start_index, end_index=end_index)

Get activity weather summary information

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.activity_weather_summary import ActivityWeatherSummary
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    start_index = 0 # int | Optional index of first point in activity to use (optional) (default to 0)
    end_index = 0 # int | Optional index of last point in activity to use (exclusive) (optional) (default to 0)

    try:
        # Get activity weather summary information
        api_response = api_instance.get_activity_weather_summary(id, start_index=start_index, end_index=end_index)
        print("The response of ActivitiesApi->get_activity_weather_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_activity_weather_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **start_index** | **int**| Optional index of first point in activity to use | [optional] [default to 0]
 **end_index** | **int**| Optional index of last point in activity to use (exclusive) | [optional] [default to 0]

### Return type

[**ActivityWeatherSummary**](ActivityWeatherSummary.md)

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

# **get_athlete_mmp_model**
> PowerModel get_athlete_mmp_model(id, type)

Get the power model used to resolve %MMP steps in workouts for the athlete

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.power_model import PowerModel
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    type = 'type_example' # str | 

    try:
        # Get the power model used to resolve %MMP steps in workouts for the athlete
        api_response = api_instance.get_athlete_mmp_model(id, type)
        print("The response of ActivitiesApi->get_athlete_mmp_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_athlete_mmp_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **type** | **str**|  | 

### Return type

[**PowerModel**](PowerModel.md)

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

# **get_gap_histogram**
> List[Bucket] get_gap_histogram(id)

Get activity gradient adjusted pace histogram

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.bucket import Bucket
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get activity gradient adjusted pace histogram
        api_response = api_instance.get_gap_histogram(id)
        print("The response of ActivitiesApi->get_gap_histogram:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_gap_histogram: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[Bucket]**](Bucket.md)

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

# **get_hr_histogram**
> List[Bucket] get_hr_histogram(id, bucket_size=bucket_size)

Get activity heart rate histogram

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.bucket import Bucket
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    bucket_size = 56 # int | Beats per bucket (default 5) (optional)

    try:
        # Get activity heart rate histogram
        api_response = api_instance.get_hr_histogram(id, bucket_size=bucket_size)
        print("The response of ActivitiesApi->get_hr_histogram:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_hr_histogram: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **bucket_size** | **int**| Beats per bucket (default 5) | [optional] 

### Return type

[**List[Bucket]**](Bucket.md)

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

# **get_hr_training_load_model**
> HRLoadModel get_hr_training_load_model(id)

Get activity heart rate training load model

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.hr_load_model import HRLoadModel
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get activity heart rate training load model
        api_response = api_instance.get_hr_training_load_model(id)
        print("The response of ActivitiesApi->get_hr_training_load_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_hr_training_load_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**HRLoadModel**](HRLoadModel.md)

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

# **get_interval_stats**
> Interval get_interval_stats(id, start_index, end_index)

Return interval like stats for part of the activity

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.interval import Interval
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    start_index = 56 # int | 
    end_index = 56 # int | 

    try:
        # Return interval like stats for part of the activity
        api_response = api_instance.get_interval_stats(id, start_index, end_index)
        print("The response of ActivitiesApi->get_interval_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_interval_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **start_index** | **int**|  | 
 **end_index** | **int**|  | 

### Return type

[**Interval**](Interval.md)

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

# **get_intervals**
> IntervalsDTO get_intervals(id)

Get activity intervals

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.intervals_dto import IntervalsDTO
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get activity intervals
        api_response = api_instance.get_intervals(id)
        print("The response of ActivitiesApi->get_intervals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_intervals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**IntervalsDTO**](IntervalsDTO.md)

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

# **get_pace_histogram**
> List[Bucket] get_pace_histogram(id)

Get activity pace histogram

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.bucket import Bucket
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get activity pace histogram
        api_response = api_instance.get_pace_histogram(id)
        print("The response of ActivitiesApi->get_pace_histogram:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_pace_histogram: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[Bucket]**](Bucket.md)

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

# **get_power_histogram**
> List[Bucket] get_power_histogram(id, bucket_size=bucket_size)

Get activity power histogram

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.bucket import Bucket
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    bucket_size = 56 # int | Watts per bucket (default 25) (optional)

    try:
        # Get activity power histogram
        api_response = api_instance.get_power_histogram(id, bucket_size=bucket_size)
        print("The response of ActivitiesApi->get_power_histogram:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_power_histogram: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **bucket_size** | **int**| Watts per bucket (default 25) | [optional] 

### Return type

[**List[Bucket]**](Bucket.md)

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

# **get_power_hr_curve**
> PowerHRCurve get_power_hr_curve(id, start, end)

Get the athlete's power vs heart rate curve for a date range

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.power_hr_curve import PowerHRCurve
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    start = 'start_example' # str | Starting local date (ISO-8601)
    end = 'end_example' # str | Ending local date (ISO-8601), inclusive

    try:
        # Get the athlete's power vs heart rate curve for a date range
        api_response = api_instance.get_power_hr_curve(id, start, end)
        print("The response of ActivitiesApi->get_power_hr_curve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_power_hr_curve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **start** | **str**| Starting local date (ISO-8601) | 
 **end** | **str**| Ending local date (ISO-8601), inclusive | 

### Return type

[**PowerHRCurve**](PowerHRCurve.md)

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

# **get_power_vs_hr**
> PowerVsHRPlot get_power_vs_hr(id, ext)

Get activity power vs heart rate data in JSON or CSV (use .csv ext) format

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.power_vs_hr_plot import PowerVsHRPlot
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    ext = 'ext_example' # str | 

    try:
        # Get activity power vs heart rate data in JSON or CSV (use .csv ext) format
        api_response = api_instance.get_power_vs_hr(id, ext)
        print("The response of ActivitiesApi->get_power_vs_hr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_power_vs_hr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ext** | **str**|  | 

### Return type

[**PowerVsHRPlot**](PowerVsHRPlot.md)

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

# **get_time_at_hr**
> Plot get_time_at_hr(id)

Get activity time at heart rate data

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.plot import Plot
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get activity time at heart rate data
        api_response = api_instance.get_time_at_hr(id)
        print("The response of ActivitiesApi->get_time_at_hr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->get_time_at_hr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Plot**](Plot.md)

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

# **list_activities**
> List[Activity] list_activities(id, oldest, newest=newest, route_id=route_id, limit=limit, fields=fields)

List activities for a date range in desc date order

An empty stub object is returned for Strava activities

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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    oldest = 'oldest_example' # str | Local ISO-8601 date or date and time e.g. 2019-07-22T16:18:49 or 2019-07-22
    newest = 'newest_example' # str | Local ISO-8601 date or date and time, defaults to now (optional)
    route_id = 56 # int | Only return activities on this route (optional)
    limit = 56 # int | Return at most this many activities (optional)
    fields = ['fields_example'] # List[str] | Comma separated list of field names to include in the returned objects (default is all), also excludes null values (optional)

    try:
        # List activities for a date range in desc date order
        api_response = api_instance.list_activities(id, oldest, newest=newest, route_id=route_id, limit=limit, fields=fields)
        print("The response of ActivitiesApi->list_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->list_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **oldest** | **str**| Local ISO-8601 date or date and time e.g. 2019-07-22T16:18:49 or 2019-07-22 | 
 **newest** | **str**| Local ISO-8601 date or date and time, defaults to now | [optional] 
 **route_id** | **int**| Only return activities on this route | [optional] 
 **limit** | **int**| Return at most this many activities | [optional] 
 **fields** | [**List[str]**](str.md)| Comma separated list of field names to include in the returned objects (default is all), also excludes null values | [optional] 

### Return type

[**List[Activity]**](Activity.md)

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

# **list_activities_around**
> List[Activity] list_activities_around(id, activity_id, route_id=route_id, limit=limit)

List activities before and after another activity in closest first order

An empty stub object is returned for Strava activities

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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    activity_id = 'activity_id_example' # str | The activity at the center (not returned in the data set)
    route_id = 56 # int | Only return activities on this route (activityId must have this route_id) (optional)
    limit = 30 # int | Return at most this many activities (default 30) (optional) (default to 30)

    try:
        # List activities before and after another activity in closest first order
        api_response = api_instance.list_activities_around(id, activity_id, route_id=route_id, limit=limit)
        print("The response of ActivitiesApi->list_activities_around:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->list_activities_around: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **activity_id** | **str**| The activity at the center (not returned in the data set) | 
 **route_id** | **int**| Only return activities on this route (activityId must have this route_id) | [optional] 
 **limit** | **int**| Return at most this many activities (default 30) | [optional] [default to 30]

### Return type

[**List[Activity]**](Activity.md)

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

# **list_activity_hr_curves**
> ActivityHRCurvePayload list_activity_hr_curves(id, ext, oldest, newest, filters=filters, secs=secs, type=type)

Get best HR for a range of durations for matching activities in the date range

Use ext of .csv to get results in CSV format

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.activity_filter import ActivityFilter
from intervals_icu_client.models.activity_hr_curve_payload import ActivityHRCurvePayload
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    ext = 'ext_example' # str | 
    oldest = 'oldest_example' # str | Local ISO-8601 date or date and time e.g. 2019-07-22T16:18:49 or 2019-07-22
    newest = 'newest_example' # str | Local ISO-8601 date or date and time (inclusive)
    filters = [intervals_icu_client.ActivityFilter()] # List[ActivityFilter] | Only return activities matching all the filters in this list (optional)
    secs = [56] # List[int] | Optional durations to return (default is all, in seconds comma separated) (optional)
    type = 'type_example' # str | The sport (Ride, Run etc.). If filters is not provided or is blank or does not contain a type filter then activities for the types of the sport matching this parameter are included (optional)

    try:
        # Get best HR for a range of durations for matching activities in the date range
        api_response = api_instance.list_activity_hr_curves(id, ext, oldest, newest, filters=filters, secs=secs, type=type)
        print("The response of ActivitiesApi->list_activity_hr_curves:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->list_activity_hr_curves: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ext** | **str**|  | 
 **oldest** | **str**| Local ISO-8601 date or date and time e.g. 2019-07-22T16:18:49 or 2019-07-22 | 
 **newest** | **str**| Local ISO-8601 date or date and time (inclusive) | 
 **filters** | [**List[ActivityFilter]**](ActivityFilter.md)| Only return activities matching all the filters in this list | [optional] 
 **secs** | [**List[int]**](int.md)| Optional durations to return (default is all, in seconds comma separated) | [optional] 
 **type** | **str**| The sport (Ride, Run etc.). If filters is not provided or is blank or does not contain a type filter then activities for the types of the sport matching this parameter are included | [optional] 

### Return type

[**ActivityHRCurvePayload**](ActivityHRCurvePayload.md)

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

# **list_activity_pace_curves**
> list_activity_pace_curves(id, ext, oldest, newest, type=type, filters=filters, distances=distances, gap=gap)

Get best pace for a range of distances for matching activities in the date range

Use ext of .csv to get results in CSV format

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.activity_filter import ActivityFilter
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    ext = 'ext_example' # str | 
    oldest = 'oldest_example' # str | Local ISO-8601 date or date and time e.g. 2019-07-22T16:18:49 or 2019-07-22
    newest = 'newest_example' # str | Local ISO-8601 date or date and time (inclusive)
    type = 'type_example' # str | The sport (Ride, Run etc.). If filters is not provided or is blank or does not contain a type filter then activities for the types of the sport matching this parameter are included (optional)
    filters = [intervals_icu_client.ActivityFilter()] # List[ActivityFilter] | Only return activities matching all the filters in this list (optional)
    distances = [3.4] # List[float] | Distances required (in meters, comma separated) (optional)
    gap = False # bool | Return gradient adjusted pace curves (optional) (default to False)

    try:
        # Get best pace for a range of distances for matching activities in the date range
        api_instance.list_activity_pace_curves(id, ext, oldest, newest, type=type, filters=filters, distances=distances, gap=gap)
    except Exception as e:
        print("Exception when calling ActivitiesApi->list_activity_pace_curves: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ext** | **str**|  | 
 **oldest** | **str**| Local ISO-8601 date or date and time e.g. 2019-07-22T16:18:49 or 2019-07-22 | 
 **newest** | **str**| Local ISO-8601 date or date and time (inclusive) | 
 **type** | **str**| The sport (Ride, Run etc.). If filters is not provided or is blank or does not contain a type filter then activities for the types of the sport matching this parameter are included | [optional] 
 **filters** | [**List[ActivityFilter]**](ActivityFilter.md)| Only return activities matching all the filters in this list | [optional] 
 **distances** | [**List[float]**](float.md)| Distances required (in meters, comma separated) | [optional] 
 **gap** | **bool**| Return gradient adjusted pace curves | [optional] [default to False]

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

# **list_activity_power_curves**
> ActivityPowerCurvePayload list_activity_power_curves(id, ext, oldest, newest, filters=filters, secs=secs, type=type, fatigue=fatigue)

Get best power for a range of durations for matching activities in the date range

Use ext of .csv to get results in CSV format

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.activity_filter import ActivityFilter
from intervals_icu_client.models.activity_power_curve_payload import ActivityPowerCurvePayload
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    ext = 'ext_example' # str | 
    oldest = 'oldest_example' # str | Local ISO-8601 date or date and time e.g. 2019-07-22T16:18:49 or 2019-07-22
    newest = 'newest_example' # str | Local ISO-8601 date or date and time (inclusive)
    filters = [intervals_icu_client.ActivityFilter()] # List[ActivityFilter] | Only return activities matching all the filters in this list (optional)
    secs = [56] # List[int] | Optional durations to return (default is all, in seconds comma separated) (optional)
    type = 'type_example' # str | The sport (Ride, Run etc.). If filters is not provided or is blank or does not contain a type filter then activities for the types of the sport matching this parameter are included. Required if fatigue is used (optional)
    fatigue = 'fatigue_example' # str | Use kj0 or kj1 to get one of the athlete's predefined fatigued power curves (optional)

    try:
        # Get best power for a range of durations for matching activities in the date range
        api_response = api_instance.list_activity_power_curves(id, ext, oldest, newest, filters=filters, secs=secs, type=type, fatigue=fatigue)
        print("The response of ActivitiesApi->list_activity_power_curves:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->list_activity_power_curves: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ext** | **str**|  | 
 **oldest** | **str**| Local ISO-8601 date or date and time e.g. 2019-07-22T16:18:49 or 2019-07-22 | 
 **newest** | **str**| Local ISO-8601 date or date and time (inclusive) | 
 **filters** | [**List[ActivityFilter]**](ActivityFilter.md)| Only return activities matching all the filters in this list | [optional] 
 **secs** | [**List[int]**](int.md)| Optional durations to return (default is all, in seconds comma separated) | [optional] 
 **type** | **str**| The sport (Ride, Run etc.). If filters is not provided or is blank or does not contain a type filter then activities for the types of the sport matching this parameter are included. Required if fatigue is used | [optional] 
 **fatigue** | **str**| Use kj0 or kj1 to get one of the athlete&#39;s predefined fatigued power curves | [optional] 

### Return type

[**ActivityPowerCurvePayload**](ActivityPowerCurvePayload.md)

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

# **list_activity_power_curves1**
> List[PowerCurve] list_activity_power_curves1(id, ext, types=types, fatigue=fatigue)

Get activity power curves for one or more streams in JSON or CSV (use .csv ext) format

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.power_curve import PowerCurve
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    ext = 'ext_example' # str | 
    types = ['types_example'] # List[str] | Comma separated list of streams required (default is watts) (optional)
    fatigue = ['fatigue_example'] # List[str] | Comma separated list of normal, kj0 or kj1 to return normal and/or fatigued curves (optional)

    try:
        # Get activity power curves for one or more streams in JSON or CSV (use .csv ext) format
        api_response = api_instance.list_activity_power_curves1(id, ext, types=types, fatigue=fatigue)
        print("The response of ActivitiesApi->list_activity_power_curves1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->list_activity_power_curves1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ext** | **str**|  | 
 **types** | [**List[str]**](str.md)| Comma separated list of streams required (default is watts) | [optional] 
 **fatigue** | [**List[str]**](str.md)| Comma separated list of normal, kj0 or kj1 to return normal and/or fatigued curves | [optional] 

### Return type

[**List[PowerCurve]**](PowerCurve.md)

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

# **list_athlete_hr_curves**
> DataCurveSetHRCurve list_athlete_hr_curves(id, ext, f1, f2, f3, newest=newest, curves=curves, type=type, sub_max_efforts=sub_max_efforts, now=now, filters=filters)

List best heart rate curves for the athlete

Curves are specified as follows: 1y (past year), 2y (past 2 years) etc., 42d (past 42 days) etc., s0 (current season), s1 (previous season) etc., all (all time), r.2023-10-01.2023-10-31 (date range). If several of the f1, f2 and f3 filter parameters are specified then each curve is returned once for each filter, for comparing curves.

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.activity_filter import ActivityFilter
from intervals_icu_client.models.data_curve_set_hr_curve import DataCurveSetHRCurve
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    ext = 'ext_example' # str | 
    f1 = [intervals_icu_client.ActivityFilter()] # List[ActivityFilter] | If set each curve is returned with these filters applied to compare curves
    f2 = [intervals_icu_client.ActivityFilter()] # List[ActivityFilter] | If set each curve is returned with these filters applied to compare curves
    f3 = [intervals_icu_client.ActivityFilter()] # List[ActivityFilter] | If set each curve is returned with these filters applied to compare curves
    newest = 'newest_example' # str |  (optional)
    curves = ['curves_example'] # List[str] | Comma separated list of curves to return (default last year) (optional)
    type = 'type_example' # str | The sport (Ride, Run etc.). If filters is not provided or is blank or does not contain a type filter then activities for the types of the sport matching this parameter are included (optional)
    sub_max_efforts = 0 # int |  (optional) (default to 0)
    now = 'now_example' # str | Current local date (ISO-8601) (optional)
    filters = [intervals_icu_client.ActivityFilter()] # List[ActivityFilter] | Only consider activities matching all the filters in this list (optional)

    try:
        # List best heart rate curves for the athlete
        api_response = api_instance.list_athlete_hr_curves(id, ext, f1, f2, f3, newest=newest, curves=curves, type=type, sub_max_efforts=sub_max_efforts, now=now, filters=filters)
        print("The response of ActivitiesApi->list_athlete_hr_curves:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->list_athlete_hr_curves: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ext** | **str**|  | 
 **f1** | [**List[ActivityFilter]**](ActivityFilter.md)| If set each curve is returned with these filters applied to compare curves | 
 **f2** | [**List[ActivityFilter]**](ActivityFilter.md)| If set each curve is returned with these filters applied to compare curves | 
 **f3** | [**List[ActivityFilter]**](ActivityFilter.md)| If set each curve is returned with these filters applied to compare curves | 
 **newest** | **str**|  | [optional] 
 **curves** | [**List[str]**](str.md)| Comma separated list of curves to return (default last year) | [optional] 
 **type** | **str**| The sport (Ride, Run etc.). If filters is not provided or is blank or does not contain a type filter then activities for the types of the sport matching this parameter are included | [optional] 
 **sub_max_efforts** | **int**|  | [optional] [default to 0]
 **now** | **str**| Current local date (ISO-8601) | [optional] 
 **filters** | [**List[ActivityFilter]**](ActivityFilter.md)| Only consider activities matching all the filters in this list | [optional] 

### Return type

[**DataCurveSetHRCurve**](DataCurveSetHRCurve.md)

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

# **list_athlete_pace_curves**
> DataCurveSetPaceCurve list_athlete_pace_curves(id, ext, f1, f2, f3, newest=newest, curves=curves, type=type, include_ranks=include_ranks, sub_max_efforts=sub_max_efforts, now=now, gap=gap, pm_type=pm_type, filters=filters)

List best pace curves for the athlete

Curves are specified as follows: 1y (past year), 2y (past 2 years) etc., 42d (past 42 days) etc., s0 (current season), s1 (previous season) etc., all (all time), r.2023-10-01.2023-10-31 (date range). If several of f1, f2 and f3 filter parameters are specified then each curve is returned once for each filter, for comparing curves.

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.activity_filter import ActivityFilter
from intervals_icu_client.models.data_curve_set_pace_curve import DataCurveSetPaceCurve
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    ext = 'ext_example' # str | 
    f1 = [intervals_icu_client.ActivityFilter()] # List[ActivityFilter] | If set each curve is returned with these filters applied to compare curves
    f2 = [intervals_icu_client.ActivityFilter()] # List[ActivityFilter] | If set each curve is returned with these filters applied to compare curves
    f3 = [intervals_icu_client.ActivityFilter()] # List[ActivityFilter] | If set each curve is returned with these filters applied to compare curves
    newest = 'newest_example' # str |  (optional)
    curves = ['curves_example'] # List[str] | Comma separated list of curves to return (default last year) (optional)
    type = 'type_example' # str | The sport (Ride, Run etc.). If filters is not provided or is blank or does not contain a type filter then activities for the types of the sport matching this parameter are included (optional)
    include_ranks = False # bool |  (optional) (default to False)
    sub_max_efforts = 0 # int |  (optional) (default to 0)
    now = 'now_example' # str | Current local date (ISO-8601) (optional)
    gap = False # bool | Return gradient adjusted pace curves (optional) (default to False)
    pm_type = 'pm_type_example' # str |  (optional)
    filters = [intervals_icu_client.ActivityFilter()] # List[ActivityFilter] | Only consider activities matching all the filters in this list (optional)

    try:
        # List best pace curves for the athlete
        api_response = api_instance.list_athlete_pace_curves(id, ext, f1, f2, f3, newest=newest, curves=curves, type=type, include_ranks=include_ranks, sub_max_efforts=sub_max_efforts, now=now, gap=gap, pm_type=pm_type, filters=filters)
        print("The response of ActivitiesApi->list_athlete_pace_curves:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->list_athlete_pace_curves: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ext** | **str**|  | 
 **f1** | [**List[ActivityFilter]**](ActivityFilter.md)| If set each curve is returned with these filters applied to compare curves | 
 **f2** | [**List[ActivityFilter]**](ActivityFilter.md)| If set each curve is returned with these filters applied to compare curves | 
 **f3** | [**List[ActivityFilter]**](ActivityFilter.md)| If set each curve is returned with these filters applied to compare curves | 
 **newest** | **str**|  | [optional] 
 **curves** | [**List[str]**](str.md)| Comma separated list of curves to return (default last year) | [optional] 
 **type** | **str**| The sport (Ride, Run etc.). If filters is not provided or is blank or does not contain a type filter then activities for the types of the sport matching this parameter are included | [optional] 
 **include_ranks** | **bool**|  | [optional] [default to False]
 **sub_max_efforts** | **int**|  | [optional] [default to 0]
 **now** | **str**| Current local date (ISO-8601) | [optional] 
 **gap** | **bool**| Return gradient adjusted pace curves | [optional] [default to False]
 **pm_type** | **str**|  | [optional] 
 **filters** | [**List[ActivityFilter]**](ActivityFilter.md)| Only consider activities matching all the filters in this list | [optional] 

### Return type

[**DataCurveSetPaceCurve**](DataCurveSetPaceCurve.md)

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

# **list_athlete_power_curves**
> DataCurveSetPowerCurve list_athlete_power_curves(id, ext, type, f1, f2, f3, newest=newest, curves=curves, include_ranks=include_ranks, sub_max_efforts=sub_max_efforts, now=now, pm_type=pm_type, filters=filters)

List best power curves for the athlete

Curves are specified as follows: 1y (past year), 2y (past 2 years) etc., 42d (past 42 days) etc., s0 (current season), s1 (previous season) etc., all (all time), r.2023-10-01.2023-10-31 (date range). Curves can also have a -kj0 or -kj1 suffix to return fatigued curves. If several of f1, f2 and f3 filter parameters are specified then each curve is returned once for each filter, for comparing curves.

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.activity_filter import ActivityFilter
from intervals_icu_client.models.data_curve_set_power_curve import DataCurveSetPowerCurve
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    ext = 'ext_example' # str | 
    type = 'type_example' # str | The sport (Ride, Run etc.). If filters is not provided or is blank or does not contain a type filter then activities for the types of the sport matching this parameter are included
    f1 = [intervals_icu_client.ActivityFilter()] # List[ActivityFilter] | If set each curve is returned with these filters applied to compare curves
    f2 = [intervals_icu_client.ActivityFilter()] # List[ActivityFilter] | If set each curve is returned with these filters applied to compare curves
    f3 = [intervals_icu_client.ActivityFilter()] # List[ActivityFilter] | If set each curve is returned with these filters applied to compare curves
    newest = 'newest_example' # str |  (optional)
    curves = ['curves_example'] # List[str] | Comma separated list of curves to return (default last year) (optional)
    include_ranks = False # bool |  (optional) (default to False)
    sub_max_efforts = 0 # int |  (optional) (default to 0)
    now = 'now_example' # str | Current local date (ISO-8601) (optional)
    pm_type = 'pm_type_example' # str |  (optional)
    filters = [intervals_icu_client.ActivityFilter()] # List[ActivityFilter] | Only consider activities matching all the filters in this list (optional)

    try:
        # List best power curves for the athlete
        api_response = api_instance.list_athlete_power_curves(id, ext, type, f1, f2, f3, newest=newest, curves=curves, include_ranks=include_ranks, sub_max_efforts=sub_max_efforts, now=now, pm_type=pm_type, filters=filters)
        print("The response of ActivitiesApi->list_athlete_power_curves:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->list_athlete_power_curves: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ext** | **str**|  | 
 **type** | **str**| The sport (Ride, Run etc.). If filters is not provided or is blank or does not contain a type filter then activities for the types of the sport matching this parameter are included | 
 **f1** | [**List[ActivityFilter]**](ActivityFilter.md)| If set each curve is returned with these filters applied to compare curves | 
 **f2** | [**List[ActivityFilter]**](ActivityFilter.md)| If set each curve is returned with these filters applied to compare curves | 
 **f3** | [**List[ActivityFilter]**](ActivityFilter.md)| If set each curve is returned with these filters applied to compare curves | 
 **newest** | **str**|  | [optional] 
 **curves** | [**List[str]**](str.md)| Comma separated list of curves to return (default last year) | [optional] 
 **include_ranks** | **bool**|  | [optional] [default to False]
 **sub_max_efforts** | **int**|  | [optional] [default to 0]
 **now** | **str**| Current local date (ISO-8601) | [optional] 
 **pm_type** | **str**|  | [optional] 
 **filters** | [**List[ActivityFilter]**](ActivityFilter.md)| Only consider activities matching all the filters in this list | [optional] 

### Return type

[**DataCurveSetPowerCurve**](DataCurveSetPowerCurve.md)

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

# **list_tags2**
> List[str] list_tags2(id)

List all tags that have been applied to the athlete's activities

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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 

    try:
        # List all tags that have been applied to the athlete's activities
        api_response = api_instance.list_tags2(id)
        print("The response of ActivitiesApi->list_tags2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->list_tags2: %s\n" % e)
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

# **search_for_activities**
> List[ActivitySearchResult] search_for_activities(id, q, limit=limit)

Search for activities by name or tag, returns summary info

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.activity_search_result import ActivitySearchResult
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    q = 'q_example' # str | Search query, case insensitive name search or exact tag search if it starts with #
    limit = 56 # int |  (optional)

    try:
        # Search for activities by name or tag, returns summary info
        api_response = api_instance.search_for_activities(id, q, limit=limit)
        print("The response of ActivitiesApi->search_for_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->search_for_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **q** | **str**| Search query, case insensitive name search or exact tag search if it starts with # | 
 **limit** | **int**|  | [optional] 

### Return type

[**List[ActivitySearchResult]**](ActivitySearchResult.md)

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

# **search_for_activities_full**
> List[Activity] search_for_activities_full(id, q, limit=limit)

Search for activities by name or tag, returns full activities

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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    q = 'q_example' # str | Search query, case insensitive name search or exact tag search if it starts with #
    limit = 56 # int |  (optional)

    try:
        # Search for activities by name or tag, returns full activities
        api_response = api_instance.search_for_activities_full(id, q, limit=limit)
        print("The response of ActivitiesApi->search_for_activities_full:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->search_for_activities_full: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **q** | **str**| Search query, case insensitive name search or exact tag search if it starts with # | 
 **limit** | **int**|  | [optional] 

### Return type

[**List[Activity]**](Activity.md)

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

# **search_for_intervals**
> List[Activity] search_for_intervals(id, min_secs, max_secs, min_intensity, max_intensity, type=type, min_reps=min_reps, max_reps=max_reps, limit=limit)

Find activities with intervals matching duration and intensity

Activities returned most recent first

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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    min_secs = 56 # int | Min time in seconds
    max_secs = 56 # int | Max time in seconds
    min_intensity = 56 # int | Min intensity percentage
    max_intensity = 56 # int | Max intensity percentage
    type = 'type_example' # str | Interval type (optional)
    min_reps = 1 # int | Min number of intervals that need to match (optional) (default to 1)
    max_reps = 999999 # int | Max number of intervals that need to match (optional) (default to 999999)
    limit = 30 # int | Max results to return (optional) (default to 30)

    try:
        # Find activities with intervals matching duration and intensity
        api_response = api_instance.search_for_intervals(id, min_secs, max_secs, min_intensity, max_intensity, type=type, min_reps=min_reps, max_reps=max_reps, limit=limit)
        print("The response of ActivitiesApi->search_for_intervals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->search_for_intervals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **min_secs** | **int**| Min time in seconds | 
 **max_secs** | **int**| Max time in seconds | 
 **min_intensity** | **int**| Min intensity percentage | 
 **max_intensity** | **int**| Max intensity percentage | 
 **type** | **str**| Interval type | [optional] 
 **min_reps** | **int**| Min number of intervals that need to match | [optional] [default to 1]
 **max_reps** | **int**| Max number of intervals that need to match | [optional] [default to 999999]
 **limit** | **int**| Max results to return | [optional] [default to 30]

### Return type

[**List[Activity]**](Activity.md)

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

# **split_interval**
> IntervalsDTO split_interval(id, split_at)

Split an interval

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.intervals_dto import IntervalsDTO
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    split_at = 56 # int | Index to split interval at

    try:
        # Split an interval
        api_response = api_instance.split_interval(id, split_at)
        print("The response of ActivitiesApi->split_interval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->split_interval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **split_at** | **int**| Index to split interval at | 

### Return type

[**IntervalsDTO**](IntervalsDTO.md)

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

# **update_activity**
> Activity update_activity(id, activity)

Update activity

Strava activities cannot be updated

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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    activity = intervals_icu_client.Activity() # Activity | 

    try:
        # Update activity
        api_response = api_instance.update_activity(id, activity)
        print("The response of ActivitiesApi->update_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->update_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **activity** | [**Activity**](Activity.md)|  | 

### Return type

[**Activity**](Activity.md)

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

# **update_activity_streams**
> UpdateStreamsResult update_activity_streams(id, activity_stream)

Update streams for the activity from JSON

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.activity_stream import ActivityStream
from intervals_icu_client.models.update_streams_result import UpdateStreamsResult
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    activity_stream = [intervals_icu_client.ActivityStream()] # List[ActivityStream] | 

    try:
        # Update streams for the activity from JSON
        api_response = api_instance.update_activity_streams(id, activity_stream)
        print("The response of ActivitiesApi->update_activity_streams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->update_activity_streams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **activity_stream** | [**List[ActivityStream]**](ActivityStream.md)|  | 

### Return type

[**UpdateStreamsResult**](UpdateStreamsResult.md)

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

# **update_interval**
> IntervalsDTO update_interval(id, interval_id, interval)

Update/create an interval

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.interval import Interval
from intervals_icu_client.models.intervals_dto import IntervalsDTO
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    interval_id = 56 # int | 
    interval = intervals_icu_client.Interval() # Interval | 

    try:
        # Update/create an interval
        api_response = api_instance.update_interval(id, interval_id, interval)
        print("The response of ActivitiesApi->update_interval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->update_interval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **interval_id** | **int**|  | 
 **interval** | [**Interval**](Interval.md)|  | 

### Return type

[**IntervalsDTO**](IntervalsDTO.md)

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

# **update_intervals**
> IntervalsDTO update_intervals(id, interval, all=all)

Update intervals for an activity

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.interval import Interval
from intervals_icu_client.models.intervals_dto import IntervalsDTO
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    interval = [intervals_icu_client.Interval()] # List[Interval] | 
    all = True # bool | Any existing intervals are replaced, otherwise a merge is done (optional) (default to True)

    try:
        # Update intervals for an activity
        api_response = api_instance.update_intervals(id, interval, all=all)
        print("The response of ActivitiesApi->update_intervals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->update_intervals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **interval** | [**List[Interval]**](Interval.md)|  | 
 **all** | **bool**| Any existing intervals are replaced, otherwise a merge is done | [optional] [default to True]

### Return type

[**IntervalsDTO**](IntervalsDTO.md)

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

# **upload_activity**
> UploadResponse upload_activity(id, name=name, description=description, device_name=device_name, external_id=external_id, paired_event_id=paired_event_id)

Create new activities from an uploaded file (fit, tcx, gpx or zip or gz of the same) as multipart/form-data

Use the 'file' form parameter to supply the uploaded file. Multisport files are split into multiple activities. Activities are de-duped using a hash of the file. Response code is 201 if at least one new activity was created and 200 otherwise (all dups).

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.upload_response import UploadResponse
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 
    name = 'name_example' # str | Activity name (optional)
    description = 'description_example' # str | Activity description (optional)
    device_name = 'device_name_example' # str | Device the activity was created on e.g. Garmin Edge 540 (optional)
    external_id = 'external_id_example' # str | ID of the activity on the system it came from (optional)
    paired_event_id = 56 # int | Workout to pair with activity (optional)

    try:
        # Create new activities from an uploaded file (fit, tcx, gpx or zip or gz of the same) as multipart/form-data
        api_response = api_instance.upload_activity(id, name=name, description=description, device_name=device_name, external_id=external_id, paired_event_id=paired_event_id)
        print("The response of ActivitiesApi->upload_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->upload_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**| Activity name | [optional] 
 **description** | **str**| Activity description | [optional] 
 **device_name** | **str**| Device the activity was created on e.g. Garmin Edge 540 | [optional] 
 **external_id** | **str**| ID of the activity on the system it came from | [optional] 
 **paired_event_id** | **int**| Workout to pair with activity | [optional] 

### Return type

[**UploadResponse**](UploadResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_activity_streams_csv**
> UpdateStreamsResult upload_activity_streams_csv(id)

Update streams for the activity from CSV

Column headers for streams to be updated must match those returned from the /streams.csv endpoint

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.update_streams_result import UpdateStreamsResult
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
    api_instance = intervals_icu_client.ActivitiesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Update streams for the activity from CSV
        api_response = api_instance.upload_activity_streams_csv(id)
        print("The response of ActivitiesApi->upload_activity_streams_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->upload_activity_streams_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**UpdateStreamsResult**](UpdateStreamsResult.md)

### Authorization

[APIKey](../README.md#APIKey), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

