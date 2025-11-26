# intervals_icu_client.ChatsApi

All URIs are relative to *https://intervals.icu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_message**](ChatsApi.md#delete_message) | **DELETE** /api/v1/chats/{id}/messages/{msgId} | Delete a message
[**list_activity_messages**](ChatsApi.md#list_activity_messages) | **GET** /api/v1/activity/{id}/messages | List all messages (comments) for the activity
[**list_chats**](ChatsApi.md#list_chats) | **GET** /api/v1/athlete/{id}/chats | List chats for the athlete, most recently active first
[**list_messages**](ChatsApi.md#list_messages) | **GET** /api/v1/chats/{id}/messages | List messages for the chat, most recent first
[**send_activity_message**](ChatsApi.md#send_activity_message) | **POST** /api/v1/activity/{id}/messages | Add a message (comment) to an activity
[**send_message**](ChatsApi.md#send_message) | **POST** /api/v1/chats/send-message | Send a message
[**show_chat**](ChatsApi.md#show_chat) | **GET** /api/v1/chats/{id} | Get a chat by id
[**update_last_seen_message_id**](ChatsApi.md#update_last_seen_message_id) | **PUT** /api/v1/chats/{id}/messages/{msgId}/seen | Update last seen message for the chat


# **delete_message**
> object delete_message(id, msg_id)

Delete a message

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
    api_instance = intervals_icu_client.ChatsApi(api_client)
    id = 56 # int | 
    msg_id = 56 # int | 

    try:
        # Delete a message
        api_response = api_instance.delete_message(id, msg_id)
        print("The response of ChatsApi->delete_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->delete_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **msg_id** | **int**|  | 

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

# **list_activity_messages**
> List[Message] list_activity_messages(id, since_id=since_id, limit=limit)

List all messages (comments) for the activity

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.message import Message
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
    api_instance = intervals_icu_client.ChatsApi(api_client)
    id = 'id_example' # str | 
    since_id = 56 # int |  (optional)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List all messages (comments) for the activity
        api_response = api_instance.list_activity_messages(id, since_id=since_id, limit=limit)
        print("The response of ChatsApi->list_activity_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->list_activity_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **since_id** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[Message]**](Message.md)

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

# **list_chats**
> List[Chat] list_chats(id)

List chats for the athlete, most recently active first

Only returns activity chats that have new_msg_count > 0 or that have been updated recently

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.chat import Chat
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
    api_instance = intervals_icu_client.ChatsApi(api_client)
    id = 'id_example' # str | 

    try:
        # List chats for the athlete, most recently active first
        api_response = api_instance.list_chats(id)
        print("The response of ChatsApi->list_chats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->list_chats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[Chat]**](Chat.md)

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

# **list_messages**
> List[Message] list_messages(id, before_id=before_id, limit=limit)

List messages for the chat, most recent first

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.message import Message
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
    api_instance = intervals_icu_client.ChatsApi(api_client)
    id = 56 # int | 
    before_id = 56 # int | Only return messages older than this one (optional)
    limit = 56 # int | Return up to this many messages (default 30, max 100) (optional)

    try:
        # List messages for the chat, most recent first
        api_response = api_instance.list_messages(id, before_id=before_id, limit=limit)
        print("The response of ChatsApi->list_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->list_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **before_id** | **int**| Only return messages older than this one | [optional] 
 **limit** | **int**| Return up to this many messages (default 30, max 100) | [optional] 

### Return type

[**List[Message]**](Message.md)

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

# **send_activity_message**
> NewMsg send_activity_message(id, new_activity_msg)

Add a message (comment) to an activity

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.new_activity_msg import NewActivityMsg
from intervals_icu_client.models.new_msg import NewMsg
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
    api_instance = intervals_icu_client.ChatsApi(api_client)
    id = 'id_example' # str | 
    new_activity_msg = intervals_icu_client.NewActivityMsg() # NewActivityMsg | 

    try:
        # Add a message (comment) to an activity
        api_response = api_instance.send_activity_message(id, new_activity_msg)
        print("The response of ChatsApi->send_activity_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->send_activity_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **new_activity_msg** | [**NewActivityMsg**](NewActivityMsg.md)|  | 

### Return type

[**NewMsg**](NewMsg.md)

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

# **send_message**
> SendResponse send_message(new_message)

Send a message

Returns the new message id. If a new chat was created then it is also returned.

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.new_message import NewMessage
from intervals_icu_client.models.send_response import SendResponse
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
    api_instance = intervals_icu_client.ChatsApi(api_client)
    new_message = intervals_icu_client.NewMessage() # NewMessage | 

    try:
        # Send a message
        api_response = api_instance.send_message(new_message)
        print("The response of ChatsApi->send_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->send_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_message** | [**NewMessage**](NewMessage.md)|  | 

### Return type

[**SendResponse**](SendResponse.md)

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

# **show_chat**
> Chat show_chat(id)

Get a chat by id

### Example

* Basic Authentication (APIKey):
* Bearer Authentication (AccessToken):

```python
import intervals_icu_client
from intervals_icu_client.models.chat import Chat
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
    api_instance = intervals_icu_client.ChatsApi(api_client)
    id = 56 # int | 

    try:
        # Get a chat by id
        api_response = api_instance.show_chat(id)
        print("The response of ChatsApi->show_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->show_chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Chat**](Chat.md)

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

# **update_last_seen_message_id**
> object update_last_seen_message_id(id, msg_id)

Update last seen message for the chat

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
    api_instance = intervals_icu_client.ChatsApi(api_client)
    id = 56 # int | 
    msg_id = 56 # int | 

    try:
        # Update last seen message for the chat
        api_response = api_instance.update_last_seen_message_id(id, msg_id)
        print("The response of ChatsApi->update_last_seen_message_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->update_last_seen_message_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **msg_id** | **int**|  | 

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

