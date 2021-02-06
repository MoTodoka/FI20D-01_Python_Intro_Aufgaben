# Schreibe eine Funktion sort_list(input, direction), die eine sortierte Version der Liste input zurückgibt - aufsteigend, wenn direction = "ascending" angibt und absteigend bei direction = "descending".

# Zum Beispiel:
# Test 	                                Resultat
# input = [0, 1, 2, 4, 3];                [0, 1, 2, 3, 4]
# print(sort_list(input, "ascending"))    [0, 1, 2, 4, 3]
# print(input)

def sort_list(input, direction):
    return sorted(input, reverse=(direction == "descending"))


# input = [0, 1, 2, 4, 3]
# print(sort_list(input, "ascending"))
# print(input)

# input = [0, 1, 2, 4, 3]
# print(sort_list(input, "descending"))
# print(input)