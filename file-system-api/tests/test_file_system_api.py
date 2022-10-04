import sys
sys.path.append('../')

import unittest
import requests
import json
from file_system_api.__init__ import __version__

#TODO test 2 posts (folder file) 1 get

class TestDocument(unittest.TestCase):

    URL = 'http://127.0.0.1:5000/document'
    HEADERS = {'Content-type': 'application/json'}

    def test_post_folder(self):

        mock_request_body = {
            "name" : "folder_unittest",
            "type" : "folder",
            "folder_parent_path" : "/"
        }
    
        response = requests.post(self.URL, data=json.dumps(mock_request_body), headers=self.HEADERS)

        assert response.status_code == 201
        
    def test_post_file(self):

        mock_request_body = {
            "name" : "teste_unit.txt",
            "type" : "file" ,
            "b64_file" : "VGVzdGVzdGVzdGU=", # b64 string
            "folder_parent_path" : "/"
        }
    
        response = requests.post(self.URL, data=json.dumps(mock_request_body), headers=self.HEADERS)

        print(response)
        assert response.status_code == 201
        
    def test_get(self):
        response = requests.get(self.URL)
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()