import json
import base64

from flask import request
from flask_restful import Resource
from service import FileSystemService
from database import Document


class DocumentView(Resource):

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
        """

        data = request.get_json()
        
        if data["type"] == 'folder':
            FileSystemService().create_folder(data["name"])
            data["url_pos_save"]= ""
        
        if data["type"] == 'file':
            assert data["b64_file"] != ""
            decoded_value = base64.b64decode(data["b64_file"]).decode('utf-8')
            with open(f'file_system_api/temp/{data["name"]}', 'w') as f:
                f.write(decoded_value)
                
            data["url_pos_save"] = FileSystemService().create_file(data["name"])
        
        Document.create(**data)
        return {'document': data}, 201

    def get(self):
        documents = [json.loads(json.dumps(document, default=str)) for document in Document.select().dicts()]
        return {'documents':documents}, 200
