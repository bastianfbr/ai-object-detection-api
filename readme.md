# 🧠🎯 AI Object Detection API

API de **détection d'objets** en temps réel 🕵️‍♂️ basée sur le modèle **YOLOv11 (You Only Look Once)**.

---

## ✨ Fonctionnalités

- ⚡ **Détection d'objets en temps réel**
- 🧠 **Modèle YOLOv11 pré-entraîné** pour une performance optimale
- 🔌 **Intégration simple** via des endpoints RESTful
- 🔄 **Support de modèles personnalisés** (`.pt`)

---

## 📦 Installation

### 🛠️ Prérequis

- 🐍 Python **3.9+**
- 📦 `pip` installé

### 🚀 Étapes

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/bastianfbr/ai-object-detection-api.git
   cd ai-object-detection-api
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Assurez-vous que le modèle `best.pt` est bien présent dans `src/model/` :

> [!NOTE]
> Ce fichier est essentiel pour lancer l'API. Vous pouvez le remplacer par un autre modèle YOLOv11 pré-entraîné si besoin.

---

## ▶️ Démarrage de l'API

Lancez le serveur avec :

```bash
uvicorn main:app --reload
```

📍 API disponible à : `http://127.0.0.1:8000/`

---

## 🧪 Exemple d'utilisation

Pour détecter des objets dans une image :

```bash
curl -X POST http://127.0.0.1:8000/predict -F 'file=@path_to_your_image.jpg'
```

> [!TIP]
> Utilisez [Postman](https://www.postman.com/) ou [Insomnia](https://insomnia.rest/) pour tester vos requêtes facilement avec une interface graphique.

---

## 📤 Format de réponse de l’API

L’API retourne un JSON avec les objets détectés :

```json
{
  "predictions": [
    {
      "class_name": "canette",
      "confidence": 0.9555226564407349,
      "box_coordinates": [
        1001.8975219726562,
        2214.22705078125,
        1396.480224609375,
        2834.273193359375
      ]
    }
  ]
}
```

> [!NOTE]
> Les coordonnées sont dans l’ordre `[x_min, y_min, x_max, y_max]`.

### 📘 Détails des champs

| Champ             | Type     | Description                                           |
|------------------|----------|-------------------------------------------------------|
| `class_name`      | `string` | Nom de l’objet détecté (ex : `"canette"`)            |
| `confidence`      | `float`  | Score de confiance du modèle (entre 0 et 1)          |
| `box_coordinates` | `array`  | Coordonnées du cadre englobant l’objet détecté       |

---

## 🗂️ Structure du projet

```
ai-object-detection-api/
├── src/
│   ├── api/
│   │   ├── __init__.py        # Initialisation du module API
│   │   └── endpoints.py       # Définition des routes
│   └── model/
│       ├── __init__.py        # Initialisation du module modèle
│       ├── best.pt            # Modèle YOLOv11 pré-entraîné
│       └── yolo.py            # Wrapper/loader pour le modèle YOLO
├── .gitignore                  # Fichiers ignorés par Git
├── .pre-commit-config.yaml     # Configuration des hooks pre-commit
├── main.py                     # Point d'entrée principal (FastAPI)
└── requirements.txt            # Dépendances Python
```
