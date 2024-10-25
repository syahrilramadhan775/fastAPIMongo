from fastapi import FastAPI, status, UploadFile, File
from datetime import timedelta
from fastapi.responses import JSONResponse
from typing import Annotated
from dotenv import dotenv_values
from config.fileSystem import FileSystems

env = dotenv_values('../.env')

# Initialize MinIO client
client = FileSystems(env['AWS_CONNECTION'])._connection_()
bucketName = FileSystems(env['AWS_CONNECTION'])._get_bucket()
filePath = FileSystems(env['AWS_CONNECTION'])._get_local_path()
type = "image/jpg"

if client.bucket_exists(bucket_name=bucketName):    
    
    # List objects
    objects = client.list_objects(bucket_name=bucketName, recursive=True)
    for obj in objects:
        
        app = FastAPI()

        @app.get('/test')
        def test():
            return {
                "PDFs"  : client.presigned_get_object(bucketName, "1-I-A-1.pdf", expires=timedelta(hours=2)),
                "ICO"   : client.presigned_get_object(bucketName, "fb.ico", expires=timedelta(hours=2)),
                "PNG"   : client.presigned_get_object(bucketName, "Bahasa.jpeg", expires=timedelta(hours=2)),
                "JPG"   : client.presigned_get_object(bucketName, "frtsh.jpeg", expires=timedelta(hours=2))
            }

        @app.put('/test')
        def tests(file: Annotated[UploadFile, File(...)]):
            open('assets/'+file.filename, 'wb').write(file.file.read())

            client.fput_object(bucketName, file.filename, filePath+"/"+file.filename, type)
            return JSONResponse(content={
                "status": status.HTTP_200_OK, 
                "cumi": client.presigned_get_object(bucketName, file.filename, expires=timedelta(hours=2))
            })
else:
    print("my-bucket does not exist")
