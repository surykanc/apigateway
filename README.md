# apigateway
##output
Usage apigateway.py region profile APIGatewayName [info methods keys authorization] [json csv]

python3 apigateway.py us-east-1 default PetStore info json
{'apiName': 'PetStore', 'apiId': 'drrgnz7vzc', 'description': 'Your first API with Amazon API Gateway. This is a sample API that integrates via HTTP with our demo Pet Store endpoints', 'createdDate': datetime.datetime(2019, 11, 4, 21, 18, 40, tzinfo=tzlocal()), 'apiKeySource': 'HEADER'}
note: it will provide the informtion about the petstore in json

python3 apigateway.py us-east-1 default PetStore methods  json
[{'id': '2jzz618k17', 'path': '/', 'resourceMethods': {'GET': {}}}, {'id': 'nutk36', 'parentId': '2jzz618k17', 'pathPart': 'pets', 'path': '/pets', 'resourceMethods': {'GET': {}, 'OPTIONS': {}, 'POST': {}}}, {'id': 'ru91qe', 'parentId': 'nutk36', 'pathPart': '{petId}', 'path': '/pets/{petId}', 'resourceMethods': {'GET': {}, 'OPTIONS': {}}}]
note: it will provide the informtion about the methods of particular of the petstore apigateway

python3 apigateway.py us-east-1 default PetStore keys  json
[{'id': 's1opgppfq4', 'name': 'surya123', 'enabled': True, 'createdDate': datetime.datetime(2019, 11, 4, 21, 22, 36, tzinfo=tzlocal()), 'lastUpdatedDate': datetime.datetime(2019, 11, 4, 21, 22, 36, tzinfo=tzlocal()), 'stageKeys': []}]
note: it will provide the informtion about the keys of particular of the petstore apigateway

python3 apigateway.py us-east-1 default PetStore authorization  json
[]
note: in this example the petstore apigateway doesn't have any authorization,so it is not secure

Important note: i'm unable to configure the authorization with the apigateway ,i also created the key and i don't know how to add the key in gateway

i don't have correct csv format ,so please let me know so that i can work on.
