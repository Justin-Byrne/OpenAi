import json

from ..validation.is_cached_file_old 	import is_cached_file_old
from .fetch_models 						import fetch_models

ERROR = -1

def get_models ( arguments ):

	if 'model' in arguments.keys ( ):

		if '|' in arguments [ 'model' ]:

			if is_cached_file_old ( 'models.info' ):

				return fetch_models ( arguments [ 'org' ], arguments [ 'key' ] )

			else:

				return True

		else:

			if is_cached_file_old ( f"models/{arguments [ 'model' ]}.info" ):

				return fetch_models ( arguments [ 'org' ], arguments [ 'key' ], arguments [ 'model' ] )

			else:

				return True

	else:

		if is_cached_file_old ( 'models.info' ):

				return fetch_models ( arguments [ 'org' ], arguments [ 'key' ] )

		else:

			return True
