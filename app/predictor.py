import torch
import torch.nn as nn
import torchvision.models as models
import torch.nn.functional as F
from torchvision.models import ResNet18_Weights
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils import preprocess_image



# Liste des classes
class_names = ['Driving License', 'Others', 'Social Security']


# Charger le modèle (à faire une seule fois)
def load_model(model_path):
    model = models.resnet18(weights=ResNet18_Weights.DEFAULT)
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, len(class_names))
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

# Prédiction sur une image
def predict(model, image_path):
    image = preprocess_image(image_path)
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
        probabilities = F.softmax(outputs[0], dim=0)
    prediction = class_names[predicted.item()]
    confidence = float(probabilities[predicted.item()] * 100)  # Pourcentage
    return prediction, confidence
