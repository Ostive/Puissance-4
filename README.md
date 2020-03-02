# Puissance-4
Jeu
def grille_vide():
    """Fonction construit un tableau 6 lignes sur 7 colonnes.
       Chaque case est remplie par un 0.
       Renvoie le tableau.
    """
    
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
    r = [-i for i in range(1,7)]
    for i in r:
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

    col1=[gril[i][col] for i in range(len(gril))]
    if 0 in col1:
        return(True)
    else:
        return(False) 
        
 def jouer(gril, j ,col):
    """ Fonction jouer(gril, j, col): joue un coup du joueur j dans la colonne col de la grille.
            arguments :
                Un tableau de 6 x 7 (ou 5 x 6 avec les indices)
                j, le joueur : un entier valant 1 ou 2
                col une colonne non pleine, un entier compris entre 0 et 6
            Si j = 1, la première case vide de la colonne col prendra la valeur 1
               j = 2,-                                                         -2
    Renvoie la grille après le coup
    """
    
    cpt = 6
    for z in range(6):
                if gril[-z][col] == 0 :
                    cpt -= 1
    gril[cpt][col] += j
    return(gril)
    
def horiz(gril, j, lig, col):
    """ Détermine si le joueur j aligne 4 pions à l'horizontale
        arguments :
                gril : la grille avec les pions.
                j, un entier avec pour valeur 1 ou 2
                lig la ligne, entier compris entre 0 et 5
                col la colonne, entier compris entre 0 et 3
        Renvoie True si c'est le cas
    """
    compteur = 0
    
    if col <= 3 and col >= 0 and lig <= 5 and lig >= 0:
        for u in range(4):
            if gril[lig][col] == gril[lig][u+col] and gril[lig][u+col] == j :
                        compteur += 1
            else:
                        compteur -= 1
    else :
        return(False)
        
    if compteur >= 4 :
                return(True)
    else:
                return(False)
  
  def vert(gril, j, lig, col):
    """ Détermine si le joueur j aligne 4 pions à la verticale
        arguments :
                gril : la grille avec les pions.
                j, un entier avec pour valeur 1 ou 2
                lig la ligne, entier compris entre 0 et 2
                col la colonne, entier compris entre 0 et 6
        Renvoie True si c'est le cas
    """

    compteur = 0
    
    if lig <= 2 and lig >= 0 and col >=0 and col <= 6:
            for u in range(4):
                if gril[lig][col] == gril[lig+u][col] and gril[lig+u][col] == j :
                        compteur += 1
                else:
                        compteur -= 1
    else :
        return(False)
	
    if compteur >= 4 :
                return(True)
    else:
                return(False)
                
 def diag_bas(gril, j, lig, col):
    """ Détermine si le joueur j aligne 4 pions en diagonale ascendante
        arguments :
                gril : la grille avec les pions.
                j, un entier avec pour valeur 1 ou 2
                lig la ligne, entier compris entre 3 et 5
                col la colonne, entier compris entre 0 et 6
        Renvoie True si c'est le cas
    """

    compteur_1 = 0

    if lig >= 3 and lig <= 5 and col >= 0 and col <= 6 :
        if col > 2 :
            for u in range(4):
                if gril[lig][col] == gril[lig-u][col-u] and gril[lig-u][col-u] == j:
                        compteur_1 += 1
                else:
                        compteur_1 -= 1
        elif col <= 2 :
            for u in range(4):
                if gril[lig][col] == gril[lig-u][col+u] and gril[lig-u][col+u] == j:
                        compteur_1 += 1
                else:
                        compteur_1 -= 1
    else :
        return(False)

    if compteur_1 >= 4 :
                return(True)
    else:
                return(False)
                
   def diag_haut(gril, j, lig, col):
    """ Détermine si le joueur j aligne 4 pions en diagonale descendante
        arguments :
                gril : la grille avec les pions.
                j, un entier avec pour valeur 1 ou 2
                lig la ligne, entier compris entre 0 et 2
                col la colonne, entier compris entre 0 et 6
        Renvoie True si c'est le cas
    """
    compteur_1 = 0
    
    if lig >= 0 and lig <= 2 and col >= 0 and col <= 6 :
        if col > 3 :
            for u in range(4):
                if gril[lig][col] == gril[lig+u][col-u] and gril[lig+u][col-u] == j:
                            compteur_1 += 1
                else:
                            compteur_1 -= 1
        elif col <= 3 :
            for u in range(4):
                if gril[lig][col] == gril[lig+u][col+u] and gril[lig+u][col+u] == j:
                            compteur_1 += 1
                else:
                            compteur_1 -= 1
    else :
        return(False)
        
    if compteur_1 >= 4 :
                return(True)
    else:
                return(False)
                
 def victoire(gril, j, lig, col):
    """ Renvoie True si le joueur j a gagné, False sinon.
    Fait appel aux fonctions horiz(), vert(), diag_haut() et diag_bas()
    """
    
    cpt_v = 0
    for lig in range(6):
            for col in range(7):
                    if horiz(gril, j, lig, col) == True :
                            cpt_v +=1
                    elif vert(gril, j, lig, col) == True :
                            cpt_v +=1
                    elif diag_haut(gril, j, lig, col) == True :
                            cpt_v +=1
                    elif diag_bas(gril, j, lig, col) == True :
                            cpt_v +=1
    if cpt_v > 0 :
            return(True)
    else :
            return(False)
            
def match_nul(gril):

    if 0 in gril[5]:
        return(False)
    else:
        return(True) 
