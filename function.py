# Def = mot-clé qui permet de déclarer une fonction
# addNumbers = nom de la fonction (libre, comme les noms de variables)
# () = la ou les entrées, avec le nom de variable qu'on souhaite leur donner, séparées par une virgule
# : = ouvrir un bloc
def addNumbers(number1, number2):
    # Début de la fonction, indentation

    # return = renvoyer la valeur à l'endroit où on a appelé la fonction
    return number1 + number2
# Fin de la fonction, on retire l'indentation


def isPositive(number):
    # Si le nombre est inférieur à zéro
    if number < 0:
        # Renvoie faux
        return False
    # Sinon, si le nombre est supérieur à zéro
    elif number > 0: 
        # Renvoie vrai
        return True
    # Sinon
    else:
        # Renvoie None
        return None


# Commentaires inutiles, mais importants à versionner quand même
resultat = addNumbers(-6, addNumbers(2, 5))
print("resultat =", resultat)
print("resultat est-il positif?", isPositive(resultat))

displayElements( [4, 12, 15, 37, 56, 121] )
