#!/usr/bin/python3

from spacyjsonnlp import SpacyPipeline
from pyjsonnlp.microservices.flask_server import FlaskMicroservice
import os

app = FlaskMicroservice(__name__, SpacyPipeline(), base_route='/')

app.with_constituents = (os.environ.get('CONSTITUENTS', 'true') != 'false')
app.with_coreferences = (os.environ.get('COREFERENCES', 'true') != 'false')
app.with_dependencies = True
app.with_expressions = True

if __name__ == "__main__":
    app.run(debug=True, port=5001, host='0.0.0.0')
