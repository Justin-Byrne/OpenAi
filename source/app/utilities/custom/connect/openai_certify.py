import openai

def openai_certify ( API_ORG, API_KEY ):

	openai.organization = API_ORG

	openai.api_key 		= API_KEY


	return openai
