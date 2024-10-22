from minio import Minio
from fastapi import FastAPI, status, UploadFile
from datetime import timedelta
from fastapi.responses import JSONResponse
from typing import Annotated


# Initialize MinIO client
client = Minio('localhost:9000',
            access_key='fastapibucket',
            secret_key='MKgk6b2TbsdQCVnYCMumUeZR1T4VPBu3oyyz8BBZ',
            secure=False)

if client.bucket_exists("fastapi"):    
    
    # List objects
    objects = client.list_objects('fastapi', recursive=True)
    for obj in objects:
        
        app = FastAPI()

        @app.get('/test')
        def test():
                return {
                    "PDFs": client.presigned_get_object("fastapi", "1-I-A-1.pdf", expires=timedelta(hours=2)),
                    "ICO": client.presigned_get_object("fastapi", "fb.ico", expires=timedelta(hours=2)),
                    "PNG": client.presigned_get_object("fastapi", "myfile.png", expires=timedelta(hours=2))
                }
        
        @app.post('/test')
        def tests(file: UploadFile):
            # return {"file": file.filename}
            # Upload an object
            client.fput_object('fastapi', file.filename, file_path=file.filename)
            return JSONResponse(content={"status": status.HTTP_200_OK})
else:
    print("my-bucket does not exist")
