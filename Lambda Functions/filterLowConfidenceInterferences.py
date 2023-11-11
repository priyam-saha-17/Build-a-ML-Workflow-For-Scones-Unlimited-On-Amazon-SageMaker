"""
Lambda Function 3: filterLowConfidenceInferences

A lambda function that takes the inferences from the Lambda 2 function output and filters low-confidence inferences
(above a certain threshold indicating success)
"""




import json


THRESHOLD = .7


def lambda_handler(event, context):
    
    # Grab the inferences from the event
    inferences = event['body']['inferences']
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = max(list(inferences))>THRESHOLD 
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }