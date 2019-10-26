from slack import RTMClient
from utils import fetch_reply
import json
import time

HELP_MSG = """
Hey! I am ScoreBot. 
I can provide you score,result,table from all around the worlds leagues :)
This app will show you today result and fixture.
"""

@RTMClient.run_on(event="message")
def say_hello(**payload):
    data = payload['data']
    web_client = payload['web_client']
    text = data.get('text')
    subtype = data.get('subtype')
    if subtype is None and text:
        channel_id = data['channel']
        user = data['user']
        client_msg_id = data['client_msg_id']
        reply = fetch_reply(text,client_msg_id)
        
        if reply['type'] == 'playerranking':
            data = json.loads(reply['data'])
            string = 'Rank\tName\n'
            for i in data:
                string += f'{i[0]}\t{i[1]}\n'
            web_client.chat_postMessage(channel=channel_id,
                                       text=string)
        if reply['type'] == 'resulttoday':
            data = json.loads(reply['data'])
            if data['result'] == 'success':
                string = ''
                for i in data['content']:
                    match = i['match']
                    link = i['link']
                    string += f'{match}\t{link}\n'
                web_client.chat_postMessage(channel=channel_id,
                                           text=string)
            else:
                web_client.chat_postMessage(channel=channel_id,
                                           text='Sorry :( ,not able to find it.')
        if reply['type'] == 'scorer':
            data = json.loads(reply['data'])
            if data['result'] == 'success':
                string = f'Name\t\tTeam\tGoals\tAssist\n'
                for i in data['content']:
                    string += f'{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\n'
                web_client.chat_postMessage(channel=channel_id,
                                           text=string)
            else:
                web_client.chat_postMessage(channel=channel_id,
                                          text='Sorry :( ,not able to find it.')
        if reply['type'] == 'points_table':
            data = json.loads(reply['data'])
            if data['result'] == 'success':
                string = 'pos\tName\t\tP\tGd\tPts\n'
                for i in data['content']:
                    
                    string += f'{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\n'
                web_client.chat_postMessage(channel=channel_id,
                                       text=string)
            else:
                web_client.chat_postMessage(channel=channel_id,
                                       text='Sorry :( ,not able to find it.')
        else:
            web_client.chat_postMessage(channel=channel_id,
                                        text=reply.get('data') )

# Slack token for bot
slack_token = 'xoxb-781825934963-802377960161-dt6FR10wrIcwX0buQcGT4vV1'

client = RTMClient(token = slack_token,connect_method='rtm.start'
)
try:
    client.start()
except:
    client.start()
#  thread_ts = data['ts'] thread_ts=thread_ts
#        web_client.chat_postMessage(channel=channel_id,
#                            text=f"Hi <@{user}>!")