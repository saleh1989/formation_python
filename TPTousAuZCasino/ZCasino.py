# -*- coding: cp1252 -*-
from random import *
#numero a miser doit etre compris entre 0 et 49

num=-1
somme=-1
while (num >49 or num<0):
    
    try:
        num = input("Saisissez une numero compris entre 0 et 49 :")
        num = int(num) # Conversion de l'année
        assert (num > 0 and num < 49)
    except NameError:
        print "la variable n'a pas été définie"
    except ValueError:
        print "Vous n'avez pas saisi un nombre."
    except AssertionError:
        print "Le numero saisie n'est pas compris entre 0et 49 ."

while (somme <= 0):
    try:
        somme = input("Saisissez la somme que vous souhaite miser:")
        somme = int(somme) # Conversion de l'année
        assert (somme > 0)
    except NameError:
        print "la variable n'a pas été définie"
    except ValueError:
        print "Vous n'avez pas saisi un nombre."
    except AssertionError:
        print "La somme saisie est négative ."


num_gangant=randrange(50)
print num_gangant

if (num_gangant==num):
    gain=somme*3
elif(num_gangant % 2 == num % 2):
    gain=ceil(somme/2)
else:
    gain=0
print gain
    
        

