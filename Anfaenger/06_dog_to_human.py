# Schreibe ein Funktion dog_to_human(dog_years), die das Alter eines Hundes dog_years in Menschjahre umrechnet und zurückgibt.
# Die Berechnung läuft wie folgt:

#     Hundejahre = 1 --> Menschenjahre = 14
#     Hundejahre = 2 --> Menschenjahre = 22
#     Hundejahre > 2 --> Menschenjahre = 22 + (Hundejahre - 2) * 5

# Zum Beispiel:
# Test:       print(dog_to_human(1))
# Resultat:   14

def dog_to_human(dog_years):
    if dog_years == 1:
        return 14
    if dog_years == 2:
        return 22
    if dog_years > 2:
        return 22 + (dog_years - 2) * 5

# print(dog_to_human(1))