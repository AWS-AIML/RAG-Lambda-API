
Project Link : https://www.youtube.com/watch?v=EPq0x2qJZW8&list=PLhO5H_NFddjueCXRO7YGdVxz03lK_tV6I&index=3


Step 1 : Create S3 Bucket if not already created

Step 2 : Upload the documents in S3 Bucket

Step 3 : Create Knowledgebase  in Bedrock

    Step 3.1 : Select S3 as Data source
    Step 3.2 : Select Embedding model e.g. Amazon Titan or any other
    Step 3.3 : Select Vector Database/Store e.g. Opensearch or Aurora
    Step 3.4 : Sync knowledgebase with Data source
Step 4 : Create Lambda Function

    Step 4.1 : Copy code in lambda_fuction.py file
    Step 4.2 : Copy "Knowledge base ID" and "Foundation Model ARN from created knowledgebase and Foundation model you want to use 
    Step 4.3 : Define "KNOWLEDGE_BASE_ID" and "FM_ARN" in Environment variabled in Lambda -> Configuration -> Environment variables
Step 5 : Add Bedrock Access policy to lambda execution role

Step 6 : Test the Lambda fuction

Step 7 : Create a REST API in API Gateway

    Step 7.1 : Create Resource for REST API
    Step 7.2 : Create Post method for Lambda function in REST API
    Step 7.3 : Test API with Lambda
    Step 7.4 : Deploy API
Step 8 : Take Invoke url from API Gateway and add it to application

Step 9 : Run the application using 'streamlit run serverless_chatbot.py' command
