# Classificateur de Documents
![Python](https://img.shields.io/badge/python-3.9+-blue)


Ce projet est une application de classification automatique de documents (permis de conduire, sécurité sociale, autres) à partir d'images, basée sur un modèle de deep learning (ResNet18).  
L'application propose une interface web conviviale pour téléverser un document et obtenir sa catégorie.

## Fonctionnalités

- **Classification automatique** de documents en 3 classes : Permis de conduire, Sécurité sociale, Autres.
- **Interface web** moderne pour l'upload et la visualisation des résultats.
- **Prédiction par lot** possible via script.
- **Entraînement et évaluation** du modèle sur vos propres données.

## Structure du projet

```
.
├── app/                # Application web Flask
│   ├── app.py
│   ├── predictor.py
│   ├── static/
│   └── templates/
├── data/               # Données d'entraînement et de test
│   ├── Training_data/
│   ├── Testing_Data/
│   └── test_images/
├── models/             # Modèles sauvegardés (.pth)
├── notebooks/          # Notebooks pour l'entraînement
├── outputs/            # Résultats divers
├── src/                # Code source principal (entraînement, prédiction, utils)
├── main.py             # Exemple d'entraînement
├── requirements.txt    # Dépendances Python
└── README.md
```

## Installation

1. **Cloner le dépôt**
   ```sh
   git clone https://github.com/HanouneCamara/document_classifier.git
   cd document_classifier
   ```

2. **Installer les dépendances**
   ```sh
   pip install -r requirements.txt
   ```

3. **Télécharger ou préparer les données**
   - Placez vos images dans `data/Training_data/` et `data/Testing_Data/` selon la structure attendue.

## Entraînement

Lancez l'entraînement du modèle avec :

```sh
python main.py
```

Le modèle entraîné sera sauvegardé dans `models/model.pth`.

## Prédiction sur une image

Utilisez le script de prédiction :

```sh
python src/predict.py --image data/test_images/image1.jpg --model models/model.pth
```

## Prédiction par lot

```sh
python src/batch_predict.py --folder data/test_images/ --model models/model.pth
```

## Lancer l'application web

Depuis le dossier `app/` :

```sh
python app.py
```

Puis ouvrez [http://localhost:5000](http://localhost:5000) dans votre navigateur.

## Auteur

Hanoune

---

## Licence

Ce projet est fourni à des fins éducatives dans le cadre d’un stage. Toute réutilisation doit être créditée à l’auteur.
