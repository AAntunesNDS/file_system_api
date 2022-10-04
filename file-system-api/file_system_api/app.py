import sys
sys.path.append('../')

from flask import Flask
from flasgger import Swagger
from flask_restful import Api

from file_system_api.database import Document
from file_system_api.views import DocumentView

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)
table_db = Document.create_table()

api.add_resource(DocumentView, '/document')

if __name__ == '__main__':
    app.run(debug = True)


