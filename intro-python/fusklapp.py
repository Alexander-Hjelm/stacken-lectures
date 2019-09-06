# Skriv ut text till terminalen
print('Hello world!')

###############
## VARIABLER ##
###############

# Python har 6 inbyggda typer:
# Vilken typ har en viss variabel? använd type()
type(1) # <type 'int'>
type(1.05) # <type 'float'>
type("hej") # <type 'str'>

###############
# - Nummer (heltal och decimaltal)
###############
x = 1
y = 9110
x = 3.141


###############
# - Booleans
###############
# Booleans (bools) är sanningsvärden som antingen är sanna eller falska
a = True
b = False

###############
# - Strängar (strings)
###############
text = "hej"
longer_text = "hej, det här är en lite längre text!"
even_longer_text = """
    hej, det här är en ännu lite längre text,
    som är så lång att den sträcker sig över
    flera rader
    """
print(even_longer_text) # Skriv ut den ännu längre texten


###############
# - Listor
###############
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(week_days[0]) # output: "Monday"
print(week_days[3]) # output: "Thursday"
print(week_days[-1]) # output: "Friday". Negativa index vandrar baklänges i listan
# Element i listor kan vara av vilken typ som helst, även blandade
random_list = ['Monday', 1.12, 900, ['listception', 'we need to go deeper']]


###############
# - Tuplar (Tuples)
###############
# Tuplar är ungefär som listor, men elementen är immutable
# Dvs, när en tuple är definerad kan man inte ändra elementen i den
min_tuple_1 = (1,2,"Hello",3.14,"world")
print(min_tuple_1) # output: (1, 2, 'Hello', 3.14, 'world')
print(min_tuple_1[3]) # output: 3.14
min_tuple_2 = (5,"six")
print(min_tuple_1 + min_tuple_2) # output: (1, 2, 'Hello', 3.14, 'world', 5, 'six')

###############
# - Dictionaries
###############
# En dictionary är en mängd av key-value par.
# Som en lista, fast nycklarna behöver inte vara heltal
min_dictionay = {'ID': 1110, 'Namn':'Johan', 'Ålder': 12}
print (min_dictionay['ID']) # output: 1110
print (min_dictionay['Ålder']) # outpput: 'Johan'


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
e = 1.1 + 9.91 # e = 10.01
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



#########################
# - Conditionals, if/else
#########################

## if, elif och else används för att endast köra en del av koden under vissa omständigheter
## if och elif behöver en boolean, eller ett uttryck som kan tolkas som en boolean
if True:
    print("Denna kod kommer att köra")
if False:
    print("Denna kod kommer inte att köra")

a = 5
if a > 4:
    print("Denna kod kommer att köra, eftersom 5 > 4")
if a < 3:
    print("Denna kod kommer att köra, eftersom 5 inte är mindre än 3")

## else efter en if
## om inte if-blocket körs så kommer else-blocket att göra det
namn = "Arne"
if namn == "Arne":
    print("Denna person heter Arne")
else:
    print("Denna person heter något annat än Arne")

## elif (else if) kan används för att bygga upp block av kod där bara ETT block kommer köras
## Här har vi en if-sats, två elif-satser och en else sats. Bara en kommer att köras!
## else-satsen fångar allting som inte går igenom någon av if- eller elif-satserna
fordon = {'Typ' : 'Motorcykel'}

if fordon['Typ'] == "Cykel":
    print("Detta fordon är en cykel. Ring ring!")

elif fordon['Typ'] == "Motorcykel":
    print("Detta fordon är en motorcykel. Vroom vroom!")
    
elif fordon['Typ'] == "Bil":
    print("Detta fordon är en bil. Tut tut!")

else:
    print("Detta fordon är någonting annat. ??? ???!")



########
# Loopar
########

## Loopar (while eller for) används för att repetera en sekvens av instruktioner flera gånger

## WHILE
# While kör tills påståendet inte längre är sant
i = 1
while i <= 10:
    # Skriv ut talen 1 till 10
    print(i)
    i = i+1

# en while True kommer köra för evigt, eller tills användaren avslutar programmet
#while True:
#    print("hej")

## FOR
# For stegar igenom en lista.
# Inuti for-loopen får man tillgång till elementet i listan som loopen står på just nu
tal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in tal:
    # Ett annat sätt att skriva ut talen 1 till 10
    print (x)

# med range kan kan bygga listor av tal mellan en start- och en slutpunkt
for tal in range(0, 9):
    # Skriv ut talen 1 - 10 igen
    print(tal)

# for kan användas för att gå igenom dictionaries
min_dict = {'Förnamn' : 'Darth', 'Efternamn' : 'Vader', 'Hemplanet' : 'Tatooine'}
for key in min_dict.keys():
    print("Nyckeln " + key + " har värdet " + min_dict[key])



##########################
# Läsa och skriva till fil
##########################

## Python kan läsa från och skriva till filer


## SKRIVA
# Öppnar eller skapar en fil och skriver till den, rad för rad
file = open("testfile.txt","w") # Öppna filen, "w" = write-läge
 
# Skriv till filen rad för rad
file.write("Hello World") 
file.write("This is our new text file") 
file.write("and this is another line.") 
file.write("Why? Because we can.") 
 
file.close() # Kom ihåg att stänga filströmmen


## LÄSA
# Öppnar en fil och läser den, rad för rad
file = open("testfile.txt", "r") # "r" = read-läge
for line in file: 
    # line är här en string
    print(line)
file.close()


###########################
# Läs input från användaren
###########################

## input() kan användas för att fråga efter input från användaren i terminalen
# Användaren kan skriva en text (följt av enter), och denna text lagras till en strång
namn = input("Skriv in ditt namn...")
print ("Hej, ditt namn är: " + namn)


############
# Funktioner
############

## Funktioner är ett bra sätt att strukturera sin kod så att man bara behöver skriva en viss programsekvens en gång,
## och sedan återanvända den.

## Exempel på funktioner:

# Addition
def addition(a, b):
    # a och b är är input till funktionen
    # return bestämmer vad funktionen ger tillbaka, i detta fall a+b
    return a + b

# Exempel på anrop av addition():
c = addition(5, 10) # c = 15
d = addition(5, 10.5) # d = 15.5
# Notera att funktionen inte bryr sig om typen på de variablar som skickas in.
# Var alltså försiktig med vilken typ du skickar in
e = addition("En fin ", "sträng") # e = 'En fin sträng'
f = addition([0, 1, 2, 3], [4, 5]) # f = [0, 1, 2, 3, 4, 5]

# Exempel på en funktion som returnerar absolutvärdet av ett tal:
def absolute_value(num):
	if num >= 0:
		return num
	else:
		return -num

# Output: 2
print(absolute_value(2))

# Output: 4
print(absolute_value(-4))
