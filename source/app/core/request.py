import os
# import re
# import subprocess

from utilities.util 						import Util
# from utilities.system.file.get_files 		import get_files

class Request:

	def __init__( self, arguments ):

		#### 	GLOBALS 	################################

		self.arguments = arguments

		self.config = {
			'auth': {
				'org': None,
				'key': None
			},
			'model': [ ],
			'cache': {
				'clear_model':  None,
				'clear_prompt': None
			}
		}

		#### 	INITIALIZE 	################################

		Util.view_arguments ( self.arguments ) 					# @apiNote: *** DEBUG ***

		self.init ( )

	#### 	INITIATORS 	########################################

	def init ( self ):

		self.set_config ( )

		# self.compile   ( )

	#### 	SETTERS 	########################################

	def set_config ( self ):

		# @TODO: REPLACE WITH COMPREHENSION !
		self.config [ 'auth'  ] [ 'org'          ] = self.arguments [ 'org'          ]
		self.config [ 'auth'  ] [ 'key'          ] = self.arguments [ 'key'          ]
		self.config [ 'model' ] 		 		   = self.arguments [ 'model'        ]
		self.config [ 'cache' ] [ 'clear_model'  ] = self.arguments [ 'clear_model'  ]
		self.config [ 'cache' ] [ 'clear_prompt' ] = self.arguments [ 'clear_prompt' ]

		for value in self.config: print ( value, ':', self.config [ value ] )

	#### 	GETTERS 	########################################
