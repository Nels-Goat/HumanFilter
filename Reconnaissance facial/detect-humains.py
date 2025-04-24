import cv2
import os
import shutil

photos_dir = "photos"
result_dir = "humains"
os.makedirs(result_dir, exist_ok=True)

# Chemins des modèles
modelFile = "res10_300x300_ssd_iter_140000.caffemodel"
configFile = "deploy.prototxt"

net = cv2.dnn.readNetFromCaffe(configFile, modelFile)

for filename in os.listdir(photos_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(photos_dir, filename)
        img = cv2.imread(img_path)
        if img is None:
            continue
        (h, w) = img.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0,
            (300, 300), (104.0, 177.0, 123.0))
        net.setInput(blob)
        detections = net.forward()
        count = 0
        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.6:  # Seulement les détections "sûres"
                count += 1
        if count > 0:
            print(f"{count} visage(s) détecté(s) dans : {filename}")
            shutil.copy(img_path, os.path.join(result_dir, filename))
