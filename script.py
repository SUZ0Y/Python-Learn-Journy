"""
Data types
str,
list, tuple, range,
 dict,
  set, frozenset,
  bytes, bytearray, memoryview,
  noneType

-------------------
#str x = "hi"
#int x = 20
x = (3, 4, 5 ,2)
z = [10, 20, 30 , 40]
y = "hi"
o = {"name" : "john", "age" : 36}
print(y + "\n",
      z, "\n",
      x, "\n",
      o, "\n",
      )
      p = none
      ----------------------------------
      x = "hay"
        print(type(x))
        ----------------
    converter
    x = 1 // int
    a = float(x)
    print(a)

    import random
    print(random.randrange(1,10))

import random
s = ["->", "=>", "~>"]
a = "Aaron"
print("Der dritte Buchstabe mein Namens ist {pfeil} ".format(pfeil = random.choices(s)[0]), a[2], "\n")

for x in "banana":
    print (len(x))

txt = "the best free"
print("\n\n")
if "free" not in txt:
    print("Yes, 'free' is present")


#slicing
x = 'welcome'
print(x[3:6] + "\t", x[:6] + "\t", x[3:] + "\t", x[-2:6] + "\t")

#modify strings
a = "  ich     Kann Alles sein  "
print(a.upper() + "\t |", a.lower() + "\t |",
      a.strip() + "\n",
      a.replace("Ka", "J") + "\n",
      a.split("a"))





"""




