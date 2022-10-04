import json
import base64

from flask import request
from flask_restful import Resource
from file_system_api.service import FileSystemService
from file_system_api.database import Document


class DocumentView(Resource):

    def post(self):
        """
        ---
        parameters:
        - name: create folder
          in: body
          required: true
          schema:
            id : Create Folder
            required:
              - name
              - type
              - folder_parent_path
            properties:
              name:
                type: string 
                description: Nome do arquivo
              type:
                type: string
                description: Tipo do arquivo (folder)
              folder_parent_path:
                type: string
                description: Caminho do arquivo
        - name: create file
          in: body
          required: true
          schema:
            id : Create file
            required:
              - name
              - type
              - b64_file
              - folder_parent_path
            properties:
              name:
                type: string 
                description: Nome do arquivo
              b64_file:
                type: string 
                description: String em base64 do arquivo a ser enviado
              type:
                type: string
                description: Tipo do arquivo (file)
              folder_parent_path:
                type: string
                description: Caminho do arquivo
        responses: 
          201:
            description: Created
        """
        data = request.get_json()
        
        if data["type"] == 'folder':
            FileSystemService().create_folder(data["name"])
            data["url_pos_save"]= ""
        
        if data["type"] == 'file':
            assert data["b64_file"] != ""
            decoded_value = base64.b64decode(data["b64_file"]).decode('utf-8')
            with open(f'temp/{data["name"]}', 'w') as f:
                f.write(decoded_value)
                
            data["url_pos_save"] = FileSystemService().create_file(data["name"])
        
        Document.create(**data)
        return {'document': data}, 201

    def get(self):
        """
        ---
        responses:
          200:
            description: All Files
        """
        documents = [json.loads(json.dumps(document, default=str)) for document in Document.select().dicts()]
        return {'documents':documents}, 200
