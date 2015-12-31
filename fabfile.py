# -*- coding: utf-8 -*-
from fabric.api import env, run, local, settings
from datetime import datetime

def github(m='Commit something to master...'):
	'''github:m = "COMMIT LOGGING"\t(default as 'Commit something to master...')
	'''	
	local('pwd'		    
		    '&& git add -A'
		    '&& git commit -am "{msg}"'
		    '&& git push'
        )