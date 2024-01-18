from PIL import Image
import matplotlib.pyplot as plt
import internal.expectations as data

image = Image.open("assets/blanc.jpg")

largeur, hauteur = image.size
milieu_x = largeur / 2
milieu_y = hauteur / 2
marker_size = 100

class Exercices:
    def __init__(self):
        """
        Initialisation de la classe
        """
        pass

    def start(self, workout):
        """
        Afficher le graphique pour l'exercice spécifié

        :param workout: Le nom de l'exercice
        """
        title = data.fetchSugar(workout)
        positions = data.fetchPosition(workout)
        markers = {
            workout: positions
        }
        ajusted_markers = {
            workout: [(milieu_x + x, milieu_y + y) for x, y in positions]
            for workout, positions in markers.items()
        }

        plt.imshow(image)

        for point in ajusted_markers[workout]:
            plt.scatter(point[0], point[1], color="red", marker="o", s=marker_size)

        plt.scatter(milieu_x, milieu_y, color="blue", marker="x", s=marker_size)
        plt.axis('on')
        plt.title(f"Positionnement : {title}")
        plt.show()