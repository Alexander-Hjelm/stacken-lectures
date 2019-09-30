# Sortera ut S-element

## Uppgift

Bygg en funktion i python som tar en lista av strängar som indata, och returnerar en ny lista av strängar. Den nya listan ska innehålla alla element i input-listan som börjar med 'S', och inget annat.

Den ursprungliga listan ska vara oförändrad.

## Exempel

Indata: ['Stefan', 'Rasmus', 'Stellan', 'Sven', 'Fabian']

Utdata: ['Stefan', 'Stellan', 'Sven']

## Tips

- En for-loop kan rimligen användas för att vandra genom indata-listan

- En if check kan användas för att verifiera att första bokstaven i ett ord matchar en viss bokstav.

- Funktionen append() kan användas för att lägga till ett element i en lista

- funktionerna upper() och lower() på string-typen kan användas för att konvertera en sträng till uppercase eller lowercase, om du vill säkra att funktionen fungerar för både stora och små bokstäver. Exempel på användning: "test".upper() ger "TEST"
