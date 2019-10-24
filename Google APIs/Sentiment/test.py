import io # for reading file
import os # for key in environment variable

# import Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# instantiate client
client = language.LanguageServiceClient()

# text to analyze
'''
text = u'Hello, world!'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)
'''
file_name = 'in-positive.txt'
with io.open(file_name, 'r') as in_file:
    content = in_file.read()
document = types.Document(
    content=content,
    type=enums.Document.Type.PLAIN_TEXT)

# detect sentiment
# score [-1.0, 1.0] - emotion
# magnitide [0.0, +inf) - strength of emotion
# https://cloud.google.com/natural-language/docs/basics#interpreting_sentiment_analysis_values
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Text: {}'.format(content))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
