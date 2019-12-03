# Renvoie la n-ème lettre de l'alphabet (en partant de 0)
def getLetter(number):
    alphabet = (
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" 
    )
    return alphabet[number]

# Renvoie le mot "hey"
def getHey():
    return getLetter(7) + getLetter(4) + getLetter(24)

# Renvoie "hey" suivi du nom passé en paramètre
def getHeyName(name):
    return getHey() + " " + name

# Renvoie la n-ème lettre de l'alphabet (à partir de 1) en vérifiant
# que la valeur n est bien comprise entre 1 et 26
def getLetterFrom1(number):
    if number < 1:
        return None
    elif number > 26:
        return None
    else:
        return getLetter(number - 1)
