from slack import RTMClient
from utils import fetch_reply


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
        web_client.chat_postMessage(channel=channel_id,
                                   text=reply.get('data'))


slack_token = 'xoxb-781825934963-780528215330-KFT40bsiyMYoHcALtkRTfUVb'

client = RTMClient(token = slack_token)

client.start()

#  thread_ts = data['ts'] thread_ts=thread_ts
#        web_client.chat_postMessage(channel=channel_id,
#                            text=f"Hi <@{user}>!")