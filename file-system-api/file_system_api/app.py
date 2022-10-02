import json

from flask import Flask, jsonify, request
from flasgger import Swagger
from flask_restful import Api, Resource
from database import Document
import datetime


app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)
table_db = Document.create_table()

#TODO swagger route!!!!  90% DONE

#TODO Artefato Database Peewee sqlite

#TODO service class aws boto3


class DocumentView(Resource):
    class DateTimeEncoder(json.JSONEncoder):
        def default(self, z):
            if isinstance(z, datetime.datetime):
                return (str(z))
            else:
                return super().default(z)


    def post(self):
        """
        ---
        parameters:
          - name: document name
            type: enumeration
            folder_parent_path: path
            url_pos_save: url string

        responses:
          200:
            description: A list of documents
            schema:
              name: string
              folder_parent_path: path
              url_pos_save: url string
              type: document type
              default: Steven Wilson
        """

        data = request.get_json()
        Document.create(**data)
        return {'document': data}, 201

    def get(self):
        documents = [json.loads(json.dumps(document, default=str)) for document in Document.select().dicts()]
        print(documents)
        return {'documents':documents}, 200

#if post:
    #TODO create folder in s3 path root is = /
    #TODO create artefato on database SQL
#if get:
    #TODO get folder url download
#if delete:
    #TODO delete folder in s3 root
    #TODO delete artefato on database SQL

#if post:
    #TODO create file in s3 folder path (root is /)
    #TODO create artefato on database SQL
#if get:
    #TODO get file url download
#if delete:
    #TODO check file exists
    #TODO delete file in s3
    #TODO delete artefato on database SQL
#if update:
    #TODO check file exists
    #TODO delete file in s3
    #TODO create file in s3
    #TODO update artefato on database SQL (URL and updated_at)


api.add_resource(DocumentView, '/document')

if __name__ == '__main__':
    app.run(debug = True)


