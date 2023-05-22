import json

from os.path 						import abspath

from ...system.validation.is_file 	import is_file

PATH = f"{abspath ( '.' )}/cache"

def read_from_cache ( filename ):

	DATA = ''

	FILE = f'{PATH}/{filename}.info'


	if is_file ( FILE, None ):

		DATA = open ( FILE, 'r' ).read ( )


	return json.loads ( DATA )
