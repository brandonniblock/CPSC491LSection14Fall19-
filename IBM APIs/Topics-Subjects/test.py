import io # for reading file
import json # for printing json

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12', # what are the possible 'versions'?
    iam_apikey='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    url='https://gateway.watsonplatform.net/natural-language-understanding/api'
)
file_name = 'in.txt'
with io.open(file_name, 'r') as in_file:
    text = in_file.read()

response = natural_language_understanding.analyze(
    text=text,
    features=Features(
        entities=EntitiesOptions()
    )
).get_result()

# need all this encode decode stuff because otherwise dumps() prints \u4e0b\u95a2
print(json.dumps(response, indent=2, ensure_ascii=False).encode('utf8').decode())
