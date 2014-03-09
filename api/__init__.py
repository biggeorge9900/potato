import os
import sys
import webapp2
from api.routes import routes
from api.configs import configs

'''
def include_3rdpart_libs():
    # path to 3rdparty directory
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../3rdparty'))

include_3rdpart_libs()
'''

application = webapp2.WSGIApplication(routes=routes, debug=True, config=configs)
