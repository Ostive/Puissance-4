# Puissance0100
Jeu
def horiz(gril, j, lig, col):
#gril : la grille de pions; j : le joueur, un entier défini par 1 ou 2 ;
#lig : la ligne, un entier avec la valeur entre 0 et 5 ; col : la   colonne, un entier avec la valeur entre 0 et 3
	compteur = 0
	for u in range(4):
    		if gril[lig][col] == gril[lig][u+col] and gril[lig][u+col] == j :
            			compteur += 1
    		else:
            			compteur -= 1
	if compteur >= 4 :
        		return(True)
	else:
        		return(False)

