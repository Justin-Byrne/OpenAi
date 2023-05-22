import json

def parse_model ( model ):

	#### 	GLOBALS 	####################################

	result = { 'data': { }, 'permissions': { } }


	model_data = json.loads ( str ( model ) )

	#### 	FUNCTIONS 	####################################

	def filter_model ( ):

		for entry in model_data:

			if entry == 'permission':

				result [ 'permissions' ] = model_data [ entry ] [ 0 ]

			else:

				result [ 'data' ] [ entry ] = model_data [ entry ]

	#### 	LOGIC 	########################################

	filter_model ( )


	return result
