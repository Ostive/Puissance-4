def coup_possible(gril,col):
#Détermine si il est possible de jouer dans la colonne col
#Prend en argument la grille, tableau 5x6 avec la position des pions des joeueurs et un entier (numéro de la colonne entre 0 et 6)
#Renvoie True si possible de jouer, False sinon
    col1=[gril[i][col] for i in range(len(gril))]
    if 0 in col1:
        return(True)
    else:
        return(False)
assert coup_possible([[0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 1]],6)==False
assert coup_possible([[0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0]],5)==True
