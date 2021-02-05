# Schreibe eine Funktion minimum(a, b), die das Minimum der beiden Zahlen a und b zurückgibt.

# Zum Beispiel:
# Test:       print(minimum(1, 4))
# Resultat:   1

def minimum(a, b):
    if a < b:
        return a
    return b

# print(minimum(1, 4))