import cv2
import numpy as np
import os

def deformImage(workout):
    filePath = f"./data/{workout}.png"
    
    points_originaux = np.float32([[0, 0], [1600, 0], [0, 800], [1600, 800]])
    points_dest = np.float32([[400, 0], [1200, 0], [0, 800], [1600, 800]])
    
    matrice_transformation = cv2.getPerspectiveTransform(points_originaux, points_dest)
    image_trapeze = cv2.warpPerspective(cv2.imread(filePath), matrice_transformation, (1600, 800))

    scaled_image = cv2.resize(image_trapeze, (800, 400))

    cv2.imshow("Image", scaled_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    os.remove(filePath)

    return "Image déformée avec succès"