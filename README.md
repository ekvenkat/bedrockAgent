Introduction:
Interface to AI models hosted on AWS. The access can be provisioned (expensive) or server less (on demand)
Model Providers
- Amazon
- AI21 labs
- Anthrophic
- Meta
- Cohere
- Stability AI
- Mistral AI


AI Models:
Programs that detect specific patterns using a collection of data sets
Once trained, an AI model can be used to make future predictions or act on data that was not previously observed
* Text Generation based on a prompt (Text to Text)
* Image generation based on a prompt (Text to Image)
* Text tasks - Summary, translation, spelling check, system check
* Anomaly detection
* Recommender systems
* Speech
* Video

IAM user creation for Amazon Bedrock - Credentials and access key

Bedrock API - Boto3 - Python
Steps:
1. Create virtual environment
python3 -m venv .venv
2. Activate virtual environment
source .venv/bin/activate
3. Install boto3 - Python SDK for AWS
4. Create Requirements file
pip install -r requirements.txt
5. Create sample boto3 bedrock call script

Bedrock text models:
Text model intro
Model parameters
Text generation using the SDK - PY and TS
