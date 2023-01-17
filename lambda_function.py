import json
import os
import mercadopago


def lambda_handler(event, context):
    
    sdk = mercadopago.SDK(os.environ["TEST_TOKEN"])
    
    #sdk = mercadopago.SDK('TEST-4608637268612593-011411-3fb888d3153d51fde9282a9446353594-1284819494')
    
    bodyGet = json.loads(event["body"])
    
    preference_response = sdk.payment().create(bodyGet)
    preference = preference_response["response"]

    return {
        "statusCode": 200,
        "body": json.dumps(
            preference
        ),
    }