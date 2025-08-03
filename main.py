from fastapi import FastAPI

from src.api import endpoints

app = FastAPI(
    title="API de détection d'objets Yolo",
    description="""
### Service de prédiction d'objets propulsé par YOLOv8

Cette API expose un modèle de détection d'objets personnalisé, entraîné avec YOLOv8.

Elle permet de soumettre des images et de recevoir en retour les prédictions
sous forme de boîtes englobantes, de classes et de scores de confiance.

Le code source du projet est disponible sur GitHub :
[https://github.com/jvondermarck/ai-object-detection/](https://github.com/jvondermarck/ai-object-detection/)
""",
)

app.include_router(endpoints.router)
