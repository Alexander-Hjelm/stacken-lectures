###############
# OPERATIONER
###############


###############
# - Nummer
###############

# De fyra räknesätten finns definerade i python:
a = 1 + 1 # a = 2
b = 5 - 1 # b = 4
c = 4 * 5 # c = 20
d = 9 / 3 # d = 3

# Det går att kombinera heltal, decimaltal eller blanda båda
e = 1.1 + 9.91 # e = 11.01
f = 9 * 10.1 # f = 90.9

# Det går också att mellanlagra variabler för komplicerade uträkningar
g = 9 * 10.1 # g = 90.9
h = g / 3 # h = 30.3
print(h) # output: 30.3

# Även modulooperatorn är definerad i python
i = 7 % 4 # i = 3
# Det är också floor division (dividera och avrunda neråt)
j = 19 / 4 # j = 4


###############
# - Booleans
###############
# Booleans har bara en egen operator: not, som inverterar ett påstående
a = not True # a = False
b = False
c = not b # c = True

# Python har 6 inbyggda operatorer för jämförelse av uttryck, som alla ger tillbaka en Boolean
# ==, Är lika med
d = ("Hej" == "Hej") # d = True
e = ("Hej" == "Då") # e = False
# !=, Är inte lika med
f = ("Hej" != "Då") # f = True
# <, Är mindre än
g = (1.0 < 2.0) # g = True
# >, Är större än
h = (10.0 > 9.9) # h = True
# <=, Är mindre än eller lika med
i = (9.9 <= 10.0) # i = True
j = (10.0 <= 10.0) # j = True
k = (10.1 <= 10.0) # k = False
# >=, Är större än eller lika med
i = (10.0 >= 10.0) # i = True
i = (11.0 >= 10.0) # i = True


###############
# - Strängar
###############

## Lite användbara strängmetoder:

## startswith
# Ger en boolean som säger om en sträng börjar med en substräng eller inte
text = "Detta är en exempelsträng"
s = text.startswith("Detta") # s = True

## endswith
# Ger en boolean som säger om en sträng slutar med en substräng eller inte
text = "Hej, jag heter olle"
s = text.endswith("olle") # s = True

## find
# Kollar om en delsträng finns i en större sträng eller inte
# Om delsträngen finns returneras platsen i den större strängen där delsträngen börjar
# Annars returneras -1
text = "En bonde som heter bosse";
f = text.find("bo") # f = 3
# Man kan också specificera på vilken plats sökningen ska börja.
f = text.find("bo", 4) # f = 19   -- Hittar den andra förekomsten av "bo" i "bosse"
f = text.find("bo", 20) # f = -1    -- Hittar varken "bonde" eller "bosse", båda ligger före plats 20

## split
# Delar upp en sträng i en Lista av strängar, separerade av mellanrum
text = "Imperiet slår tillbaka"
s = text.split() # s = ['Impertiet', 'slår', 'tillbaka']
# Om man vill splitta på ett annat tecken än mellanrum går det också bra
text2 = "Kebab, Pizza, Ananas"
s = text2.split(", ") # s = ['Kebab', 'Pizza', 'Ananas']

## join
# Bygger ihop en text av en Lista
del_ord = ['Kebab', 'Pizza', 'Ananas']
mat = "".join(del_ord) # mat = 'KebabPizzaAnanas'
mat = ", ".join(del_ord) # mat = 'Kebab, Pizza, Ananas'


###############
# - Listor
###############

## Lite användbara metoder för listor:

## Uppdatera ett element i en lista 
lista = ["George", "Orwell", 1984]
lista[2] = 1985
print(lista) # lista = ['George', 'Orwell', 1985]

## append
# Lägg till ett element i en lista
lista = ["Ed", "Edd"]
lista.append("Eddy")
print(lista) # lista = ['Ed', 'Edd', 'Eddy']

## del
# Ta bort ett element på en viss plats ut en lista
lista = ["George", "Orwell", 1984]
del lista[1]
print(lista) # lista = ['George', 1984]

## remove
# Ta bort ett speciellt element ut en lista
lista = ["George", "Orwell", 1984]
lista.remove("George")
print(lista) # lista = ['Orwell', 1984]

## len
# Visa längden på en lista
lista = [0, 1, 2, 3, 4]
l = len(lista) # l = 5

## in
# Finns ett element i en lista?
lista = ["Johan", "Jens", "Johanna", "Jar-Jar"]
exists = "Johanna" in lista # exists = True
exists = "Jerry" in lista # exists = False

## +
# Slå ihop två listor
lista1 = [0, 1, 2]
lista2 = [3, 4, 5]
lista3 = lista1 + lista2 # lista3 = [0, 1, 2, 3, 4, 5]

## *
# Multiplicera en lista
lista = ["La"] * 6 # lista = ['La', 'La', 'La', 'La', 'La', 'La']


################
# - Dictionaries
################

## Lite användbara metoder för dictionaries:

min_dictionary = {'ID': 1110, 'Namn':'Johan', 'Ålder': 12}

## Uppdatera eller lägg till element i en dicitonary:
min_dictionary["ID"] = 1120
min_dictionary["Efternamn"] = "Johansson"
print(min_dictionary) # min_dictionary = {'ID' : 1120, 'Efternamn' : 'Johansson', 'Namn' : 'Johan', 'Ålder' : 12}

## del
# Ta bort ett element ur en lista
del min_dictionary["Namn"]
print(min_dictionary) # min_dictionary = {'ID' : 1120, 'Efternamn' : 'Johansson', 'Ålder' : 12}

## len
# Hämta längden på en dictionary (antal key-value-par)
l = len(min_dictionary) # l = 3

## in
# Kolla om en dictionary har en viss nyckel
a = "ID" in min_dictionary # a = True
b = "Yrke" in min_dictionary # b = False

## keys
# Hämta alla nycklar i en dictionary till en lista
keys = min_dictionary.keys() # keys = ['ID', 'Efternamn', 'Ålder']

## values
# Hämta alla values i en dictionary till en lista
values = min_dictionary.values() # values = ['1120', 'Johansson', '12']
