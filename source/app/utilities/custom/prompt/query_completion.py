import openai

from ..connect.openai_certify 	import openai_certify

ERROR = -1

def query_completion ( arguments ):

	request = {						# REQUIRED | DATA TYPE 		   | DEFAULT 	     | #
		'model':  			 None, 	# Yes 	   | <string> 		   | N.A. 		     | 00
		'prompt': 			 None, 	# No. 	   | <string or array> | <|endoftext|>   | 01
		'suffix': 			 None, 	# No. 	   | <string> 		   | None		     | 02
		'max_tokens':  		 None, 	# No. 	   | <integer> 		   | 16			     | 03
		'temperature': 		 None, 	# No. 	   | <number> 		   | 1			     | 04
		'top_p': 			 None, 	# No. 	   | <number> 		   | 1			     | 05
		'n': 				 None,	# No. 	   | <integer> 		   | 1			     | 06
		'stream': 			 None,	# No. 	   | <boolean> 		   | False 		     | 07
		'logprobs': 		 None,	# No. 	   | <integer> 		   | None 		     | 08
		'echo': 			 None, 	# No. 	   | <boolean> 		   | False 		     | 09
		'stop': 			 None,	# No. 	   | <string or array> | None 		     | 10
		'presence_penalty':  None, 	# No. 	   | <number> 		   | 0			     | 11
		'frequency_penalty': None,  # No. 	   | <number> 		   | 0			     | 12
		'best_of': 			 None,  # No. 	   | <integer> 		   | 1			     | 13
		'logit_bias': 		 None,  # No. 	   | <map> 			   | None		     | 14
		'user': 			 None   # No. 	   | <string> 		   | N.A 		     | 15
	}

	request [ 'model' ]       = arguments [ 'model' ]

	request [ 'prompt' ]      = 'Say this is a test'

	request [ 'max_tokens' ]  = 7

	request [ 'temperature' ] = 0

	# request [ 'top_p' ] 	  = 1

	# request [ 'n' ] 		  = 1

	# request [ 'stream' ] 	  = False

	# request [ 'logprobs' ]  = None

	# request [ 'stop' ]      = '\n'

	try:

		openai   = openai_certify ( arguments [ 'org' ], arguments [ 'key' ] )

		response = openai.Completion.create (
			model       = request [ 'model'       ], 			# 00
			prompt      = request [ 'prompt'      ], 			# 01
			max_tokens  = request [ 'max_tokens'  ], 			# 03
			temperature = request [ 'temperature' ], 			# 04
			top_p 		= request [ 'top_p'       ], 			# 05
			n 			= request [ 'n'           ], 			# 06
			stream 		= request [ 'stream'      ], 			# 07
			logprobs 	= request [ 'logprobs'    ], 			# 08
			stop 		= request [ 'stop'        ] 			# 10
		)

		return response

	except openai.error.RateLimitError as e:

		print ( '>> [ERROR] query_completion.py\n\t~ Open AI connection failed !\n\t~ Rate limit exceeded !' )

		return ERROR
