import io # for reading file
import os # for key in environment variable

from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

# get API key from environment
key_var_name = 'TEXT_ANALYTICS_SUBSCRIPTION_KEY'
if not key_var_name in os.environ:
    raise Exception('Set/export environment variable: {}'.format(key_var_name))
subscription_key = os.environ[key_var_name]

# get endpoint from environment
endpoint_var_name = 'TEXT_ANALYTICS_ENDPOINT'
if not endpoint_var_name in os.environ:
    raise Exception('Set/export environment variable: {}'.format(endpoint_var_name))
endpoint = os.environ[endpoint_var_name]

# set credentials object
credentials = CognitiveServicesCredentials(subscription_key)

# authenticate client
text_analytics = TextAnalyticsClient(endpoint=endpoint, credentials=credentials)

# get text from file
file_name = 'in-positive.txt'
with io.open(file_name, 'r') as in_file:
    text = in_file.read()

# pack and send for analysis
documents = [
    {
        'id': '1',
        'language': 'en',
        'text': text
    }
]
response = text_analytics.sentiment(documents=documents)

# score [0.0, 1.0] - negative to positive sentiment
for document in response.documents:
    print('Document ID: ', document.id,
          ', Sentiment Store: ', '{:.2f}'.format(document.score))
