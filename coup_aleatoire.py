3.11 
def coup_aleatoire(gril, j):
	""" Permet de jouer un coup aléatoire pour le joueur j,
	On supposera que la grille n'est pas pleine,
	pour éviter une boucle infini
	"""
    	a = randint(0,6)
    	if coup_possible(gril, a) == True :
        			jouer(gril, j, a)
	return(gril)
