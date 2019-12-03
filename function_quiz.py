def function1(n):
    alphabet = (
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" 
    )
    return alphabet[n]

def function2():
    return function1(7) + function1(4) + function1(24)

def function3(n):
    return function2() + " " + n

def function4(n):
    if n < 1:
        return None
    elif n > 26:
        return None
    else:
        return function1(n - 1)
