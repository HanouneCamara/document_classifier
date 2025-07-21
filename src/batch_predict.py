import os
import argparse

import torch
from predict import load_model, predict_image
from utils import display_results, preprocess_image

# Fonction pour traiter un dossier d'images
def batch_predict(model, folder_path):
    supported_formats = ['.jpg', '.jpeg', '.png', '.bmp']
    class_names = ['driving_license', 'others', 'social_security']

    for filename in os.listdir(folder_path):
        if any(filename.lower().endswith(ext) for ext in supported_formats):
            image_path = os.path.join(folder_path, filename)
            print(f"\n📷 Traitement de l’image : {filename}")
            predicted_class, probabilities = predict_image(model, image_path)
            display_results(filename, predicted_class, probabilities, class_names)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Prédiction par lot des documents")
    parser.add_argument('--folder', type=str, required=True, help="Dossier contenant les images")
    parser.add_argument('--model', type=str, default='../models/model.pth', help='Chemin du modèle entraîné')
    args = parser.parse_args()
    
    if not os.path.exists(args.folder):
        print("❌ Dossier non trouvé :", args.folder)
        exit(1)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = load_model(args.model)
    
    batch_predict(model, args.folder)