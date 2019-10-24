import io # for reading file
import os # for key in environment variable

from google.cloud import language_v1
from google.cloud.language_v1 import enums

client = language_v1.LanguageServiceClient()

file_name = 'in.txt'
with io.open(file_name, 'r') as in_file:
    text_content = in_file.read()

# available types: PLAIN_TEXT, HTML
type_ = enums.Document.Type.PLAIN_TEXT

# optional (if not specified, automatically detected)
# languages: https://cloud.google.com/natural-language/docs/languages
language = 'en'
document = {'content': text_content, 'type': type_, 'language': language}

# available values: NONE, UTF8, UTF16, UTF32
encoding_type = enums.EncodingType.UTF8

response = client.analyze_entities(document, encoding_type=encoding_type)
# loop through entities returned from API
for entity in response.entities:
    print(u'Representative name for the entity: {}'.format(entity.name))
    # get entity type, ex. PERSON, LOCATION, ADDRESS, NUMBER, etc.
    print(u'Entity type: {}'.format(enums.Entity.Type(entity.type).name))
    # get salience score, range [0, 1.0]
    print(u'Salience score: {}'.format(entity.salience))
    # loop over metadata for entity
    # usually Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid)
    # sometimes others (ex. ADDRESS entity has street_name, postal_code, etc.)
    for metadata_name, metadata_value in entity.metadata.items():
        print(u'{}: {}'.format(metadata_name, metadata_value))
    
    # loop over mentions of this entity in input document
    # proper nouns supported
    for mention in entity.mentions:
        print(u'Mention text: {}'.format(mention.text.content))
        # get mention type (ex. PROPER = proper noun)
        print (
            u'Mention type: {}'.format(enums.EntityMention.Type(mention.type).name)
        )

# get language of text (what I specified or what was detected if not)
print(u'Language of text: {}'.format(response.language))
