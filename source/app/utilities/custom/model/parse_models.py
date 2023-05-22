import json

def parse_models ( models ):

	#### 	GLOBALS 	####################################

	result = { }


	model_data   = json.loads ( str ( models ) )

	#### 	FUNCTIONS 	####################################

	def filter_models ( ):

		for data in model_data [ 'data' ]:

			temp = { 'data': { }, 'permissions': { } }


			for entry in data:

				if entry == 'permission':

					for permission in data [ entry ] [ 0 ]:

						temp [ 'permissions' ] [ permission ] = data [ entry ] [ 0 ] [ permission ]

				else:

					temp [ 'data' ] [ entry ] = data [ entry ]


			ROOT = temp [ 'data' ] [ 'root' ]


			if ROOT not in result.keys ( ):

				result [ ROOT ]                   = temp [    'data'     ]
				result [ ROOT ] [ 'permissions '] = temp [ 'permissions' ]

			else:

				print ( f'>> [ERROR] parse_list_models.py\n\t~ "{ROOT}" is already a valid model !' )

	#### 	LOGIC 	########################################

	filter_models ( )


	return result
