import requests
from os import environ

url = "https://api.meaningcloud.com/summarization-1.0"
input = open("input.txt","r+")
YOUR_TXT_VALUE = input.read()
YOUR_SENTENCES_VALUE = 2
YOUR_URL_VALUE = ''
YOUR_DOC_VALUE = ''
payload = 'key=21562aa114eb8acc65be61d10044ca84&txt=' + YOUR_TXT_VALUE + '&url=&doc=&sentences=' + str(YOUR_SENTENCES_VALUE)
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.request("POST", url, data=payload, headers=headers)

output = open("output.txt","w+")

output.write('SUMMARIZATION API TEST:')
output.write(response.text)
output.write('\n')
output.write('\n')

url = "https://api.meaningcloud.com/sentiment-2.1"
payload = 'key=21562aa114eb8acc65be61d10044ca84&lang=en&txt=' + YOUR_TXT_VALUE + '&txtf=plain&url=&doc='
response = requests.request("POST", url, data=payload, headers=headers)

response = response.text.rsplit('sentence_list', 1)
response = response[0].rsplit('score_tag', 1)

output.write("SENTIMENT ANALYSIS API TEST: ")
output.write(response[1])
output.write('\n')
output.write('\n')

url = "https://api.meaningcloud.com/topics-2.0"
payload = 'key=21562aa114eb8acc65be61d10044ca84&lang=en&txt=' + YOUR_TXT_VALUE + '&url=&doc=&&tt=a' 
response = requests.request("POST", url, data=payload, headers=headers)
output.write("TOPICS ANALYSIS API TEST: ")
output.write(response.text)