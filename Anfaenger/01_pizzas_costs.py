# Eine Pizza kostet euro_per_pizza Euro . Bestimme, wie viel Euro wir für num_pizzas Pizzen zahlen müssen. Schreibe eine Funktion pizzas_costs(euro_per_pizza, num_pizzas), die den Preis in Euro zurückgibt.

# Zum Beispiel:
# Test:       print(pizzas_costs(6, 3))
# Resultat:   18

def pizzas_costs(euro_per_pizza, num_pizzas):
    return euro_per_pizza * num_pizzas

# print(pizzas_costs(6, 3))