import os
import shutil

from fastapi import APIRouter, File, UploadFile

from src.model.yolo import predict_image

router = APIRouter()


@router.get("/")
async def root():
    """
    Endpoint racine pour vérifier que l'API fonctionne.
    """
    return {"message": "Bienvenue dans l'API de détection d'objets!"}


@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Reçoit une image et renvoie les prédictions de détection d'objets.

    Args:
        file (UploadFile): L'image à traiter.

    Returns:
        dict: Un dictionnaire contenant les résultats de la détection.
    """
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    predictions = predict_image(file_path)
    os.remove(file_path)

    return {"predictions": predictions}
