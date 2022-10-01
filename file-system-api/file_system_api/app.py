import json
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/') 
def hello_world():
    response = jsonify('Hello world!')
    response.status_code = 200
    return response

@app.route('/folder', methods = ['GET', 'POST', 'DELETE'])
def folder():
    #if post:
        #TODO create folder in s3 root
        #TODO create artefato on database SQL
    #if get:
        #TODO get folder url download
    #if delete:
        #TODO delete folder in s3 root
        #TODO delete artefato on database SQL
    
    return print("test")



@app.route('/file', methods = ['GET', 'POST', 'DELETE', 'UPDATE'])
def file():
    #if post:
        #TODO get folder with folder body
        #TODO create file in s3 folder
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
    
    return print("test")


if __name__ == "__main__":
    app.run(debug=True)