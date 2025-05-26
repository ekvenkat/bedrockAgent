import boto3
import os
import json
import logging
import pprint

bedrock = boto3.client(
    service_name="bedrock",
    region_name=os.environ.get("AWS_REGION", "us-east-1")
)

pp = pprint.PrettyPrinter(depth=4)

def list_foundation_models():
    models = bedrock.list_foundation_models();
    for model in models["modelSummaries"]:
        pp.pprint(model);
        pp.pprint("------------------")

def get_foundation_model(model_id):
    pp.pprint("Getting model: " + model_id);
    # Get the model
    model = bedrock.get_foundation_model(modelIdentifier=model_id)  # Corrected parameter name
    pp.pprint(model)
    pp.pprint("------------------")


list_foundation_models()
get_foundation_model('meta.llama3-2-3b-instruct-v1:0')