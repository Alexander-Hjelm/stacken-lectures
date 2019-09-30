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
