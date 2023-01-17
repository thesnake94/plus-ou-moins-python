from random import randint 


nbEssaiMax = 4
nbEssaiJoueur = 1
chiffreJoueur = 0
chiffreOrdi = randint(0,9)

while chiffreJoueur != chiffreOrdi  and nbEssaiJoueur <= nbEssaiMax: 
    print("choisi un chiffre de 0 à 9 : " )
    chiffreJoueur = int(input())
    print("tu en es à l'essai n° " , nbEssaiJoueur , "n'oublies pas qu'il y a seulement " , nbEssaiMax , " essais !")
    if chiffreJoueur < chiffreOrdi :
        print("bien essayé mais c'est plus")

    elif chiffreJoueur > chiffreOrdi:
        print("bien essayé mais c'est moins")

    else :
        print("bien joué c'est gagné ! vous avez utilisé " , nbEssaiJoueur ," essais sur les " , nbEssaiMax , " possibles.")
    
    nbEssaiJoueur += 1
    
if nbEssaiJoueur > nbEssaiMax and chiffreJoueur != chiffreOrdi: 
    print("Et c'est fini ! tu as utilisé tous tes essais. J'avais choisi " , chiffreOrdi , " et tu ne l'as pas trouvé !" )

print("Merci d'avoir joué à ce jeu")