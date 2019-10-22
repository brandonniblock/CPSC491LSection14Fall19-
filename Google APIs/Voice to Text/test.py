import io # for reading file
import os # for key in environment variable

# import Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# instantiate client
client = speech.SpeechClient()

# name of audio file
file_name = 'in.wav'
'''
file_name = os.path.join (
    os.path.dirname(__file__),
    'resources',
    'audio.raw')
'''

# load audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    # encoding=enums.RecognitionConfig.AudioEncoding.XYZ
    # https://cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig#AudioEncoding
    sample_rate_hertz=44100,
    language_code='en_US')

# detect speech in audio file
response = client.recognize(config, audio)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
