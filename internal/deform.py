import cv2
import numpy as np
import os

def deformImage(workout):
    filePath = f"./data/{workout}.png"
    image = cv2.imread(filePath)
    
    if image is not None:
        height, width = image.shape[:2]
        center = (width // 2, height // 2)
        radius = min(center)
        
        map_x, map_y = np.meshgrid(np.arange(width), np.arange(height))
        polar_map_x = center[0] + ((map_x - center[0]) / radius) * np.sqrt((map_x - center[0])**2 + (map_y - center[1])**2)
        polar_map_y = center[1] + ((map_y - center[1]) / radius) * np.sqrt((map_x - center[0])**2 + (map_y - center[1])**2)
        
        image_cercle = cv2.remap(image, polar_map_x.astype(np.float32), polar_map_y.astype(np.float32), interpolation=cv2.INTER_LINEAR)
        
        cv2.imwrite(f"./data/deform-{workout}.png", image_cercle)
        os.remove(filePath)

        return "Image déformée avec succès"

    return "Erreur : Impossible de charger l'image initiale"