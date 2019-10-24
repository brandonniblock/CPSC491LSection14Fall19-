import time
import logging
from flask import Flask, request, render_template, jsonify
import uuid
import boto3
from botocore.exceptions import ClientError
import json
import requests

app = Flask(__name__)

@app.route("/")
def upload():
	return send_from_directory('fullstack_template/static', 'index.html', asattachment=True)

@app.route("/analyze/<job_name>", methods=['GET'])
def analyze(job_name):
    comprehend = boto3.client('comprehend', region_name='us-east-1')
    transcription = get_transcription_results(job_name)
    sentiment_results = comprehend.detect_sentiment(Text = transcription, LanguageCode='en')
    key_phrase_results = comprehend.detect_key_phrases(Text = transcription, LanguageCode = 'en')
    entity_results = comprehend.detect_entities(Text = transcription, LanguageCode = 'en')
    
    sentiment = sentiment_results["Sentiment"]
    sentiment_score = sentiment_results["SentimentScore"]
    key_phrases = key_phrase_results["KeyPhrases"]
    entities = entity_results["Entities"]
    print(entity_results)
    
    return render_template("display_analysis.html", sentiment=sentiment, sentiment_score = sentiment_score,
            key_phrases = key_phrases, entities = entities)
    
    
@app.route('/jobs', methods = ['GET'])
def jobs():
        transcribe = boto3.client('transcribe', region_name='us-east-1')
        response = transcribe.list_transcription_jobs()
        response = (response.get('TranscriptionJobSummaries'))
        return render_template("display_transcription_list.html", response = response)

@app.route("/jobs/<job_name>", methods=['GET'])
def get_job(job_name):
    transcript = get_transcription_results(job_name)
    return render_template("display_transcription.html", transcript=transcript, transcript_name = job_name)        
        
@app.route('/success', methods = ['POST'])
def success():
    s3 = boto3.client('s3')
    if request.method == 'POST':
        f = request.files['file']
        file_path = "uploads/" + f.filename
        f.save(file_path)
        s3.upload_file(file_path, 'nlp-harness', file_path)
        start_transcription(f.filename)
    return render_template("success.html", name = f.filename)

def start_transcription(file_name):
    transcribe = boto3.client('transcribe', region_name='us-east-1')
    job_name = "transcribe_job_" + file_name
    job_uri = "https://nlp-harness.s3.amazonaws.com/uploads/" + file_name
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri':job_uri},
        MediaFormat='mp3',
        LanguageCode='en-US'
    )
        
def get_transcription_results(job_name):
    transcribe = boto3.client('transcribe', region_name='us-east-1')
    job = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    job = job["TranscriptionJob"]["Transcript"]["TranscriptFileUri"]
    job = requests.get(job)  

    job = job.json()["results"]["transcripts"][0]["transcript"]
    return job

if __name__ == "__main__":
    app.run(host="0.0.0.0")
