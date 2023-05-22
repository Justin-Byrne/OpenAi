# SYSTEM
from .system.get_commands 				import get_commands 	# GENERAL

from .system.validation.is_directory 	import is_directory		# VALIDATION
from .system.validation.is_file 		import is_file

from .system.debug.output 				import output 			# DEBUG
from .system.debug.view_arguments 		import view_arguments

# CUSTOM
from .custom.connect.openai_certify 	import openai_certify 	# CONNECT

from .custom.model.get_models			import get_models 		# MODEL

from .custom.prompt.get_completion 		import get_completion 	# PROMPT

class Util:

	def __init__ (  ): pass

	#### 	SYSTEM 	########################################

	# GENERAL

	def get_commands   ( commands ) 		 	  			: return get_commands   ( commands )

	# VALIDATION

	def is_directory   ( path ) 				  			: return is_directory   ( path )

	def is_file 	   ( path,   type = None ) 				: return is_file        ( path, type )

	# DEBUG

	def output 		   ( source, message, type = 'ERROR' )	: return output 		( source, message, type )

	def view_arguments ( arguments )						: return view_arguments ( arguments )

	#### 	CUSTOM 	########################################

	# CONNECT

	def openai_certify ( API_ORG, API_KEY ) 				: return openai_certify ( API_ORG, API_KEY )

	# MODEL

	def get_models     ( arguments )                 		: return get_models     ( arguments )

	# PROMPT

	def get_completion ( arguments )						: return get_completion ( arguments )
