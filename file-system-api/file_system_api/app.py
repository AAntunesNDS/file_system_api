from flask import Flask, jsonify, request
from flasgger import Swagger
from flask_restful import Api, Resource
from database import Document
from views import DocumentView

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)
table_db = Document.create_table()

api.add_resource(DocumentView, '/document')

if __name__ == '__main__':
    app.run(debug = True)


