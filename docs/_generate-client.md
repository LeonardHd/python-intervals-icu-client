# Generate Client from OpenAPI spec

`docker run --rm -v "${PWD}:/local" --user "$(id -u):$(id -g)" openapitools/openapi-generator-cli generate -c /local/openapiconfig.json`