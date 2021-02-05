# Schreibe eine Funktion get_brutto(netto), die den Bruttobetrag für den Nettobetrag netto berechnet.

# Zum Beispiel:
# Test: 	    print(round(get_brutto(10), 1));
# Resultat:   11.9

def get_brutto(netto):
    brutto = netto + netto * 0.19
    return brutto

# print(round(get_brutto(10), 1))