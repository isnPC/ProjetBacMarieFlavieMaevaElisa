# ProjetBacMarieFlavieMaevaElisa
Voici notre projet bac en ISN, en groupe de 4.

import tkinter as tk
# pour utiliser un objet tkinter on fera précéder le nom par tk.

fenetre = tk.Tk()
fenetre.title("Jeu du rébus")

def niveau ():
    """Entrée : demande quel est le niveau choisi
    Sortie : renvoie le nombre d’indices maximal et lance la partie"""
    difficulte = 0
    if difficulte != 1 or difficulte != 2 or difficulte != 3:
        print ("Veuillez choisir votre niveau, 1, 2 ou 3")
        difficulte = int(input("Choisissez le niveau de difficulté : 1 expert (6 indices maximum) 2 : confirmé (4 indices maximum) 3 : Débutant (2 indices maximum)"))
    if difficulte == 1:
        return 6
    elif difficulte == 2:
        return 4
    else :
        return 2

label = tk.Label(fenetre, text="Jeu du Rébus")
label.grid()

Label1 = tk.Label(fenetre, text ="Bienvenu(e) dans le jeu du rébus ! Le but est simple : à partir de la suite d'images qui vous est montrée, devinez la phrase ou le mot caché en assemblant les syllabes que forment les différentes images. Vous pourrez choisir un niveau entre 3 niveaux;")
Label1.grid()

label2 = tk.Label(fenetre, text = "niveau 1 = 6 indices, niveau 2 = 4 indices et niveau 3 = 2 indices, les indices vous aideront à trouver la solution si vous êtes bloqués !")
label2.grid()

label3 = tk.Label (fenetre, text = "Votre score sera calculé et affiché au fur et à mesure du jeu, vous gagnerez 3 points si vous trouvez la solution sans cliquer sur le bouton 'indice', 2 points si vous utilisez la moitié de vos indices, et un seul point s'il vous a fallu tous vos indices.")
label3.grid()

label4= tk.Label(fenetre, text= "Vous pouvez quitter le jeu en cliquant sur le bouton quitter à tout moment. Bonne chance !")
label4.grid()

def newFenetre():
    newWindow = tk.Toplevel(fenetre)

start = tk.Button(fenetre, text = "Commencer une partie", command = newFenetre)
start.grid(row= 7, column=0)

indice = tk.Button(fenetre, text='Indices', command = list)
indice.grid(row = 6, column = 1)

quitter = tk.Button(fenetre, text='Quitter', command = fenetre.destroy)
quitter.grid(row = 15, column=0)

fenetre.mainloop()
