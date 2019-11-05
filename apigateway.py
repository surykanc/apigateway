import boto3
import json
import sys


if len(sys.argv) == 1:
    print("Usage : " + sys.argv[0] + " region profile APIGatewayName [info methods keys authorization] [json csv]")
    sys.exit()
session = boto3.Session(profile_name=sys.argv[2])
client = session.client('apigateway',region_name=sys.argv[1])


def info_json(APIGatewayName):
    response = client.get_rest_apis()
    apis=response.get("items")
    for api in apis:
        if api.get("name") == APIGatewayName:
            apiJson={'apiName':api.get("name"),'apiId':api.get("id"),'description':api.get("description"),'createdDate':api.get("createdDate"),'apiKeySource':api.get("apiKeySource")}
    return apiJson        

def details_json(APIGatewayName):
    response = client.get_rest_apis()
    apis=response.get("items")
    for api in apis:
        if api.get("name") == APIGatewayName:
            apiId=api.get("id")
    resources = client.get_resources(restApiId=apiId)
    return resources.get("items")

def ApiKeys_json():
    response = client.get_api_keys()
    return response.get("items")

def authorization_json(APIGatewayName):
    response = client.get_rest_apis()
    apis=response.get("items")
    for api in apis:
        if api.get("name") == APIGatewayName:
            apiId=api.get("id")
    response = client.get_authorizers(
    restApiId=apiId,
    )
    return response.get("items")
if sys.argv[4] == "info":
    if sys.argv[5] == "json":
        info=info_json(sys.argv[3])
        print(info)

if sys.argv[4] == "methods":
     if sys.argv[5] == "json":
         resourceInfo=details_json(sys.argv[3])
         print(resourceInfo)

if sys.argv[4] == "keys":
     if sys.argv[5] == "json":
         keyInfo=ApiKeys_json()
         print(keyInfo)  

if sys.argv[4] == "authorization":
     if sys.argv[5] == "json":
         authorizationInfo=authorization_json(sys.argv[3])
         print(authorizationInfo)  