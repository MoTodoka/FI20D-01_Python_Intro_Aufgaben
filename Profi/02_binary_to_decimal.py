# Schreibe eine Funktion binary_to_decimal(binary_string), die für eine Binärzahl, gegeben als String, den Dezimalwert berechnet.

# Beispiel:  "010010000110000101101100011011000110111100100001"

def binary_to_decimal(binary_string):
    return int(binary_string,base=2)

# print(binary_to_decimal("010010000110000101101100011011000110111100100001"))