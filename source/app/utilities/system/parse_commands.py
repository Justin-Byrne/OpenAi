import re
import os

def parse_commands ( commands ):

	#### 	GLOBALS 	####################################

	arguments = {
		'org': None,
		'key': None
	}

	regexes = {
		'org':   		r'\s*-o\s*|\s*--org\s*',
		'key':   		r'\s*-k\s*|\s*--key\s*',
		'model': 		r'\s*-m\s*|\s*--model\s*',
		'clear_model':	r'\s*-cm\s*|\s*--clear_model\s*',
		'clear_prompt': r'\s*-cp\s*|\s*--clear_prompt\s*'
	}

	#### 	FUNCTIONS 	####################################

	def validate_keys      ( regex, value ):

		keys = {
			'org': 'org-',
			'key': 'sk-'
		}

		lengths = {
			'org': 28,
			'key': 51
		}

		length = len ( value )


		match regex:

			case 'org':

				if value[:4] == keys [ regex ] and length == lengths [ regex ]:

					arguments [ regex ] = value

				elif length == 24 and re.search ( rf'\w{{{length}}}', value ):

					arguments [ regex ] = f'org-{value}'

			case 'key':

				if value[:3] == keys [ regex ] and length == lengths [ regex ]:

					arguments [ regex ] = value

				elif length == 48 and re.search ( rf'\w{{{length}}}', value ):

					arguments [ regex ] = f'sk-{value}'

	def check_command_line ( ):

		for i in range ( 1, len ( commands ) ):

			command = commands [ i ]


			for regex in regexes:

				if ( re.search ( regexes [ regex ], command ) ):

					value  = commands [ i + 1 ]

					length = len ( value )


					match regex:

						case 'org' | 'key':

							validate_keys ( regex, value )

						case _default:

							arguments.update ( { regex: value } )

	def check_config_file  ( ):

		config_regex = {
			'org':   		r'OPEN\s*API\s*ORG',
			'key':   		r'OPEN\s*API\s*KEY',
			'model': 		r'\s*MODELS\s*',
			'clear_model': 	r'CLEAR_CACHE_MODEL\s*?=\s*?(\d{2}:\d{2}:\d{2}:\d{2})',
			'clear_prompt': r'CLEAR_CACHE_PROMPT\s*?=\s*?(\d{2}:\d{2}:\d{2}:\d{2})'
		}


		for regex in config_regex:

			if regex in arguments.keys ( ):

				if arguments [ regex ] == None:

					value   = None

					lines   = open ( './config/config.txt', 'r' ).readlines ( )

					capture = False


					for line in lines:

						if re.search ( config_regex [ regex ], line ):

							capture = True

							continue


						if capture:

							if line [ 0 ] in [ '\n', '\r\n', '#' ]: continue

							else:

								value = line.replace ( '\n', '' )


						if value:

							validate_keys ( regex, value )

							break

			else:

				values  = [ ]

				lines   = open ( './config/config.txt', 'r' ).readlines ( )

				capture = False


				match regex:

					case 'clear_model' | 'clear_prompt':

						data = open ( './config/config.txt', 'r' ).read ( )


						if re.search ( config_regex [ regex ], data ):

							value = re.search ( config_regex [ regex ], data ).group ( 1 )

							arguments.update ( { regex: value } )

					case _default:

						for line in lines:

							if capture and line [ 0 ] == '\n':

								break


							if re.search ( config_regex [ regex ], line ):

								capture = True

								continue


							if capture:

								if line [ 0 ] in [ '\n', '\r\n', '#' ]: continue

								else:

									values.append ( line.replace ( '\n', '' ) )


							if len ( values ) > 0:

								arguments.update ( { regex: '|'.join ( values ) } )

	#### 	LOGIC 	########################################

	check_command_line ( )

	check_config_file  ( )


	return arguments
