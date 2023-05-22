from .query_completion 							import query_completion

from ..file.write_to_cache						import write_to_cache

from ...system.time.get_enumerated_timestamp 	import get_enumerated_timestamp

def get_completion ( arguments ):

	#### 	GLOBALS 	####################################

	response = query_completion ( arguments )

	text 	 = response [ 'choices' ] [ 0 ] [ 'text' ].strip ( )

	#### 	LOGIC 	########################################

	if text:

		timestamp = get_enumerated_timestamp ( )

		filename = f"responses/{timestamp [ 'year' ]}/{timestamp [ 'month' ]}-{timestamp [ 'day' ]}/{timestamp [ 'hour' ]}:{timestamp [ 'min' ]}:{timestamp [ 'sec' ]}.{timestamp [ 'mil' ]}"


		write_to_cache ( filename, response, True )

	else:

		print ( '>> [ERROR] get_completion.py\n\t~ Open AI connection failed !' )
