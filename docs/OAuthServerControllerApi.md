# intervals_icu_client.OAuthServerControllerApi

All URIs are relative to *https://intervals.icu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disconnect_app**](OAuthServerControllerApi.md#disconnect_app) | **DELETE** /api/v1/disconnect-app | Disconnect the athlete from the app matching the bearer token


# **disconnect_app**
> disconnect_app()

Disconnect the athlete from the app matching the bearer token

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
    api_instance = intervals_icu_client.OAuthServerControllerApi(api_client)

    try:
        # Disconnect the athlete from the app matching the bearer token
        api_instance.disconnect_app()
    except Exception as e:
        print("Exception when calling OAuthServerControllerApi->disconnect_app: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**401** | Missing or invalid access token |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

