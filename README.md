#Puissance4
Jeu

def grille_vide():
    """fonction construit un tableau 6*7
    6 ligne 7 colonne
    chaque case ==0
    ne prend pas d'argument
    renvoie le tableau"""
    a=[[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]]
    return(a)

def affiche(gril):
    """ Fonction affiche(gril): affiche une grille de 6 lignes sur 7 colonnes.
            arguments :
                Un tableau de 6 x 7
                           Les lignes sont notées lig, et sont des entiers compris entre 0 et 5,
        la ligne 0 est située en bas.
                Les colonnes sont notées col, et sont des entiers compris entre 0 et 6,
        la colonne 0 est située à gauche.
    Dans la grille :
        0 représente une case vide, représentée par un “.”
        1 représente un pion du joueur 1, représenté par un “x”
        2-                       du joueur 2,-          -“0” 
   """

    lig,col = len(gril),len(gril[0])
    print(' ', end = '')
    for z in range(7):
            print(z,'', end = '')
            if z == 6:
                    print()
    for i in range(lig):
            for j in range(col):
                    if gril[i][j] == 0 :
                            print('|.',end='')
                            if j == 6:
                                print("|")
                    elif gril[i][j] == 1:
                            print('|x',end='')
                            if j == 6:
                                print("|")
                    elif gril[i][j] == 2:
                            print('|0',end='')
                            if j == 6:
                                print("|")
def coup_possible(gril,col):
"""Détermine si il est possible de jouer dans la colonne col
Prend en argument la grille, tableau 5x6 avec la position des pions des joeueurs et un entier (numéro de la colonne entre 0 et 6)
Renvoie True si possible de jouer, False sinon"""
    col1=[i[col] for i in gril]
    if 0 in col1:
        return(True)
    else:
        return(False)                                
