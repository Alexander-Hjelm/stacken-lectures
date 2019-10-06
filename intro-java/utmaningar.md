# Intro till Java: Utmaningar

Efter föreläsningen finns det ett antal utmaningar som ni kan pröva på att lösa med era nyvunna kunskaper inom **Java**! Det finns olika former av uppgifter där det som vi gått igenom under föreläsningen berörs.

Försök att lösa alla utmaningar, genom att börja med det lättaste och sedan arbete din väg uppåt i svårighetsgrad.

## Problem 1: Medelvärde

Beräkna medelvärdet av följande tal genom användandet av en lista *(Array)* i Java. Och sen utföra beräkningar med varje element.

Rent matematiskt kan formeln för medelvärde skrivas på följande sätt:

![img](https://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Clarge%20M%28x%29%3D%5Cfrac%7Bx_1&plus;x_2&plus;x_3&plus;...&plus;x_n%7D%7Bn%7D)

> ### Uppgift
> Skriv ett program som beräknar medelvärdet av alla tal i en lista av typen **int**.

### Önskad Lösning

| Input                                                        | Output     |
| ------------------------------------------------------------ | ---------- |
| 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500, 1000, 1500, 2000, 3000 | 400.0      |
| 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 1345, 1955, 3300 | 455.333... |



## Problem 2: Tolka fil

En metod för att läsa in filer i Java är följande:

```Java
File file1 = new File("min_fil.txt");
FileReader fr1 = new FileReader(file1);
BufferedReader br = new BufferedReader(fr1);
String line;
while ((line = br.readLine()) != null) {
    System.out.println(line);
}
br.close();
```

Detta kommer dock med lite problem om man klistrar in koden direkt. Försök lista ut hur man gör för att fixa dem själv. Googla eller *(ifall du använder Eclipse Java IDE)* håll musen över den problematiska raden för att se mer information om felet.

>  ### Uppgift
>
>  Läs in följande fil [`tolkafil.txt`](/filer/tolkafil.txt) och skriv ut alla rader med meningarna som börjar på `"A"`. Alla rader ska vara på följande format: `INDEX: RAD`.

### Önskad Lösning

| Input        | Output                                                       |
| ------------ | ------------------------------------------------------------ |
| tolkafil.txt | 0: All kittens is white except Molly.<br/>2: Another kitten called Alex likes to play.<br/>5: As always, the kittens are cuddly, but not<br />6: as loving as dogs. |



## Problem 3: Fibonaccis talföljd

![img](http://www.webbmatte.se/bilder/3_1_3_sop.jpg)

Talföljden, i vilken varje tal är summan av de två närmast föregående talen, ser ut så här:
**1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55…**

![img](http://www.webbmatte.se/bilder/3_1_1_sop.jpg)

Notera att talföljden har initialt talen 1 och 1, därefter beräknas alla andra.

Matematiskt ser funktionen för talet, ***n***, ut på följande sätt: ![{\displaystyle F(n)=F(n-1)+F(n-2)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e276f07879eeeec58ad2c214c5712b54889bcc66)

> ### Uppgift
>
> Skriv ett program som skriver ut alla Fibonaccital, **F(*n*)**, där ***n*** är talets index mellan: **0 ≤ *n* ≤ 100**.
>
> Programmet ska ha minst en funktion.

### Önskad Lösning

| Output                                                       |
| ------------------------------------------------------------ |
| 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041, 1548008755920, 2504730781961, 4052739537881, 6557470319842, 10610209857723, 17167680177565, 27777890035288, 44945570212853, 72723460248141, 117669030460994, 190392490709135, 308061521170129, 498454011879264, 806515533049393, 1304969544928657, 2111485077978050, 3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221, 23416728348467685, 37889062373143906, 61305790721611591, 99194853094755497, 160500643816367088, 259695496911122585, 420196140727489673, 679891637638612258, 1100087778366101931, 1779979416004714189, 2880067194370816120, 4660046610375530309, 7540113804746346429, 12200160415121876738, 19740274219868223167, 31940434634990099905, 51680708854858323072, 83621143489848422977, 135301852344706746049, 218922995834555169026, 354224848179261915075, 573147844013817084101, 927372692193078999176 |

### Extra Utmaning

Kan du lösa problemet linjärt: **O(n)**? Läs mer om [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)/[Ordo](https://sv.wikipedia.org/wiki/Ordo).



## Problem 4: Bilar

De programmeringsparadigmer som Java bygger på är: imperativ, deklarativ, funktionell och objektorienterad programmering. 

> ### Uppgift
>
> Använd dig utav objektorienterad design för den här lösningen, och skapa en klass (Car) som beskriver en bil och som har följande egenskaper:
>
> #### Egenskaper
>
> * **Publika**: Wheels, Engine, Color, Position, Direction
>
> * **Privata**: Speed, MaxSpeed
>
> Välj lämpliga datatyper för alla egenskaper.
>
> #### Metoder
>
> * **Publika**: Car (Konstruktor), Start, Drive, Stop
>
> Varje metod ska skriva lämplig information till skärmen.
>
> ---
>
> Instansiera klassen Car två gånger med olika data. Gör en ***for*** loop för att gå bilen att komma upp i högre hastighet, då **Drive** metoden ska öka hastigheten, **Speed**, varje gång den anropas ända tills den når **MaxSpeed**.



### Extra Utmaning

Hur skulle man kunna göra för att spara kod, ifall man vill lägga till en **buss** och **lastbil** också? Kan man göra någon slags huvud klass som definierar vad ett fordon är?
