import matplotlib.pyplot as plt
from src.dataset import get_dataloaders
from src.model import build_model
"""
#Charger les DataLoaders
train_loader, val_loader = get_dataloaders("notebooks/hymenoptera_data", batch_size=4)

#Récupérer un batch
images, labels = next(iter(train_loader))
classes = train_loader.dataset.classes

#Afficher le batch
fig, axs = plt.subplots(1, 4, figsize=(12, 4))
for i in range(4):
    img = images[i].permute(1, 2, 0)
    axs[i].imshow(img)
    axs[i].set_title(classes[labels[i]])
    axs[i].axis('off')
plt.show()
"""

# Créer le modèle avec 2 classes(ants & bees )
model = build_model(num_classes=2)
print(model)

total_params = sum(p.numel() for p in model.parameters())
trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)

print(f"Total parameters: {total_params}")
print(f"Trainable parameters: {trainable_params}")