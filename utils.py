import apiai
import json

# api.ai client 
APIAI_ACCESS_TOKEN = "ef4ddbe4120d45ee99b53c35afa97a62"
ai = apiai.ApiAI(APIAI_ACCESS_TOKEN)


HELP_MSG = """
Hey! I am ScoreBot. 
I can provide you score,result,table from all around the worlds leagues :)
This app will show you today result and fixture.
"""

def apiai_response(query, session_id):
	"""
	function to fetch api.ai response
	"""
	request = ai.text_request()
	request.lang = 'en'
	request.session_id = session_id
	request.query = query
	response = request.getresponse()
	return json.loads(response.read().decode('utf8'))


def parse_response(response):
	"""
	function to parse response and 
	return intent and its parameters
	"""
	result = response['result']
	params = result.get('parameters')
	intent = result['metadata'].get('intentName')
	return intent, params

	
def fetch_reply(query, session_id):
    response = apiai_response(query, session_id)
    intent, params = parse_response(response)
    reply = {}
    print('RESPONSE')
    print(response)
    if response['result']['action'].startswith('smalltalk'):
        reply['type'] = 'smalltalk'
        reply['data'] = response['result']['fulfillment']['speech']
    return reply
