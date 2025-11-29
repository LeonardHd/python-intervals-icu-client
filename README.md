# python-intervals-icu-client

A Python client library for the Intervals.icu API.

> NOTE: This client is in early development and not published to PyPI yet.
> You can install it directly from the GitHub repository as described below.
> Most functionality should work, but most of the endpoints have not been
> tested yet.
> Check `tests/functional` and `tests/integration` for examples of usage.

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

Install directly from the GitHub repository using `pip`:

```sh
pip install git+https://github.com/LeonardHd/python-intervals-icu-client.git
```

Then import the package:
```python
import intervals_icu_client
```

### Example usage

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    activity = intervals_icu_client.Activity() # Activity | 

    try:
        # Create a manual activity
        api_response = api_instance.create_manual_activity(id, activity)
        print("The response of ActivitiesApi->create_manual_activity:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ActivitiesApi->create_manual_activity: %s\n" % e)

```
