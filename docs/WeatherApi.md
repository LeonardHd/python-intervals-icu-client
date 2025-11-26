# intervals_icu_client.WeatherApi

All URIs are relative to *https://intervals.icu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_forecast**](WeatherApi.md#get_forecast) | **GET** /api/v1/athlete/{id}/weather-forecast | Get weather forecast information
[**get_weather_config**](WeatherApi.md#get_weather_config) | **GET** /api/v1/athlete/{id}/weather-config | Get the athlete&#39;s weather forecast configuration
[**update_weather_config**](WeatherApi.md#update_weather_config) | **PUT** /api/v1/athlete/{id}/weather-config | Update the athlete&#39;s weather forecast configuration


# **get_forecast**
> WeatherDTO get_forecast(id)

Get weather forecast information

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.weather_dto import WeatherDTO
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
    api_instance = intervals_icu_client.WeatherApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get weather forecast information
        api_response = api_instance.get_forecast(id)
        print("The response of WeatherApi->get_forecast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeatherApi->get_forecast: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WeatherDTO**](WeatherDTO.md)

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

# **get_weather_config**
> WeatherConfig get_weather_config(id)

Get the athlete's weather forecast configuration

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.weather_config import WeatherConfig
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
    api_instance = intervals_icu_client.WeatherApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get the athlete's weather forecast configuration
        api_response = api_instance.get_weather_config(id)
        print("The response of WeatherApi->get_weather_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeatherApi->get_weather_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WeatherConfig**](WeatherConfig.md)

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

# **update_weather_config**
> WeatherConfig update_weather_config(id, weather_config)

Update the athlete's weather forecast configuration

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.weather_config import WeatherConfig
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
    api_instance = intervals_icu_client.WeatherApi(api_client)
    id = 'id_example' # str | 
    weather_config = intervals_icu_client.WeatherConfig() # WeatherConfig | 

    try:
        # Update the athlete's weather forecast configuration
        api_response = api_instance.update_weather_config(id, weather_config)
        print("The response of WeatherApi->update_weather_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeatherApi->update_weather_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **weather_config** | [**WeatherConfig**](WeatherConfig.md)|  | 

### Return type

[**WeatherConfig**](WeatherConfig.md)

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

