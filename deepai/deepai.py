import requests
from requests import *

sentimentAnalysisText = 'Sometimes I’ll start a sentence, and I don’t even know where it’s going. I just hope I find it along the way'

textSummarizationAndTagging = 'He picked up the children’s history book and looked at the portrait of Big Brother which formed its frontispiece. The hypnotic eyes gazed into his own. It was as though some huge force were pressing down upon you—something that penetrated inside your skull, battering against your brain, frightening you out of your beliefs, persuading you, almost, to deny the evidence of your senses. In the end the Party would announce that two and two made five, and you would have to believe it. It was inevitable that they should make that claim sooner or later: the logic of their position demanded it. Not merely the validity of experience, but the very existence of external reality, was tacitly denied by their philosophy. The heresy of heresies was common sense. And what was terrifying was not that they would kill you for thinking otherwise, but that they might be right. For, after all, how do we know that two and two make four? Or that the force of gravity works? Or that the past is unchangeable? If both the past and the external world exist only in the mind, and if the mind itself is controllable what then?'

textSummarizationAndTagging2 = 'Previous question has been moved and seconded. As you know, a motion for previous question, if passed by a two-thirds vote, will cut off further debate and require us to vote yes or no on the resolution before us. You should vote for this motion if you wish to cut off further debate of the wheel tax increase at this point. Will all those in favor of previous question please raise your hand? Will all those against please raise your hand? The vote is 17-2. Previous question passes. We are now on the motion to increase the wheel tax by $10 to make up the state cut in education funding. Will all those in favor please raise your hand? Will all those against please raise your hand? The vote is 17-2. This increase passes on first passage. Is there any other new business? Since no member is seeking recognition, are there announcements? Commissioner Hailey.'


#Sentiment analysis
a = requests.post(
    "https://api.deepai.org/api/sentiment-analysis",
    data={
        'text': sentimentAnalysisText,
    },
    headers={'api-key': 'a0dbb0aa-347e-4804-bbe0-e779d8984731'}
)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Text Summarization with DeepAI
b = requests.post(
    "https://api.deepai.org/api/summarization",
    data={
        'text': textSummarizationAndTagging,
    },
    headers={'api-key': 'a0dbb0aa-347e-4804-bbe0-e779d8984731'}
)
b2 = requests.post(
    "https://api.deepai.org/api/summarization",
    data={
        'text': textSummarizationAndTagging2,
    },
    headers={'api-key': 'a0dbb0aa-347e-4804-bbe0-e779d8984731'}
)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Text Tagging
c = requests.post(
    "https://api.deepai.org/api/text-tagging",
    data={
        'text': textSummarizationAndTagging,
    },
    headers={'api-key': 'a0dbb0aa-347e-4804-bbe0-e779d8984731'}
)
print('Sentiment analysis: ' + '\n')
print(a.json())
print('\n' + '~~~~~~~~~~')
print('Text summary: ' + '\n')
print(b.json())
print('\n' + '~~~~~~~~~~')
print('Text summary: ' + '\n')
print(b2.json())
print('\n' + '~~~~~~~~~~')
print('Text tagging: ' + '\n')
print(c.json())
print('\n' + '~~~~~~~~~~')
