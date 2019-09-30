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
