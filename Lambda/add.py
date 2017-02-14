'''
  Name: Paul Talaga
  Date: Feb 14, 2017
  Desc: Demo of a simple lambda function to add two number given
  	as get parameters 'a', and 'b'.  Returns the result as a json
  	response.
'''

from __future__ import print_function

import json


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    This adds the 'a' and 'b' parameters together and returns the result.
    '''


    operation = event['httpMethod']
    if operation == 'GET' and 'a' in event['queryStringParameters'] and 'b' in event['queryStringParameters']:
        payload = event['queryStringParameters']
        return respond(None,  int(payload['a']) + int(payload['b']))
    else:
        return respond(ValueError('Unsupported method "%s" or a or b not present.' % (operation)))
