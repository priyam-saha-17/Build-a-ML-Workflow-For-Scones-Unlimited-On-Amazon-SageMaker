"""
Lambda Function 2: imageClassifier

A lambda function that is responsible for the classification part. It takes the image output from the 
lambda 1 function, decodes it, and then pass inferences back to the the Step Function
"""



import json
import base64
import boto3

# Using low-level client representing Amazon SageMaker Runtime ( To invoke endpoint)
runtime_client = boto3.client('sagemaker-runtime')                   


# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2023-11-07-07-53-38-912" ## TODO: fill in (Trained IC Model Name)


def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])     ## TODO: fill in (Decoding the encoded 'Base64' image-data and class remains'bytes')

    # Instantiate a Predictor (Here we have renamed 'Predictor' to 'response')
    # Response after invoking a deployed endpoint via SageMaker Runtime 
    response = runtime_client.invoke_endpoint(
                                        EndpointName=ENDPOINT,    # Endpoint Name
                                        Body=image,               # Decoded Image Data as Input (class:'Bytes') Image Data
                                        ContentType='image/png'   # Type of inference input data - Content type (Eliminates the need of serializer)
                                    )
                                    
    
    # Make a prediction: Unpack reponse
    # (NOTE: 'response' returns a dictionary with inferences in the "Body" : (StreamingBody needs to be read) having Content_type='string')
    
    ## TODO: fill in (Read and decode predictions/inferences to 'utf-8' & convert JSON string obj -> Python object)
    inferences = json.loads(response['Body'].read().decode('utf-8'))     # list
  
    
    # We return the data back to the Step Function    
    event['inferences'] = inferences            ## List of predictions               
    return {
        'statusCode': 200,
        'body': event                           ## Passing the event python dictionary in the body
    }

