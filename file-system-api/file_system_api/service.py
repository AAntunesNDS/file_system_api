import boto3
from dotenv import load_dotenv
import os
  
load_dotenv()

class FileSystemService():

    def __init__(self) -> None:
        self.session = boto3.Session(
            aws_access_key_id=os.environ.get('AWS_ACCOUNT_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_KEY')
        )
        self.s3 = self.session.resource('s3')
        self.bucket = os.environ.get('BUCKET_NAME')

    @staticmethod
    def create_url(bucket , file_name):
        return f'https://{bucket}.s3.amazonaws.com/{file_name}'

    def create_file(self, file_name):
        try:
            self.s3.Bucket(self.bucket).upload_file(f'temp/{file_name}', file_name)
            os.remove(f'temp/{file_name}')
            url = self.create_url(self.bucket, file_name)
            return url
        except:
            # log in cloud watch
            print("Error when creating file!")

    def create_folder(self, folder_name):
        try:
            response = self.s3.Bucket(os.environ.get('BUCKET_NAME')).put_object(
                Body='',
                Key=f'{folder_name}/'
            )
            return response
        except:
            # log in cloud watch
            print("Error when creating folder!")
