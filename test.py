import torch
import torchvision
from torchvision import transforms
from PIL import Image
from pathlib import Path
import matplotlib.pyplot as plt

device = "mps" if torch.backends.mps.is_available() else "cpu"
print(device)

class_names = ['Apple_Fresh', 'Apple_Rotten', 'Banana_Fresh', 'Banana_Rotten', 'Strawberry_Fresh', 'Strawberry_Rotten']

weights = torchvision.models.EfficientNet_V2_L_Weights.DEFAULT
model = torchvision.models.efficientnet_v2_l(weights=weights).to(device)

model.classifier = torch.nn.Sequential(
    torch.nn.Dropout(p=0.2, inplace=True),
    torch.nn.Linear(in_features=1280, out_features=len(class_names), bias=True)
).to(device)

MODEL_PATH = Path("models/fruit_model")
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.eval()  
print("Model loaded")

auto_transforms = weights.transforms()

def predict_image(image_path: str, model=model, class_names=class_names, transform=auto_transforms, device=device):
    img = Image.open(image_path).convert('RGB')
    transformed_img = transform(img).unsqueeze(0).to(device)
    
    with torch.inference_mode():
        pred_logits = model(transformed_img)
        pred_probs = torch.softmax(pred_logits, dim=1)
        pred_label = torch.argmax(pred_probs, dim=1)
        confidence = pred_probs[0][pred_label].item()

    predicted_class = class_names[pred_label.item()]
    return predicted_class, confidence

def predict_and_plot(image_path: str, model=model, class_names=class_names, transform=auto_transforms, device=device):
    img = Image.open(image_path).convert('RGB')
    
    pred_class, confidence = predict_image(image_path, model, class_names, transform, device)
    
    plt.figure(figsize=(8, 8))
    plt.imshow(img)
    plt.title(f"Predicted: {pred_class} | Confidence: {confidence:.3f}", fontsize=14)
    plt.axis('off')
    plt.show()
    return pred_class, confidence

image_path = "banana.jpg"  
predicted_class, confidence = predict_image(image_path)
print(f"Predicted class: {predicted_class}")
print(f"Confidence: {confidence:.3f}")


