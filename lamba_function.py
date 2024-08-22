import boto3

import json

def lambda_handler(event, context):
    # TODO implement
    
    runtime_client = boto3.client('runtime.sagemaker')
    
    endpoint_name = 'Employeeattritionendpoint'
    sample = '31,1,17,4,2,0,2,1,10310,0,3,1,89,1,60,0,0,0,3,0'
    response = runtime_client.invoke_endpoint(EndpointName ='EmployeeAttrition',
                                              ContentType = 'text/csv',
                                              Body=sample)
    result = response['Body'].read().decode('ascii')
    print(result)
    
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'body':result
    }