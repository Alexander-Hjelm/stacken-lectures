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
