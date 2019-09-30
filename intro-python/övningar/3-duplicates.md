# Ta bort duplikat

## Uppgift

Bygg en funktion i python som tar en lista som indata, och returnerar SAMMA lista, men duplikat av element ska tas bort. Dvs varje element får bara förekomma en gång.

## Exempel

Indata: [1, 1, 'hej', 'soffa', 'hej', 3.1416]

Utdata: [1, 'hej', 'soffa', 3.1416]

## Tips

- Strukturen för programmet kan se ut ungefär som i uppgift 1.

- Tänk på att in eller contains() kommer returnera true ifall elementet är hämtat direkt ur listan. Dessa funktioner kan alltså inte användas direkt för att hitta duplikat.

- En inre while-loop skulle kunna användas för att identifiera två likadana element på olika index i listan...

- ... eller så kan man kopiera element till en ny lista och använda contains() på den nya listan för att se om elementet redan lagts till.

- Kort sagt, det finns många sätt att lösa denna uppgift på, precis som med de flesta problem i riktiga världen.
