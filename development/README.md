# Development Documentation

## Preparing Code Generation

1. Download the OpenAPI specification file from the API provider.

    `curl -o openapi.json https://intervals.icu/api/v1/docs`

2. Convert the JSON specification to YAML format for easier readability.

    `yq -p json -o yaml openapi.json >| openapi.yaml`

3. Generate Client from OpenAPI spec

    `docker run --rm -v "${PWD}:/local" --user "$(id -u):$(id -g)" openapitools/openapi-generator-cli generate -c /local/openapiconfig.json`
