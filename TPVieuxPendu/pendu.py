# -*- coding: cp1252 -*-
from donees import *
from fonctions import *

score=recup_score(nom_fichier_scores)
mot= mot_hoazard(liste_mots)
lettres_recup=[]
essai=0
utilisateur=recup_nom()

if utilisateur not in score.keys() :
    score[utilisateur]=0

while essai < nb_coups:
    lettres_recup.append(recup_lettre())
    result=affiche_result(lettres_recup,mot)
    print result
    if result==mot:
        print "mot trouver"
        break
    else:
        essai+=1

score[utilisateur]=calcul_score(essai,nb_coups)
print 'votre score est' score[utulisateur] 
enregistrer_scores(nom_fichier_scores,score)

