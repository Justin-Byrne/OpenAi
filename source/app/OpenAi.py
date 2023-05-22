import sys

from utilities.util 	import Util
from core.request 		import Request

ERROR = -1

def main ( commands ):

	arguments = Util.get_commands ( commands )


	if arguments != ERROR:

		Request ( arguments )

		# Util.view_arguments ( arguments ) 						# @apiNote: *** DEBUG ***

		# if Util.get_models ( arguments ):

		# 	pass
		# 	# Util.get_completion ( arguments )

		# else:

		# 	Util.output ( 'main', 'Could not obtain open AI models !' )


main ( sys.argv )
