import os
import torch
from torchvision import datasets, transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader

def get_dataloaders(data_dir, batch_size=4):
    data_transforms = {
        "train": transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
        "val": transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
    }
    
    image_datasets = {
        "train": datasets.ImageFolder(os.path.join(data_dir, "Training_data"), transform=data_transforms["train"]),
        "val": datasets.ImageFolder(os.path.join(data_dir, "Testing_Data"), transform=data_transforms["val"]),
    }
    
    dataloaders = {
        "train": DataLoader(image_datasets["train"], batch_size=batch_size, shuffle=True),
        "val": DataLoader(image_datasets["val"], batch_size=batch_size, shuffle=False),
    }
    
    return dataloaders["train"], dataloaders["val"]