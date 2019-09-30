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
