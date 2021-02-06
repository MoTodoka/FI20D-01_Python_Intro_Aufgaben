# Beim Cäsar-Chiffre wird jeder Buchstabe im Alphabet um eine fixe Anzahl an Zeichen shift verschoben. Ist der Shift z.B. 5 werden alle Buchstaben im Alphabet um 5 verschoben:

# Vorher: [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
# Danach: [f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a, b, c, d, e]

# Aus "hallo" wird also "mfqqt".

# Schreibe eine Funktion caesar(message, shift), die den Cäsar-Chiffre für Kleinbuchstaben umsetzt.

# Tipps: ord, chr

def caesar(message, shift):
    result = ""
    for char in message:
        result += chr(ord(char)+shift)
    return result

# print(caesar("hallo",5))