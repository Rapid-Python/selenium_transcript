from extension import app
from app.controller.transcript import api
import logging

logging.basicConfig(level=logging.DEBUG)

app.logger.setLevel(logging.INFO)

# register the api
app.register_blueprint(api)

if __name__ == '__main__':
    ''' run application '''
    app.run(host='0.0.0.0', port='8000', debug=True)
