import json
import logging

logger = logging.getLogger()
logger.setLevel("INFO")

def lambda_handler(event, context):
    logger.info("Event received: %s", json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps('Log processed successfully')
    }
