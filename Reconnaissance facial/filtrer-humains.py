import pytesseract
import os
import shutil
from PIL import Image

# Si besoin, précise le chemin de tesseract sur Windows :
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

input_dir = "humains"
output_dir = "final"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(input_dir, filename)
        try:
            img = Image.open(img_path)
            text = pytesseract.image_to_string(img)
            # On garde les images avec moins de 20 caractères reconnus
            if len(text.strip()) < 20:
                print(f"Aucun texte détecté dans : {filename}")
                shutil.copy(img_path, os.path.join(output_dir, filename))
            else:
                print(f"Texte détecté ({len(text.strip())} caractères) dans : {filename}")
        except Exception as e:
            print(f"Erreur avec {filename} : {e}")
