from torchvision import transforms
from PIL import Image

#Applique les transformations nécessaires pour préparer l'image à l'entrée du modèle.
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],  # Moyenne des canaux RGB pour ImageNet
                             [0.229, 0.224, 0.225])  # Écart-type des canaux RGB pour ImageNet
    ])
    image = Image.open(image_path).convert('RGB')
    return transform(image).unsqueeze(0)  # Ajout de la dimension de batch (1 image dans ce cas)

#Affiche la prédiction avec les probabilités pour chaque classe.
def display_results(image_name, prediction, probabilities, class_names):
    print(f"✅ L’image {image_name} est classée comme : {prediction}")
    print("Probabilités par classe :")
    for i, prob in enumerate(probabilities):
        print(f"{class_names[i]}: {prob.item():.4f}")