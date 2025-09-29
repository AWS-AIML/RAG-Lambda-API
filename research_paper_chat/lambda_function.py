

import os
import json
import boto3

# 2. Define Knowledge base - Foundation Model & Client Setup
service_name = "bedrock-agent-runtime"
client = boto3.client(service_name)

knowledge_base_id = os.getenv("KNOWLEDGE_BASE_ID")
fm_ARN = os.getenv("FM_ARN")

# 3. Define the Lambda function

def lambda_handler(event, context):
    
    # 3.1. Retrive User query/Question 
    user_query = event["user_query"]
    
    # 3.2. API call to "retrieve_and_generate" function
    client_knowledgebase = client.retrieve_and_generate(
        input = {
            "text" : user_query
        },
        retrieveAndGenerateConfiguration = {
            "type" : "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration" :  {
                "knowledgeBaseId" : knowledge_base_id,
                "modelArn" : fm_ARN
            }
        }
    )

    # 3.3. Citations - References and Final Response
    print("------------------ Reference Details ------------------")
    citations = client_knowledgebase["citations"]
    reference = citations[0]["retrievedReferences"][0]

    s3_location = reference["location"]["s3Location"]["uri"]

    generated_response = client_knowledgebase["output"]["text"]
    
    # 3.4. Final object to return
    body = {
        "statusCode" : 200,
        "query" : user_query,
        "answer" : generated_response,
        "reference" : s3_location
    }
    
    # 3.5. Print & Return Result
    print("Result Details : \n")
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"   # Needed for browser requests
        },
        "body": json.dumps(body)
    }