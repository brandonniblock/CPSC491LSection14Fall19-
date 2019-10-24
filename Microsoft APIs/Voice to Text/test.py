import azure.cognitiveservices.speech as speechsdk

# Interestingly, there is a way to recognize straight from the mic with Microsoft
# https://github.com/Azure-Samples/cognitive-services-speech-sdk/blob/master/samples/python/console/speech_sample.py

# Create instance of speech config w/ key and region
# https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/regions
speech_key, service_region = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'westus2'
file_name = 'in.wav'
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
audio_config = speechsdk.audio.AudioConfig(filename=file_name)

# Create recognizer with config's settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

# Start speech recognition
# This only works up to 15sec, use start_continuous_recognition() for longer
result = speech_recognizer.recognize_once()

# Check result
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print('Recognized: {}'.format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print('No speech could be recognized: {}'.format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print('Speech Recognition cancelled: {}'.format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print('Error details: {}'.format(cancellation_details.error_details))
