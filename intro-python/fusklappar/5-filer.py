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
