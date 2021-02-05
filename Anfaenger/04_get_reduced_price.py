# Gegeben ist ein Preis price und ein Rabatt in Prozent (discount). Schreibe eine Funktion get_reduced_price(price, discount), die den Restpreis nach Abzug des Rabatts zurcükgibt.

# Zum Beispiel:
# Test:       print(round(get_reduced_price(10, 25), 1))
# Resultat:   7.5

def get_reduced_price(price, discount):
    discount_value = price * discount / 100
    reduced_price = price - discount_value
    return reduced_price

# print(round(get_reduced_price(10, 25), 1))