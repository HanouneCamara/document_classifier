import torch
import torchvision.models
import torch.nn
from torchvision.models import ResNet18_Weights


def build_model(num_classes):
    # Charger resnet18 pré-entraîné
    model = torchvision.models.resnet18(weights=ResNet18_Weights.DEFAULT)
    
    # Geler les anciennes couches
    for param in model.parameters():
        param.requires_grad = False
        
    # Remplacer la couche fc
    model.fc = torch.nn.Linear(in_features=512, out_features=num_classes)
    
    # Retourner le modèle
    return model