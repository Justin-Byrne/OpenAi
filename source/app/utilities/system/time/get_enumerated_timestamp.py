import re

from datetime import datetime

ERROR = -1

def get_enumerated_timestamp ( timestamp = datetime.now ( ) ):

    result = {
        'year':  None,
        'month': None,
        'day':   None,
        'hour':  None,
        'min':   None,
        'sec':   None,
        'mil':   None
    }

    regex = r'(\d{4})-(\d{2})-(\d{2})\s*(\d{2})\:(\d{2}):(\d{2})\.(\d{3})'


    if isinstance ( timestamp, datetime ) and re.search ( regex, str ( timestamp ) ):

        matches = re.match ( regex, str ( timestamp ) )


        for i, entry in enumerate ( result ):

            match = matches.group ( i + 1 )


            if isinstance ( match, str ) and match.isdigit ( ):

                match = int ( match )


            result [ entry ] = match

    else:

        print ( 'you fucked up !' )

        return ERROR


    return result
