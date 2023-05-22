import os

from .parse_commands 	import parse_commands
from .debug.output 		import output

ERROR = -1

def get_commands   ( commands ):

	arguments = parse_commands ( commands )


	if arguments [ 'org' ] == None:

		output ( 'get_commands', [ 'Org key needs to be present', 'Org key needs to be at least 24 characters long !' ] )

		return ERROR


	if arguments [ 'key' ] == None:

		output ( 'get_commands', [ 'Secret key needs to be present', 'Secret key needs to be at least 48 characters long !' ] )

		return ERROR


	if 'model' not in arguments.keys ( ):

		output ( 'get_commands', 'Requires at least a single model !' )

		return ERROR


	return arguments
