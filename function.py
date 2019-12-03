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


def displayElements(list):
    for element in list:
        print(element)


def isLegal(age):
    # Si l'âge est négatif
    if age < 0:
        # Arrête le programme et génère un message d'erreur
        raise Exception("Age must be a positive integer")
    # Sinon, si l'âge est supérieur à 18
    elif age >= 18:
        # Renvoie vrai
        return True
    # Sinon
    else:
        # Renvoie faux
        return False


# Commentaires inutiles, mais importants à versionner quand même
resultat = addNumbers(-6, addNumbers(2, 5))
print("resultat =", resultat)
print("resultat est-il positif?", isPositive(resultat))

displayElements( [4, 12, 15, 37, 56, 121] )


def displayAges(ages):
    # Pour chaque âge présent dans la liste
    for age in ages:
        # Afficher l'âge
        print(age)
        # Si cet âge ne correspond PAS à une personne majeure OU s'il est supérieur ou égal à 60 ans
        if not isLegal(age) or age >= 60:
            # Affiche "réduction"
            print("réduction")
        # Si cet âge ne correspond PAS à une personne majeure ET s'il est supérieur ou égal à 15 ans
        if not isLegal(age) and age >= 15:
            # Affiche "tarif spécial"
            print("tarif spécial")


displayAges( (15, 17, 21) )
displayAges( (3, 12, 21, 15, 53, 62, 9, 0, 18, 75) )
