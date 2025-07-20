import torch
import torchvision.transforms as transforms
from PIL import Image
import torch.nn as nn
import torchvision.models as models
import argparse
import os

from utils import preprocess_image, display_results


class_names = ['driving_license', 'others', 'social_security']
# Charge le modèle avec les bons poids
def load_model(model_path):
    model = models.resnet18(pretrained=True)
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, len(class_names))

    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

# Fonction de prédiction
def predict_image(model, image_path):
    image = preprocess_image(image_path) 

    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
        # Calcul des probabilités
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
        
        
    prediction = class_names[predicted.item()]
    return prediction, probabilities


# Point d’entrée du script
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Classification de document")
    parser.add_argument('--image', type=str, required=True, help='Chemin de l’image')
    parser.add_argument('--model', type=str, default='../models/model.pth', help='Chemin du modèle entraîné')
    args = parser.parse_args()

    if not os.path.exists(args.image):
        print("Erreur : image non trouvée :", args.image)
        exit(1)

    model = load_model(args.model)
    prediction, probabilities = predict_image(model, args.image)
    display_results(args.image, prediction, probabilities, class_names)


    