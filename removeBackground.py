import cv2
import numpy as np

# Charger l'image
image_path = "image.jpg"
image = cv2.imread(image_path)

# Convertir l'image en couleur HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Définir les limites de la couleur d'arrière-plan en HSV
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

# Créer un masque en utilisant le seuillage
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Inverser le masque pour obtenir le masque de l'arrière-plan
mask_inverse = cv2.bitwise_not(mask)

# Remplacer les pixels de l'arrière-plan par une couleur bleue
image[np.where(mask_inverse == 255)] = [255, 0, 0]  # [B, G, R]

# Afficher l'image résultante
cv2.imshow("Foreground", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
