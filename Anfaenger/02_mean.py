# Schreibe eine Funktion mean(list_of_integers), die den Mittelwert der Liste von Ganzzahlen list_of_integers berechnet.

# Beispiel: list_of_integers = [2, 3, 4]

# Dann ist der Mittelwert (2 + 3 + 4)/ 3 = 3

# Zum Beispiel:
# Test:     print(mean([2,3,4]))
# Resultat: 3.0

def mean(list_of_integers):
    summe = 0
    for i in list_of_integers:
        summe += i
    return summe / len(list_of_integers)

# print(mean([2,3,4]))