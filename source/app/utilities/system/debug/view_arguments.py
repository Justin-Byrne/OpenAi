def view_arguments ( arguments ):

	print ( '-' * 4, '[ Arguments ]', '-' * 41 )


	max_key_length = max ( len ( key ) for key in arguments )


	for argument in arguments:

		spaces = max_key_length - len ( argument )

		print ( f'{argument}:', ' ' * spaces, arguments [ argument ] )


	print ( '-' * 60 )
