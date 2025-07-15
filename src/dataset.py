import os
import torch
from torchvision import datasets, transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader

def get_dataloaders(data_dir, batch_size=32):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]
        )
    ])
    
    train_dataset = datasets.ImageFolder(os.path.join(data_dir, "train"), transform=transform)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    
    val_dataset = datasets.ImageFolder(os.path.join(data_dir, "val"), transform=transform)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=True)
    
    """
    test_dataset = datasets.ImageFolder(os.path.join(data_dir, "test"), transform=transform)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    """
    return train_loader, val_loader