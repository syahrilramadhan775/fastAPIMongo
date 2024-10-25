from dotenv import dotenv_values
from minio import Minio

# env = dotenv_values('../../.env')
env = dotenv_values('../.env')

class MinioService:
    def __init__(self, host, port, bucket, access_key, secret_key) -> None:
        self.host = host
        self.port = port
        self.bucket = bucket
        self.access_key = access_key
        self.secret_key = secret_key

    def _minio(self):
        client = Minio(f'{self.host}:{self.port}',
            access_key=f'{self.access_key}',
            secret_key=f'{self.secret_key}',
            secure=False)
        return client

class FileSystems:
    minio = MinioService(env['AWS_HOST'], env['AWS_PORT'], env['AWS_BUCKET'], env['AWS_ACCESS_KEY'], env['AWS_SECRET_KEY'])
    def __init__(self, services) -> None:
        self.services = services

    def _connection_(self):
        conn = env['AWS_CONNECTION']
        match conn:
            case "minio":
                return FileSystems.minio._minio()
            case _:
                return "Nothing Else"
            
    def _get_bucket(self):
        self.bucket = FileSystems.minio.bucket
        return self.bucket
    
    def _get_local_path(self):
        self.path = env["LOCAL_PATH"]
        return self.path

