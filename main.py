from fastapi import FastAPI

from src.api import endpoints

app = FastAPI(
    title="API de détection d'objets",
    description="""
### Service de prédiction d'objets propulsé par YOLOv11

Cette API expose un modèle de détection d'objets personnalisé, entraîné avec YOLOv11.

Elle permet de soumettre des images et de recevoir en retour les prédictions
sous forme de boîtes englobantes, de classes et de scores de confiance.

Le code source du projet d'entraînement du model est disponible sur GitHub :
[https://github.com/jvondermarck/ai-object-detection/](https://github.com/jvondermarck/ai-object-detection/)
""",
)

app.include_router(endpoints.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
