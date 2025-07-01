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

price = 59
txt = f"The price is {float(price) + 0.4} dollars"
print(txt)


x = 200
print(isinstance(x,float)) //int wäre richtig statt float, schauen ob es richtig ist oder nicht

x = 10
y = 2
z = x % y

if z != 0 or x < 2:
    print(f"Die Zahl {x} ist ungerade")
else:
    print(f"Die Zahl {x} ist gerade")

list_test = ["apple", "banana", "strawberry", 4, 2]
for i in range(len(list_test)):
    print(list_test[i])

# Listen ---------------------------------------- 2ter Tag  = Jun 27
mylist = ['apple', 'banana', "cool"]
mylist[2] = "nicht cool"
mylist[:2] = ['eckelhaft', 'geil']
tropical = ["mango neu"]
#oder inserting, aber nicht replacen
mylist.insert(2, "übel")
#add list items
mylist.append("orange")
#extend list ( listen zusammenfügen)
mylist.extend(tropical)

#remove saschen aus der liste (spezifisch den Namen wissen)
mylist.remove("orange")
#pop, removen nur stelle wissen
mylist.pop(2)
#oder del
del mylist[0]
#clear list, komplett auslöschen
#mylist.clear()

#loop listen -----------
#alle sachen in einer Liste aufzählen
for x in mylist:
    print(x)
#druch index nummern
for i in range(len(mylist)):
    print(mylist[i])
#while loop
p = 0
while p < len(mylist):
    print(mylist[p])
    p += 1
#comprehension shortest syntaax loop
[print(x) for x in mylist]

#listen comprehension
#Unterscheid for undcomprehension
newlist = []
for x in mylist:
    if 'a' in x:
        newlist.append(x)


    newlist = [x for x in mylist if 'a' in x]
#The Syntax
#newlist = [expression for item in iterable if condition == True]
# nicht gleich appfel
newlist = [x for x in mylist if x != "cool"]
newlist = [x for x in range(10) if x <5]
newlist = [x.upper() for x in mylist]
newlist = [x if x != "banana" else "orange" for x in mylist]

print(newlist)
print(mylist, len(mylist))

#Sort list------------------
obst_Salat = ["orange", "mango", "kiwi", "pineapple", "banana"]
#alphabet sortieren
obst_Salat.sort()
# und reverse
nummer_Liste = [100,20,40,10,1,5,6,7,3,4,5,6,4,5,3]
nummer_Liste.sort(reverse = True)

#generell reverse
nummer_Liste.reverse()


#copy lists- ---------------------
    #list1 = list2 geht nicht, weil wenn eins geändert, dann das andere auch also copy
neue_liste = nummer_Liste.copy()
neue_liste = list(nummer_Liste)

#join list
#normal
zusammen_Gefuegt = neue_liste + nummer_Liste
#for loop in die erste liste
for x in nummer_Liste:
    zusammen_Gefuegt.append(x)
# extend
neue_liste.extend(nummer_Liste) #print neue liste

print("\nNeue Liste \t\t",neue_liste, len(neue_liste))
print("\tNummer Liste \t", nummer_Liste, len(nummer_Liste))
print("\t\tObst Salat\t\t",obst_Salat, len(obst_Salat))
print("\t\t\tZusammen gefügte Liste\t\t",zusammen_Gefuegt, len(zusammen_Gefuegt))

#-------------------------Tuples
tuple_Test = ("regen", "wind", "storm", "noch was")
#tuple mit einer item, brauchen hinten ein Komma
tuple_Eins = ("test Schon?",)
print(type(tuple_Eins))
#packing and unpacking, * speichert alle verbleiblichen zu einer liste
(gut, sehr_gut, *joa) = tuple_Test
#gleiche geht auch in der Mitte
(eins, *zwei, drei) = tuple_Test
print(zwei)
#ausgabe mit index numbers
for x in range(len(tuple_Test)):
    if tuple_Test[x] == "regen":
        print(tuple_Test[x])
#asugabe mit while loop
i = 0
while i < len(tuple_Test):
    print(tuple_Test[i])
    i += 1
#join tuples
tuple3 = tuple_Test +  tuple_Eins
tuple4 = tuple3 * 20
print(tuple4)

#python sets--------------------------------------------------
myset = {"apple", "banana", "cherry"}
#addieren
myset.add("orange")
print(myset)
#zusammenführen können auch listen oder tuples oder alles mögliche sein
myset2 = {"lol", "mega", "mind"}
myset.update(myset2)
#remove
myset.remove("apple")
#oder
myset.discard("apple")
#random item
myset.pop()
#clear
myset.clear()
#delete
del myset
#loops
for x in myset2:
    print(x)
print(myset2)


"""

#dictionaries -------------------------------------

thisDict = {
    "marke": "BMW",
    "viersitzer": True,
    "PS": 200,
    "Jahr": 1964,
    "verkäufer": "kp"
}

#dictonaries or kurz dict, abfragen
print(thisDict)
x = thisDict["marke"]
print(f"Die Marke ist {x}!")

#dict erstellen v2
testDict = dict(name = "Aaron", alter = 4, land = "deutschland")
print(testDict)
