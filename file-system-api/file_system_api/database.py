import peewee
import datetime

from enumerations import TYPE_DOCUMENT


db = peewee.SqliteDatabase('Document.db')

class BaseModel(peewee.Model):
    """Classe model base"""

    class Meta:
        # Indica em qual banco de dados a tabela
        # utilizamos o banco 'Document.db' criado anteriormente
        database = db


class Document(BaseModel):
    name = peewee.CharField()
    type = peewee.CharField(choices=TYPE_DOCUMENT)
    url_pos_save = peewee.CharField()
    folder_parent_path = peewee.CharField()
    created_at = peewee.DateTimeField(default=datetime.datetime.now().strftime('%Y-%m-%d'))
