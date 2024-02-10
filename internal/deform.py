import cv2
import numpy as np
import os

def deformImage(workout):
    filePath = f"./data/{workout}.png"
    image = cv2.imread(filePath)
    
    if image is not None:
        height, width = image.shape[:2]

        points_originaux = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        points_dest = np.float32([[0, 0], [width, 0], [width // 4, height], [3 * width // 4, height]])
        
        matrice_homographique = cv2.getPerspectiveTransform(points_originaux, points_dest)
        image_deformee = cv2.warpPerspective(image, matrice_homographique, (width, height))
        
        cv2.imwrite(f"./data/deform-{workout}.png", image_deformee)
        os.remove(filePath)

        return "Image déformée avec succès"

    return "Erreur : Impossible de charger l'image initiale"