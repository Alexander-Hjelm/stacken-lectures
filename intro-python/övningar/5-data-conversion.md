# Konvertera data

## Uppgift

I katalogen files/4/ finns en fil som är hämtad json.org/example, och som troligen ska beskriva en applikation (vilka visuella element som ska finnas och hur de ska fungera). Som du ser har varje item en action och ett id knutet till sig. Låt oss låtsas att ditt team på kontoret har bestämt sig för att ändra i dataformatet så att fältet "action" nu ska heta "event" istället, och du ska migrera all data till det nya formatet. Du kan antingen kavla upp ärmarna och sätta dig i notepad och skriva om alla förekomster av "action" till "event" för hand, men om du har en riktigt stor datamängd kan det vara lönt att skriva ett program som gör det åt dig istället!

Uppgiften är att läsa in filen files/4/app.xml, och på varje rad ersätta ordet "action" till "event", sedan skriva över filen igen med de nya ändringarna. Dvs du ska skriva till samma fil. Om du vill konstruera lösningen som ett program med eller utan funktioner är upp till dig, men du ska kunna köra programmet och efteråt se ändringarna i filen.

## Tips

- Läsdelen av uppgiften kan se ut som i uppgift 4.

- Kolla i fusklappar/5-files.py för att se hur man läser från och skriver till en textfil.

- Det går bra att mellanlagra filens innehåll som en sträng eller en lista av strängar, mellan läs- och skrivstegen.

- Funktionen string.replace() kan användas för att byta ut en viss delsträng mot en annan. Kolla upp på internet hur man använder den!

- Uppgiften är (som du kanske gissat) påhittad, men datamigrering är ett vanligt problem i riktiga världen, och det är vanligt att man använder program för att utföra migreringar.
