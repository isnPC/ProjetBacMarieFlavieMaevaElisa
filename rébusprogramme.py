import tkinter as tk
# pour utiliser un objet tkinter on fera précéder le nom par tk.

from random import randint

from PIL import Image, ImageTk

fenetre = tk.Tk()
fenetre.title("Jeu du rébus")

# on crée un canvas pour pouvoir insérer une photo
image1 = tk.Canvas(fenetre, width=100,height=100, bg="black")
image1.grid(row=1, column=1)
# grace à PIL on insère la photo dans le canvas
# image redimensionnée grace à paint avec un longueur ou lageur maximale de 100px mais on peut changer ces dimensions
pilImage1 = Image.open("test1.jpg")
imag1 = ImageTk.PhotoImage(pilImage1)
imagesprite1 = image1.create_image(50,50,image=imag1) # les deux 50 correspondent au centre de la photo

image2 = tk.Canvas(fenetre, width=100,height=100, bg="black")
image2.grid(row=1, column=2)
pilImage2 = Image.open("test.jpg")
imag2 = ImageTk.PhotoImage(pilImage2)
imagesprite2 = image1.create_image(50,50,image=imag2)

label = label(fenetre, text ="Bienvenu(e) dans le jeu du rébus ! Le but est simple : à partir de la suite d'images qui vous est montrée, devinez la phrase ou le mot caché en assemblant les syllabes que forment les différentes images. vous pourrez choisir un niveau entre 3 niveaux;"
        "niveau 1 = 6 indices, niveau 2 = 4 indices et niveau 3 = 2 indices, les indices vous aideront à trouver la solution si vous êtes bloqués !"
        "Votre score sera calculé et affiché au fur et à mesure du jeu, vous gagnerez 3 points si vous trouvez la solution sans cliquer sur le bouton 'indice', 2 points si vous utilisez la moitié de vos indices, et un seul point s'il vous a fallu tous vos indices."
        "Vous pouvez quitter le jeu en cliquant sur le bouton quitter à tout moment. Bonne chance !")
label.pack()

indice = tk.Button(text='Indices', command = fenetre.bbox)
indice.grid(row = 2, column = 5)

quitter = tk.Button(text='Quitter', command = fenetre.destroy)
quitter.grid(row=8, column=1)

fenetre.mainloop()