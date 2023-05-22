from ..connect.openai_certify 	import openai_certify
from ..file.write_to_cache 		import write_to_cache
from .parse_models 				import parse_models
from .parse_model 				import parse_model

ERROR = -1

def fetch_models ( API_ORG, API_KEY, MODEL = None ):

	if MODEL:

		try:

			openai = openai_certify ( API_ORG, API_KEY )

			model   = openai.Model.retrieve ( MODEL )

		except:

			print ( '>> [ERROR] fetch_models.py\n\t~ Open AI connection failed !' )

			return ERROR


		model = parse_model ( model )


		final 					= model [ 'data' ]

		final [ 'permissions' ] = model [ 'permissions' ]


		if final:

			write_to_cache ( f"models/{final [ 'root' ]}", final, True )

			return True

	else:

		try:

			openai = openai_certify ( API_ORG, API_KEY )

			models = openai.Model.list ( )

		except:

			print ( '>> [ERROR] fetch_models.py\n\t~ Open AI connection failed !' )

			return ERROR


		dictionary = parse_models ( models )


		if dictionary:

			write_to_cache ( 'models', dictionary, True )


			for model in dictionary:

				write_to_cache ( f'models/{model}', dictionary [ model ], True )


			return True
