from PIL import Image
import matplotlib.pyplot as plt
# Charger l'image
image_path = "blanc.jpg"
image = Image.open(image_path)

largeur, hauteur = image.size
milieu_x = largeur / 2
milieu_y = hauteur / 2
print (milieu_x ,milieu_y)
# Coordonnées des points que vous souhaitez afficher pour chaque exercice
marqueurs = {
    "Pompes": [
        (milieu_x+400, milieu_y+150),  # Main droite
        (milieu_x+400, milieu_y-150),  # Main gauche
        (milieu_x-400, milieu_y+75),   # Pied droit
        (milieu_x-400, milieu_y-75),   # Pied gauche
    ],
    "Squats": [
        (milieu_x+100, milieu_y),  # pied gauche
        (milieu_x-100, milieu_y),  # pied droit

    ],
    "Burpees": [
        (milieu_x+400, milieu_y+150),  # Main droite
        (milieu_x+400, milieu_y-150),  # Main gauche
        (milieu_x-400, milieu_y+75),   # Pied droit
        (milieu_x-400, milieu_y-75),   # Pied gauches
    ],
    "Curls": [
        (milieu_x+100, milieu_y),  # Main droite
        (milieu_x-100, milieu_y),  # Main gauche

    ],
}

exercice =  input("ecrits en toutes lettre ce que tu veux ")
marker_size = 100


def afficher_points(exercice):
    # Affiche l'image avec les points pour l'exercice spécifié
    plt.imshow(image)

    # Ajoute les points aux coordonnées spécifiées pour l'exercice
    for point in marqueurs[exercice]:
        plt.scatter(point[0], point[1], color='red', marker='o', s=marker_size)
        




    # Ajoute un point au milieu de l'image
    plt.scatter(milieu_x, milieu_y, color='blue', marker='x', s=marker_size)
    # Affiche les axes (optionnel)
    plt.axis('on')

    # Affiche l'image avec les points
    plt.show()
    
afficher_points(exercice)
