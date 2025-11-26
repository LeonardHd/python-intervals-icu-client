# intervals_icu_client.LibraryApi

All URIs are relative to *https://intervals.icu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_current_plan_changes**](LibraryApi.md#apply_current_plan_changes) | **PUT** /api/v1/athlete/{id}/apply-plan-changes | Apply any changes from the athlete&#39;s current plan to the athlete&#39;s calendar
[**create_folder**](LibraryApi.md#create_folder) | **POST** /api/v1/athlete/{id}/folders | Create a new workout folder or plan
[**create_multiple_workouts**](LibraryApi.md#create_multiple_workouts) | **POST** /api/v1/athlete/{id}/workouts/bulk | Create multiple new workouts in a folder or plan in the athlete&#39;s workout library
[**create_workout**](LibraryApi.md#create_workout) | **POST** /api/v1/athlete/{id}/workouts | Create a new workout in a folder or plan in the athlete&#39;s workout library
[**delete_folder**](LibraryApi.md#delete_folder) | **DELETE** /api/v1/athlete/{id}/folders/{folderId} | Delete a workout folder or plan including all workouts
[**delete_workout**](LibraryApi.md#delete_workout) | **DELETE** /api/v1/athlete/{id}/workouts/{workoutId} | Delete a workout (and optionally others added at the same time if the workout is on a plan)
[**download_workout**](LibraryApi.md#download_workout) | **POST** /api/v1/download-workout{ext} | Convert a workout to .zwo (Zwift), .mrc, .erg or .fit
[**download_workout_for_athlete**](LibraryApi.md#download_workout_for_athlete) | **POST** /api/v1/athlete/{id}/download-workout{ext} | Convert a workout to .zwo (Zwift), .mrc, .erg or .fit.
[**duplicate_workouts**](LibraryApi.md#duplicate_workouts) | **POST** /api/v1/athlete/{id}/duplicate-workouts | Duplicate workouts on a plan
[**import_workout_file**](LibraryApi.md#import_workout_file) | **POST** /api/v1/athlete/{id}/folders/{folderId}/import-workout | Create new workout from .zwo, .mrc, .erg or .fit file in a folder
[**list_folder_shared_with**](LibraryApi.md#list_folder_shared_with) | **GET** /api/v1/athlete/{id}/folders/{folderId}/shared-with | List athletes that the folder or plan has been shared with
[**list_folders**](LibraryApi.md#list_folders) | **GET** /api/v1/athlete/{id}/folders | List all the athlete&#39;s folders, plans and workouts
[**list_tags**](LibraryApi.md#list_tags) | **GET** /api/v1/athlete/{id}/workout-tags | List all tags that have been applied to workouts in the athlete&#39;s library
[**list_workouts**](LibraryApi.md#list_workouts) | **GET** /api/v1/athlete/{id}/workouts | List all the workouts in the athlete&#39;s library
[**show_workout**](LibraryApi.md#show_workout) | **GET** /api/v1/athlete/{id}/workouts/{workoutId} | Get a workout
[**update_folder**](LibraryApi.md#update_folder) | **PUT** /api/v1/athlete/{id}/folders/{folderId} | Update a workout folder or plan
[**update_folder_shared_with**](LibraryApi.md#update_folder_shared_with) | **PUT** /api/v1/athlete/{id}/folders/{folderId}/shared-with | Add/remove athletes from the share list for the folder
[**update_plan_workouts**](LibraryApi.md#update_plan_workouts) | **PUT** /api/v1/athlete/{id}/folders/{folderId}/workouts | Update a range of workouts on a plan. Currently only hide_from_athlete can be changed
[**update_workout**](LibraryApi.md#update_workout) | **PUT** /api/v1/athlete/{id}/workouts/{workoutId} | Update a workout


# **apply_current_plan_changes**
> Dict[str, object] apply_current_plan_changes(id)

Apply any changes from the athlete's current plan to the athlete's calendar

Only workouts from today or in the future are updated

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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 

    try:
        # Apply any changes from the athlete's current plan to the athlete's calendar
        api_response = api_instance.apply_current_plan_changes(id)
        print("The response of LibraryApi->apply_current_plan_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->apply_current_plan_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **create_folder**
> Folder create_folder(id, create_folder_dto)

Create a new workout folder or plan

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.create_folder_dto import CreateFolderDTO
from intervals_icu_client.models.folder import Folder
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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 
    create_folder_dto = intervals_icu_client.CreateFolderDTO() # CreateFolderDTO | 

    try:
        # Create a new workout folder or plan
        api_response = api_instance.create_folder(id, create_folder_dto)
        print("The response of LibraryApi->create_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->create_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_folder_dto** | [**CreateFolderDTO**](CreateFolderDTO.md)|  | 

### Return type

[**Folder**](Folder.md)

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

# **create_multiple_workouts**
> List[Workout] create_multiple_workouts(id, workout_ex)

Create multiple new workouts in a folder or plan in the athlete's workout library

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.workout import Workout
from intervals_icu_client.models.workout_ex import WorkoutEx
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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 
    workout_ex = [intervals_icu_client.WorkoutEx()] # List[WorkoutEx] | 

    try:
        # Create multiple new workouts in a folder or plan in the athlete's workout library
        api_response = api_instance.create_multiple_workouts(id, workout_ex)
        print("The response of LibraryApi->create_multiple_workouts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->create_multiple_workouts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **workout_ex** | [**List[WorkoutEx]**](WorkoutEx.md)|  | 

### Return type

[**List[Workout]**](Workout.md)

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

# **create_workout**
> Workout create_workout(id, workout_ex)

Create a new workout in a folder or plan in the athlete's workout library

This endpoint accepts workouts in native Intervals.icu format ('description' field) as well as zwo, mrc, erg and fit files (use 'file_contents' or 'file_contents_base64')

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.workout import Workout
from intervals_icu_client.models.workout_ex import WorkoutEx
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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 
    workout_ex = intervals_icu_client.WorkoutEx() # WorkoutEx | 

    try:
        # Create a new workout in a folder or plan in the athlete's workout library
        api_response = api_instance.create_workout(id, workout_ex)
        print("The response of LibraryApi->create_workout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->create_workout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **workout_ex** | [**WorkoutEx**](WorkoutEx.md)|  | 

### Return type

[**Workout**](Workout.md)

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

# **delete_folder**
> Dict[str, object] delete_folder(id, folder_id)

Delete a workout folder or plan including all workouts

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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 
    folder_id = 56 # int | 

    try:
        # Delete a workout folder or plan including all workouts
        api_response = api_instance.delete_folder(id, folder_id)
        print("The response of LibraryApi->delete_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->delete_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **folder_id** | **int**|  | 

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

# **delete_workout**
> List[int] delete_workout(id, workout_id, others=others)

Delete a workout (and optionally others added at the same time if the workout is on a plan)

Returns the ids of the deleted workout(s)

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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 
    workout_id = 56 # int | 
    others = True # bool |  (optional)

    try:
        # Delete a workout (and optionally others added at the same time if the workout is on a plan)
        api_response = api_instance.delete_workout(id, workout_id, others=others)
        print("The response of LibraryApi->delete_workout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->delete_workout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **workout_id** | **int**|  | 
 **others** | **bool**|  | [optional] 

### Return type

**List[int]**

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

# **download_workout**
> download_workout(ext, workout)

Convert a workout to .zwo (Zwift), .mrc, .erg or .fit

The athlete to use is extracted from the bearer token and used to resolve power targets etc.. Note that the create workout endpoint can convert workouts and might be more convenient.

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.workout import Workout
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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    ext = 'ext_example' # str | 
    workout = intervals_icu_client.Workout() # Workout | 

    try:
        # Convert a workout to .zwo (Zwift), .mrc, .erg or .fit
        api_instance.download_workout(ext, workout)
    except Exception as e:
        print("Exception when calling LibraryApi->download_workout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ext** | **str**|  | 
 **workout** | [**Workout**](Workout.md)|  | 

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

# **download_workout_for_athlete**
> download_workout_for_athlete(id, ext, workout)

Convert a workout to .zwo (Zwift), .mrc, .erg or .fit.

The athlete's settings are used to resolve power targets etc.. Note that the create workout endpoint can convert workouts and might be more convenient.

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.workout import Workout
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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 
    ext = 'ext_example' # str | 
    workout = intervals_icu_client.Workout() # Workout | 

    try:
        # Convert a workout to .zwo (Zwift), .mrc, .erg or .fit.
        api_instance.download_workout_for_athlete(id, ext, workout)
    except Exception as e:
        print("Exception when calling LibraryApi->download_workout_for_athlete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ext** | **str**|  | 
 **workout** | [**Workout**](Workout.md)|  | 

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

# **duplicate_workouts**
> List[Workout] duplicate_workouts(id, duplicate_workouts_dto)

Duplicate workouts on a plan

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.duplicate_workouts_dto import DuplicateWorkoutsDTO
from intervals_icu_client.models.workout import Workout
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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 
    duplicate_workouts_dto = intervals_icu_client.DuplicateWorkoutsDTO() # DuplicateWorkoutsDTO | 

    try:
        # Duplicate workouts on a plan
        api_response = api_instance.duplicate_workouts(id, duplicate_workouts_dto)
        print("The response of LibraryApi->duplicate_workouts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->duplicate_workouts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **duplicate_workouts_dto** | [**DuplicateWorkoutsDTO**](DuplicateWorkoutsDTO.md)|  | 

### Return type

[**List[Workout]**](Workout.md)

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

# **import_workout_file**
> Workout import_workout_file(id, folder_id, type, athlete_id=athlete_id, upload_wellness_request=upload_wellness_request)

Create new workout from .zwo, .mrc, .erg or .fit file in a folder

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.upload_wellness_request import UploadWellnessRequest
from intervals_icu_client.models.workout import Workout
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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 
    folder_id = 56 # int | 
    type = 'type_example' # str | 
    athlete_id = 'athlete_id_example' # str |  (optional)
    upload_wellness_request = intervals_icu_client.UploadWellnessRequest() # UploadWellnessRequest |  (optional)

    try:
        # Create new workout from .zwo, .mrc, .erg or .fit file in a folder
        api_response = api_instance.import_workout_file(id, folder_id, type, athlete_id=athlete_id, upload_wellness_request=upload_wellness_request)
        print("The response of LibraryApi->import_workout_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->import_workout_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **folder_id** | **int**|  | 
 **type** | **str**|  | 
 **athlete_id** | **str**|  | [optional] 
 **upload_wellness_request** | [**UploadWellnessRequest**](UploadWellnessRequest.md)|  | [optional] 

### Return type

[**Workout**](Workout.md)

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

# **list_folder_shared_with**
> List[SharedWith] list_folder_shared_with(id, folder_id)

List athletes that the folder or plan has been shared with

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.shared_with import SharedWith
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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 
    folder_id = 56 # int | 

    try:
        # List athletes that the folder or plan has been shared with
        api_response = api_instance.list_folder_shared_with(id, folder_id)
        print("The response of LibraryApi->list_folder_shared_with:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->list_folder_shared_with: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **folder_id** | **int**|  | 

### Return type

[**List[SharedWith]**](SharedWith.md)

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

# **list_folders**
> List[Folder] list_folders(id)

List all the athlete's folders, plans and workouts

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.folder import Folder
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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 

    try:
        # List all the athlete's folders, plans and workouts
        api_response = api_instance.list_folders(id)
        print("The response of LibraryApi->list_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->list_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[Folder]**](Folder.md)

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

# **list_tags**
> List[str] list_tags(id)

List all tags that have been applied to workouts in the athlete's library

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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 

    try:
        # List all tags that have been applied to workouts in the athlete's library
        api_response = api_instance.list_tags(id)
        print("The response of LibraryApi->list_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->list_tags: %s\n" % e)
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

# **list_workouts**
> List[Workout] list_workouts(id)

List all the workouts in the athlete's library

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.workout import Workout
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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 

    try:
        # List all the workouts in the athlete's library
        api_response = api_instance.list_workouts(id)
        print("The response of LibraryApi->list_workouts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->list_workouts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[Workout]**](Workout.md)

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

# **show_workout**
> Workout show_workout(id, workout_id)

Get a workout

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.workout import Workout
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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 
    workout_id = 56 # int | 

    try:
        # Get a workout
        api_response = api_instance.show_workout(id, workout_id)
        print("The response of LibraryApi->show_workout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->show_workout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **workout_id** | **int**|  | 

### Return type

[**Workout**](Workout.md)

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

# **update_folder**
> Folder update_folder(id, folder_id, folder)

Update a workout folder or plan

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.folder import Folder
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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 
    folder_id = 56 # int | 
    folder = intervals_icu_client.Folder() # Folder | 

    try:
        # Update a workout folder or plan
        api_response = api_instance.update_folder(id, folder_id, folder)
        print("The response of LibraryApi->update_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->update_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **folder_id** | **int**|  | 
 **folder** | [**Folder**](Folder.md)|  | 

### Return type

[**Folder**](Folder.md)

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

# **update_folder_shared_with**
> List[SharedWith] update_folder_shared_with(id, folder_id, shared_with)

Add/remove athletes from the share list for the folder

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.shared_with import SharedWith
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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 
    folder_id = 56 # int | 
    shared_with = [intervals_icu_client.SharedWith()] # List[SharedWith] | 

    try:
        # Add/remove athletes from the share list for the folder
        api_response = api_instance.update_folder_shared_with(id, folder_id, shared_with)
        print("The response of LibraryApi->update_folder_shared_with:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->update_folder_shared_with: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **folder_id** | **int**|  | 
 **shared_with** | [**List[SharedWith]**](SharedWith.md)|  | 

### Return type

[**List[SharedWith]**](SharedWith.md)

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

# **update_plan_workouts**
> List[Workout] update_plan_workouts(id, folder_id, oldest, newest, workout)

Update a range of workouts on a plan. Currently only hide_from_athlete can be changed

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.workout import Workout
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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 
    folder_id = 56 # int | 
    oldest = 56 # int | 
    newest = 56 # int | 
    workout = intervals_icu_client.Workout() # Workout | 

    try:
        # Update a range of workouts on a plan. Currently only hide_from_athlete can be changed
        api_response = api_instance.update_plan_workouts(id, folder_id, oldest, newest, workout)
        print("The response of LibraryApi->update_plan_workouts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->update_plan_workouts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **folder_id** | **int**|  | 
 **oldest** | **int**|  | 
 **newest** | **int**|  | 
 **workout** | [**Workout**](Workout.md)|  | 

### Return type

[**List[Workout]**](Workout.md)

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

# **update_workout**
> Workout update_workout(id, workout_id, workout_ex)

Update a workout

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.workout import Workout
from intervals_icu_client.models.workout_ex import WorkoutEx
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
    api_instance = intervals_icu_client.LibraryApi(api_client)
    id = 'id_example' # str | 
    workout_id = 56 # int | 
    workout_ex = intervals_icu_client.WorkoutEx() # WorkoutEx | 

    try:
        # Update a workout
        api_response = api_instance.update_workout(id, workout_id, workout_ex)
        print("The response of LibraryApi->update_workout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->update_workout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **workout_id** | **int**|  | 
 **workout_ex** | [**WorkoutEx**](WorkoutEx.md)|  | 

### Return type

[**Workout**](Workout.md)

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

