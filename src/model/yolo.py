from ultralytics import YOLO

MODEL_PATH = "src/model/best.pt"
model = YOLO(MODEL_PATH)


def predict_image(image_path: str):
    """
    Fait une prédiction sur une image donnée et renvoie les résultats formatés.

    Args:
        image_path (str): Le chemin vers l'image.

    Returns:
        list: Une liste de dictionnaires, chaque dictionnaire représentant un objet détecté.
              Retourne une liste vide si aucun objet n'est détecté.
    """
    if model is None:
        return []

    results = model(image_path)

    predictions = []
    if results and results[0].boxes:
        for box in results[0].boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            confidence = float(box.conf[0])
            class_id = int(box.cls[0])
            class_name = model.names[class_id]

            predictions.append(
                {
                    "class_name": class_name,
                    "confidence": confidence,
                    "box_coordinates": [x1, y1, x2, y2],
                }
            )

    return predictions
