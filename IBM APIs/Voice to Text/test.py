import io # for reading file
import json # for printing json

from ibm_watson import SpeechToTextV1

speech_to_text = SpeechToTextV1(
    iam_apikey='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    url='https://stream.watsonplatform.net/speech-to-text/api'
)
file_name = "in.wav"

with io.open(file_name, 'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/wav'#,
        #word_alternatives_threshold=0.85
    ).get_result()
print(json.dumps(speech_recognition_results, indent=2))
