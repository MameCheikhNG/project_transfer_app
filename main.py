from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from pathlib import Path
import uuid
import shutil

app = FastAPI()

UPLOAD_DIR = Path("C:/Users/mamecheikh.ngom/PycharmProjects/project_transfer_app/shared_files")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    file_path = UPLOAD_DIR / f"{file_id}_{file.filename}"
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"file_id": file_id, "filename": file.filename}

@app.get("/download/{file_id}/{filename}")
def download_file(file_id: str, filename: str):
    file_path = UPLOAD_DIR / f"{file_id}_{filename}"
    if not file_path.exists():
        return {"error": "Fichier introuvable"}
    return FileResponse(file_path, filename=filename)
