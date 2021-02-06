# Dies ist eine Anfängeraufgabe, die gerne für ein erstes Aussieben bei Bewerbungsgesprächen gestellt wird, da tatsächlich erstaunlich viele Bewerber die Aufgabe falsch lösen oder zu viel Zeit dafür benötigen.

# Aufgabe:
# Schreibe eine Funktion fizzbuzz(), die alle Zahlen von 1 bis 100 ausgibt. Wenn die Zahl allerdings ein Vielfaches von 3 ist, soll statt der Zahl das Wort "Fizz" ausgegeben werden. Wenn die Zahl ein Vielfaches von 5 ist, soll statt der Zahl das Wort "Buzz" ausgegeben werden. Ist die Zahl sowohl ein Vielfaches von 3 als auch von 5, soll statt der Zahl das Wort "FizzBuzz" ausgegeben werden.

# Zum Beispiel:
# Test 	    Resultat
# fizzbuzz()  1
#             2
#             Fizz
#             4
#             Buzz
#             Fizz
#             7
#             8
#             Fizz
#             Buzz
#             11
#             Fizz
#             13
#             14
#             FizzBuzz
#             16
#             17
#             Fizz
#             19
#             Buzz
#             Fizz
#             22
#             23
#             Fizz
#             Buzz
#             26
#             Fizz
#             28
#             29
#             FizzBuzz
#             31
#             32
#             Fizz
#             34
#             Buzz
#             Fizz
#             37
#             38
#             Fizz
#             Buzz
#             41
#             Fizz
#             43
#             44
#             FizzBuzz
#             46
#             47
#             Fizz
#             49
#             Buzz
#             Fizz
#             52
#             53
#             Fizz
#             Buzz
#             56
#             Fizz
#             58
#             59
#             FizzBuzz
#             61
#             62
#             Fizz
#             64
#             Buzz
#             Fizz
#             67
#             68
#             Fizz
#             Buzz
#             71
#             Fizz
#             73
#             74
#             FizzBuzz
#             76
#             77
#             Fizz
#             79
#             Buzz
#             Fizz
#             82
#             83
#             Fizz
#             Buzz
#             86
#             Fizz
#             88
#             89
#             FizzBuzz
#             91
#             92
#             Fizz
#             94
#             Buzz
#             Fizz
#             97
#             98
#             Fizz
#             Buzz

def fizzbuzz(start=1, lines=100):
    for i in range(start, lines + start):
        out = ""
        out += "Fizz" if i % 3 == 0 else ""
        out += "Buzz" if i % 5 == 0 else ""
        out = i if out == "" else out
        print(out)


# fizzbuzz()
