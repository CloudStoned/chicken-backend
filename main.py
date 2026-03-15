from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
from image_analyzer import read_photo
import os

app = FastAPI()

origins = os.getenv("DEV_ORIGINS")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".heic", ".heif", ".webp", ".bmp"}

@app.get("/")
def home():
    return {"message": "Chicken Server Running"}

@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    ext = os.path.splitext(file.filename or "")[1].lower()
    is_image = file.content_type.startswith("image/") or ext in ALLOWED_EXTENSIONS
    if not is_image:
        return {"error": "File must be an image"}
    img_bytes = await file.read()
    try:
        Image.open(io.BytesIO(img_bytes))
    except Exception as e:
        print(f"Image open failed: {e}")
        return {"error": "Invalid image format"}
    response = read_photo(img_bytes, file.content_type)
    return response