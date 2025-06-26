"""
Data Types:
-----------
str, list, tuple, range, dict, set, frozenset, bytes, bytearray, memoryview, NoneType

Beispiele:
----------
# String
x = "hi"

# Integer
x = 20

# Tuple
x = (3, 4, 5, 2)

# List
z = [10, 20, 30, 40]

# String
y = "hi"

# Dictionary
o = {"name": "john", "age": 36}

# Ausgabe
print(y + "\n", z, "\n", x, "\n", o, "\n")

# NoneType
p = None

-------------------------------
Datentyp anzeigen:
-------------------------------
x = "hay"
print(type(x))

-------------------------------
Typumwandlung:
-------------------------------
x = 1  # int
a = float(x)
print(a)

-------------------------------
Zufallswerte & String-Zugriff:
-------------------------------
import random

# Zufälliger Wert aus einem Bereich
print(random.randrange(1, 10))

# Zufälliger Pfeil aus Liste
s = ["->", "=>", "~>"]
a = "Aaron"
print("Der dritte Buchstabe meines Namens ist {pfeil}".format(pfeil=random.choices(s)[0]), a[2], "\n")

# Zeichen zählen (korrekte Einrückung für die Schleife!)
for char in "banana":
    print(len(char))  # Hinweis: len(char) ist immer 1

-------------------------------
Text überprüfen:
-------------------------------
txt = "the best free"
print("\n\n")
if "free" in txt:
    print("Yes, 'free' is present")

-------------------------------
Slicing:
-------------------------------
x = 'welcome'
print(x[3:6] + "\t", x[:6] + "\t", x[3:] + "\t", x[-2:6] + "\t")

-------------------------------
String-Modifikation:
-------------------------------
a = "  ich     Kann Alles sein  "
print(a.upper() + "\t |", a.lower() + "\t |", a.strip() + "\n", a.replace("Ka", "J") + "\n", a.split("a"))
"""


