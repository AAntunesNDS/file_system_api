import sys
sys.path.append('../')

import unittest
import datetime
from file_system_api.database import Document
from file_system_api.enumerations import TYPE_DOCUMENT
from file_system_api.__init__ import __version__

class TestDocument(unittest.TestCase):

    mock_document_insert = {
        "name" : 'folder_1', 
        "type" : TYPE_DOCUMENT[0], 
        "url_pos_save" : "example.com.br", 
        "folder_parent_path" : "/", 
        "created_at" : datetime.datetime.now(),
    }

    def test_version(self):
        assert __version__ == '0.1.0'

    def test_create_Document_table(self):
        Document.create_table()
        assert Document

    def test_insert_document_table(self):
        
        Document.create_table()
        Document.create(**self.mock_document_insert)
        assert Document.select().count() > 0

    def test_get_document_item_by_name(self):
        Document.create_table()
        Document.create(**self.mock_document_insert)
        
        record = Document.get(Document.name == self.mock_document_insert["name"])
        print(record)

        assert record


if __name__ == '__main__':
    unittest.main()