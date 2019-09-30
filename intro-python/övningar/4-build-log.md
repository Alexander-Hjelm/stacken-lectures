# Läs en build-logg

## Uppgift

Skriv en funktion som läser de 2 filerna i katalogen files/4/, och returnerar True eller False beroende på om bygget slutade med status Succeeded eller Failed. Funktionen ska ta filens sökväg (path) som indata.

Bakgrund: filerna har genererats av en kompilator som har byggt ett C-program från källkod, och vi kan vilja använda resultatet för någonting skoj. Till exempel kan vi notifiera en webbserver som visar hur senaste bygget gick på en webbsida. Detta ingår inte i uppgiften dock!

## Tips

- Kolla i fusklappar/5-files.py för att se hur man läser en textfil rad för rad.

- Försök hitta något som identifierar raden som säger om bygget gick bra eller inte. Denna rad är inte alltid på samma plats i filen!

- "in" operatorn kan användas för att kolla om en sträng innehåller en annan delsträng.
