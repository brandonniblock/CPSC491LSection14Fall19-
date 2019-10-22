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
file_name = 'in-jp.txt'
with io.open(file_name, 'r') as in_file:
    text = in_file.read()

# pack and send for analysis
# https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/language-support
documents = [
    {
        'id': '1',
        'language': 'ja',
        'text': text
    }
]
response = text_analytics.entities(documents=documents)

# loop through entities returned from API
# score = confidence
for document in response.documents:
    print('Document ID: ', document.id)
    print('\tKey Entities:')
    for entity in document.entities:
        print('\t\t', 'NAME: ', entity.name, '\tType: ',
              entity.type, '\tSub-type: ', entity.sub_type)
        for match in entity.matches:
            print('\t\t\tOffset: ', match.offset, '\tLength: ', match.length,
                  '\tScore: ', '{:.2f}'.format(match.entity_type_score))
