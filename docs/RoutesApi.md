# intervals_icu_client.RoutesApi

All URIs are relative to *https://intervals.icu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_merge**](RoutesApi.md#check_merge) | **GET** /api/v1/athlete/{id}/routes/{route_id}/similarity/{other_id} | How similar is this route to another?
[**get_athlete_route**](RoutesApi.md#get_athlete_route) | **GET** /api/v1/athlete/{id}/routes/{route_id} | Get a route for an athlete
[**list_athlete_routes**](RoutesApi.md#list_athlete_routes) | **GET** /api/v1/athlete/{id}/routes | List routes for an athlete with activity counts
[**update_athlete_route**](RoutesApi.md#update_athlete_route) | **PUT** /api/v1/athlete/{id}/routes/{route_id} | Update a route for an athlete


# **check_merge**
> RouteSimilarity check_merge(id, route_id, other_id)

How similar is this route to another?

Returned routes include path information

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.route_similarity import RouteSimilarity
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
    api_instance = intervals_icu_client.RoutesApi(api_client)
    id = 'id_example' # str | 
    route_id = 56 # int | 
    other_id = 56 # int | 

    try:
        # How similar is this route to another?
        api_response = api_instance.check_merge(id, route_id, other_id)
        print("The response of RoutesApi->check_merge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutesApi->check_merge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **route_id** | **int**|  | 
 **other_id** | **int**|  | 

### Return type

[**RouteSimilarity**](RouteSimilarity.md)

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

# **get_athlete_route**
> AthleteRoute get_athlete_route(id, route_id, include_path=include_path)

Get a route for an athlete

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.athlete_route import AthleteRoute
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
    api_instance = intervals_icu_client.RoutesApi(api_client)
    id = 'id_example' # str | 
    route_id = 56 # int | 
    include_path = False # bool | Include latlngs for the route GPS path (optional) (default to False)

    try:
        # Get a route for an athlete
        api_response = api_instance.get_athlete_route(id, route_id, include_path=include_path)
        print("The response of RoutesApi->get_athlete_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutesApi->get_athlete_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **route_id** | **int**|  | 
 **include_path** | **bool**| Include latlngs for the route GPS path | [optional] [default to False]

### Return type

[**AthleteRoute**](AthleteRoute.md)

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

# **list_athlete_routes**
> List[WithCount] list_athlete_routes(id)

List routes for an athlete with activity counts

The path (latlngs) is not included

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.with_count import WithCount
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
    api_instance = intervals_icu_client.RoutesApi(api_client)
    id = 'id_example' # str | 

    try:
        # List routes for an athlete with activity counts
        api_response = api_instance.list_athlete_routes(id)
        print("The response of RoutesApi->list_athlete_routes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutesApi->list_athlete_routes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[WithCount]**](WithCount.md)

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

# **update_athlete_route**
> AthleteRoute update_athlete_route(id, route_id, athlete_route)

Update a route for an athlete

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.athlete_route import AthleteRoute
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
    api_instance = intervals_icu_client.RoutesApi(api_client)
    id = 'id_example' # str | 
    route_id = 56 # int | 
    athlete_route = intervals_icu_client.AthleteRoute() # AthleteRoute | 

    try:
        # Update a route for an athlete
        api_response = api_instance.update_athlete_route(id, route_id, athlete_route)
        print("The response of RoutesApi->update_athlete_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutesApi->update_athlete_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **route_id** | **int**|  | 
 **athlete_route** | [**AthleteRoute**](AthleteRoute.md)|  | 

### Return type

[**AthleteRoute**](AthleteRoute.md)

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

