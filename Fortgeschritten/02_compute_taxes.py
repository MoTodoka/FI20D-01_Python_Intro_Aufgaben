# Der Steueramtchef von Trogland stellt dich an, um eine einfache Funktion compute_taxes(name, surname, income) in Python zu schreiben. Dieses Programm soll den Steuersatz jedes Steuerzahlers berechnen. Die Eingabeparameter sind:

#     Vorname und Nachname des Steuerzahlers
#     Einkommen (in Dublonen, die Währung von Trogland)

# Die Ausgabe soll von folgender Form sein:

#     Der Steuerzahler Vorname Nachname muss für das laufende Jahr X Dublonen dem Steueramt bezahlen.

# Der Steuersatz wird gemäss folgender Tabelle bestimmt:
# Einkommen E       | Steuersatz
# E≤10′000          | 40%
# 10′000<E≤30′000	| 55%
# 30′000<E≤70′000	| 75%
# E>70′000	        | 82%

def compute_taxes(name, surname, income):
    tax = income * get_tax_percentage(income) / 100
    # print("Der Steuerzahler", name, surname, "muss für das laufende Jahr", tax, "Dublonen dem Steueramt bezahlen.")
    # Dies war mein erster Abgabeversuch. Hier wurde die Steuer als float mit einer Nachkommastelle ausgegeben.
    # Diese Lösung wurde als falsch gewertet. In der Aufgabe sehe ich aber keinen Hinweis darauf, dass hier ein Integer erwartet wird.
    # Frage:    Ist round() hier eine sinnvolle Lösung? Sollten wir, da wir mit Geldwerten arbeiten nicht besser mit mehr präzision arbeiten?
    #           Kann Python ein stringf/printf (formatierten string) oder kann ich den Wert irgendwie in einen Integer casten?
    print("Der Steuerzahler", name, surname, "muss für das laufende Jahr", round(tax), "Dublonen dem Steueramt bezahlen.")

def get_tax_percentage(income):
    if income <= 10000:
        return 40
    if income > 10000 and income <= 30000:
        return 55
    if income > 30000 and income <= 70000:
        return 75
    if income > 70000:
        return 82

# compute_taxes("Tom","Taube",5000)
# compute_taxes("Simon","Simsalabim",50000)
# compute_taxes("Bernd","Bunge",500000)