# Ich brauche ein Programm für die Notenvergabe. Die Abschlussnote hängt von den folgenden Parametern ab:

#     Prüfungsnote base_grade (von 1 bis 6 mit Halbpunkten, .5);
#     Augenfarbe (z.B. dunkel=1, hell=0);
#     Frisur (z.B. kurze Haare=1, lange Haare=0);
#     Wetter (z.B. schön=1, nicht schön=0).

# Es gilt folgendes:

#     Hat der Prüfling dunkle Augen und…
#         kurze Haare, so wird die Abschlussnote um 10% erhöht (d.h. Abschlussnote = Prüfungsnote + 10% Prüfungsnote).
#         lange Haare, so wird die Abschlussnote um 10% reduziert.
#     Hat der Prüfling helle Augen und…
#         kurze Haare, so wird die Abschlussnote um 10% reduziert.
#         lange Haare, so wird die Abschlussnote um 10% erhöht.
#     Ist das Wetter schön, so wird die Abschlussnote um eine Einheit reduziert.
#     Die Abschlussnoten müssen auf halbe Noten gerundet werden.

# Schreibe eine Funktion compute_grade(base_grade, eye_color, hair, weather), die die Note berechnet.

# Hinweis: Wie kann man auf halbe Noten runden? Die Funktion round() rundet auf ganze Noten, z.B. round(5.4) = 5 aber round(5.4*2) = 11… ;)

## Meine Notizen:
#  eye_color == 1 && hair == 1 -> +10%
#  eye_color == 0 && hair == 0 -> +10%
#  eye_color == 1 && hair == 0 -> -10%
#  eye_color == 0 && hair == 1 -> -10%

def compute_grade(base_grade, eye_color, hair, weather):
    result = base_grade
    if eye_color != hair:
        result -= get_modifier(base_grade)
    else:
        result += get_modifier(base_grade)
    if weather == 1:
        result -= 1
    return round(result*2) / 2


def get_modifier(base_grade, percentage=10):
    return (base_grade * percentage / 100)


# print(compute_grade(3, 0, 1, 0))
# print(compute_grade(3, 1, 0, 0))
# print(compute_grade(3, 0, 0, 0))
# print(compute_grade(3, 1, 1, 0))
# print(compute_grade(3, 1, 1, 1))
