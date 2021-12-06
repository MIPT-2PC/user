# swagger-client
This is MIPT-2PC preprocessor API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InteractionApi(swagger_client.ApiClient(configuration))

try:
    # hello message to get preprocessed data
    api_response = api_instance.get_table()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_table: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.InteractionApi(swagger_client.ApiClient(configuration))
body = swagger_client.Table() # Table | Nums request body (optional)

try:
    # start preprocessing procedure
    api_response = api_instance.start2_pc(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->start2_pc: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8080/MIPT-2PC/preprocessor/1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*InteractionApi* | [**get_table**](docs/InteractionApi.md#get_table) | **GET** /getTable | hello message to get preprocessed data
*InteractionApi* | [**start2_pc**](docs/InteractionApi.md#start2_pc) | **POST** /start2PC | start preprocessing procedure

## Documentation For Models

 - [Table](docs/Table.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

mipt@mipt.ru