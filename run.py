import os
if 'VIRTUAL_ENV' not in os.environ:
    import sys
    abspath = os.path.abspath(__file__)
    app_root = os.path.dirname(abspath)
    path = os.path.join(app_root, 'virtualenv.bundle')
    sys.path.insert(0, path)
    sys.path.insert(0, app_root)
from app import app
from app.admin import *
from app.view import *
if __name__ == "__main__":
    #app.run(threaded=True, host='0.0.0.0',port=80,debug=True)
    app.run()
