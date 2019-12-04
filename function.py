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

# displayElements( [4, 12, 15, 37, 56, 121] )


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


# Fonction permettant de calculer si le poids total de nos colis est trop lourd pour l'ascenseur
def isTooHeavy(boxes, totalWeight = 100):
    # Initialise le poids actuel à zéro
    currentWeight = 0
    # Pour chaque carton
    for weight in boxes:
        # Ajoute le poids du carton au poids actuel
        currentWeight = currentWeight + weight
        # Si le poids actuel dépasse 100 kg
        if currentWeight > totalWeight:
            # Renvoie vrai
            return True
    # Renvoie faux
    return False

print(isTooHeavy([11, 25, 45, 3, 63, 24]))  # Trop lourd
print(isTooHeavy([99]))  # Pas trop lourd
print(isTooHeavy([120]))  # Trop lourd
print(isTooHeavy([13, 24, 32])) # Pas trop lourd


# Détermine le nombre minimal de voyages en ascenseur pour envoyer les colis dans l'ordre
# dès que la collection de colis dépasse 100kg
def travels(boxes, totalWeight = 100):
    # Initialise le nombre de voyages
    travels = 1
    # Initialise le poids actuel à zéro
    currentWeight = 0
    # Pour chaque carton
    for weight in boxes:
        # Ajoute le poids du carton au poids actuel
        currentWeight = currentWeight + weight
        # Si le poids actuel est supérieur à 100
        if currentWeight >= totalWeight:
            # Incrémente (ajouter 1 à) le nombre de voyages
            travels += 1    # travels = travels + 1
            # Réinitialise le poids actuel
            currentWeight = 0
    # Renvoie le nombre de voyages
    return travels

print(travels([11, 25, 45, 20, 63, 24, 15, 34]))  # 3
print(travels([99]))  # 1
print(travels([54, 52, 43])) # 2
print(travels([13, 24, 32])) # 1


def findName(names, searchedName):
    n = 0
    for name in names:
        if name == searchedName:
            return n    # ou break si on est en-dehors d'une fonction
        n += 1
    return -1

print(findName(["Jean-Pierre", "Mireille", "Gertrude", "Michel", "Paul", "Jules", "Antoine"], "Martin"))
