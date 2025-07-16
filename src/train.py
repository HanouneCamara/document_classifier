import torch
import torch.nn
import torch.optim

# Fontion pour l'entraînement
def train(model, train_loader, val_loader, device, epochs=10, lr=0.001):
    # Mettre le modèle sur le bon device
    model.to(device)
    
    # Fonction de perte
    criterion = torch.nn.CrossEntropyLoss()
    
    # Créer l'optimiseur
    optimizer = torch.optim.Adam(model.fc.parameters(), lr=lr)
    
    # La boucle d’apprentissage
    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        
        for inputs, labels in train_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()
            
        avg_loss = running_loss / len(train_loader)
        print(f"Epoch [{epoch+1}/{epochs}] - Train Loss: {avg_loss:.4f}")