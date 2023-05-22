import os
import re

from datetime import datetime, timedelta

from ...system.time.get_enumerated_timestamp 	import get_enumerated_timestamp

CONFIG = f"{os.getcwd ( ).split ( 'utilities', 1 ) [ 0 ]}/config/config.txt"

REGEX  = r'CLEAR_CACHE_MODEL\s*?=\s*?(\d{2}:\d{2}:\d{2}:\d{2})'

ERROR  = -1

def is_cached_file_old ( file ):

	#### 	GLOBALS 	####################################

	FILE = f"{os.getcwd ( ).split ( 'utilities', 1 ) [ 0 ]}/cache/{file}"

	#### 	FUNCTIONS 	####################################

	def get_time_difference ( ):

		time_created = datetime.fromtimestamp ( os.path.getctime ( FILE ) )

		time_current = datetime.now ( )


		time_elapsed = ( time_current - time_created )


		return time_elapsed

	def get_cache_interval  ( ):

		value   = None

		lines   = open ( CONFIG, 'r' ).readlines ( )

		capture = False


		for line in lines:

			if re.search ( r'CACHING', line ):

				capture = True

				continue


			if capture:

				if re.search ( REGEX, line ):

					value = re.search ( REGEX, line ).group ( 1 ).split ( ':' )

					value = [ int ( entry ) for entry in value ]

					value = timedelta ( days = value [ 0 ], hours = value [ 1 ], minutes = value [ 2 ], seconds = value [ 3 ], milliseconds = 0 )

				else:

					continue


			if value:

				return value


		return ERROR

	#### 	LOGIC 	########################################

	if os.path.isfile ( FILE ):

		time_elapsed   = get_time_difference ( )

		cache_interval = get_cache_interval  ( )


		if cache_interval == -1:

			print ( ' >> [ERROR] is_cached_file_old.py\n\t~ Could not locate caching settings in config.txt !' )

			return ERROR

		else:

			return True if time_elapsed > cache_interval else False

	else:

		return True
