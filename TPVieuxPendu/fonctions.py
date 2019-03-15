# -*- coding: cp1252 -*-
from donees import *
import random
import os
import pickle


def mot_hoazard (liste_mots):
    liste_mots=[x.lower() for x in liste_mots if len(x)<9]
    return liste_mots[random.randint(0,len(liste_mots)-1)]


def recup_lettre():
    lettre = input("Saisissez une lettre :")
    lettre=str(lettre)
    if len (lettre)>1 or not lettre.isalpha():
        print "vous n'avez pas saisi une lettre"
        return recup_lettre()
    else :
        return lettre.lower()

def affiche_result(lettres_recup,mot):
    result=""
    for lettres in mot :
        if lettres in lettres_recup:
            result+=lettres
        else:
            result+="*"
    return result 

def recup_nom():
    nom=input("Saisissez votre nom :")
    return(nom)

def calcul_score(essai,nb_coups):
    score = nb_coups-essai
    return score


def recup_score(nom_fichier_scores):
    if os.path.exists(nom_fichier_scores):
        fichier=open(nom_fichier_scores,"rb")
        mon_depickler = pickle.Unpickler(fichier)
        scores = mon_depickler.load()
        fichier.close()
    else:
        scores={}

    return(scores)



def enregistrer_scores(nom_fichier_scores,score):
    fichier=open(nom_fichier_scores,"wb")
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(score)
    fichier.close()





