package fusklapp;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class fusklapp {

	public static void main(String[] args) {
		// 1 - Skriv: hello world
		System.out.println("Hello, World!");
		
		// 1.1 - Lägga ihop text
		System.out.println("Hello, " + "World!");

		// 1.1 - Skriv: 123
		System.out.println( 123 );
		
		// 1.2 - Lägga ihop text och nummer
		System.out.println( "Mitt nummer=" + 123 );
		
		// 2 - Variabler
		
		// 2.1 - Heltal (int)
		int ett_tva_tre = 123;
		System.out.println( "ett två tre=" + ett_tva_tre );
		
		int num = 19;				// Variabler kan ha vilka namn som helst, bara de inte är samma som någonting som redan finns i Java (int, float, System, etc)
		System.out.println("nummer=" + num);

		// 2.1 - Decimaltal (float, decimal, double)
		float f1 = 5/3;
		float f2 = 5/3f;         // Notera: f-suffix
		System.out.println("f1=" + f1);
		System.out.println("f2=" + f2);

		// double har högre precition än float
		double d1 = 5/3;
		double d2 = 5/3d;		// Notera: d-suffix
		System.out.println("d1=" + d1);
		System.out.println("d2=" + d2);
		
		// 2.2 - Andra nummer typer (gör inte igenom)
		
		byte minbyte = 0x10;
		short s = 1;
		long l = 13;
		// ...

		// 2.3 - Strängar (Text)
		String str = "hej! åäö";           // String deklareras med stort "S", eftersom det är ett objekt, och inte en "ren" datatyp

		System.out.println("str=" + str);

		// 2.4 - Tecken
		char j = 'j';  // Note the single quotes
		System.out.println("j=" + j);
		
		// 2.5 - Booleans
		Boolean sant = true;	// object/reference typ som wrappar en boolean
		boolean falskt = false;	// "Ren" (primitiv) datatyp


		// 2.6 - Listor, (Tuplar)
		int[] values = {1, 2, 3, 4};								// values är en 4-tupel
		double[] coolValues = {1.2, 5.7783, 999999.1, 1/10^2 };
		char[] hej1 = {'h','e','j'};
		String hej2 = "hej";  // Betyder det här att String egentligen är en char[]???? -> Ja det gör det, String är en object/reference typ som wrappar en char[]
		
		// Prata om listors properties:
		// .length
		// 

		// Läsa element
		System.out.println(values[0]);
		System.out.println(values[1]);

		// Sätta element
		char[] namn = {'B','o','b'};
		System.out.println(namn);
		namn[0] = 'T';
		namn[2] = 'm';
		System.out.println(namn);

		int[] maxList = new int[10]; // Den här listan kan enbart ha 10 element i sig
		maxList[20] = 1337;			 // ERROR: Index 20 out of bounds for length 10

		// maxList är en 10-tupel

		// 2.7 - Variabla listor	(Mängder som kan växa och minska i storlek dynamiskt)
		// Måste ha: import java.util.*;
		List<Integer> myList = new ArrayList<Integer>();

		// In Java the type of any variable is either a primitive type or a reference
		// type. Generic type arguments must be reference types. Since primitives do not
		// extend Object they cannot be used as generic type arguments for a
		// parametrized type.
		System.out.println(myList); // []
		myList.add(1);
		System.out.println(myList); // [1]
		myList.add(10);
		myList.add(6);
		System.out.println(myList); // [1, 10]
		myList.remove(2);	// Index 2, räknar från 0
		System.out.println(myList); // [1]
		System.out.println(myList.size()); // 1 - Till skillnad från en arrays .length, så är .size() vilken kapacitet som listan har

		// 2.8 - Dictionaries
		Map<String, String> dictionary = new HashMap<String, String>();
		System.out.println(dictionary); // {}
		dictionary.put("key", "value");
		System.out.println(dictionary); // {key=value}
		dictionary.put("key2", "value2");
		System.out.println(dictionary); // {key2=value2, key=value}

		// Om man lägger till något som redan finns, läggs det inte till igen
		dictionary.put("key2", "value2");
		System.out.println(dictionary); // {key2=value2, key=value}

		System.out.println(dictionary.get("key2"));
		dictionary.replace("key2", "lalalalallala"); // Byter ut det som finns i key2 mot lalllalalal om det finns ett värde sedan innan.
		System.out.println(dictionary.get("key2"));


		// 3 - Operationer

		// +
		// - 
		// *
		// /
		// %
		
		// Prata om att lägga ihop olika typer, vad händer?

		int x = 10;
		x *= 2;
		x = x / 2;
		// Fler exempel som de här


		// 3.1 - Logiska operationer
		boolean even = 2 % 2 == 0; // Är 2 mod(2) lika med noll ?
		boolean ett1 = (1 == 1) || (1 == 0); // Är ett lika med ett, eller är ett lika med noll?	Ja
		boolean ett2 = (1 == 1) && (1 == 0); // Är ett lika med ett, och är ett lika med noll? Nej
		boolean inteNegativt = x > 0; // Är x större än noll?
		// >=
		// <=
		// Turnary operations: ?
		// Not: !

		// 4 - Conditions
		if (true) {
			System.out.println("Denna kod kommer att köra");
		}
		if (false) {
			System.out.println("Denna kod kommer inte att köra");
		}

		int a = 50;		// Kan vara användar input
		if (a > 80) {
			System.out.println("a är större än 80");
		}
		else if (a > 50) {									// 50 > 50  -> False
			System.out.println("a är större än 50");
		}
		else {
			System.out.println("a är mindre eller lika med 50");
		}

		// Allt som kan evalueras till sant eller falskt, påståenden

		String kompis = "Vilgot";
		if (kompis == "Vilgot") {
			System.out.println("Min kompis heter " + kompis);
		}
		else {
			System.out.println("Någon jag känner heter " + kompis);
		}

		
		// 5 - Loopar

		// 5.1 - while
		while(1 != 2) {	// Farlig loop...
			System.out.println("Ett är fortfarande inte lika med två...");
		}
		
		int i = 0;
		while(i != 2) {
			System.out.println("i är fortfarande inte lika med två...");
			i++;
		}
		System.out.println("i är lika med två!");


		// 5.2 - for
		for (int k = 0; k != 2; k++) {
			System.out.println("k är fortfarande inte lika med två...");
		}
		System.out.println("k är lika med två!");
		

		for (int k = 0; k < 2; k++) {
			System.out.println("k är fortfarande mindre än två...");
		}
		System.out.println("k är större eller lika med två!");

		// För varje element i mängd
		int[] set = {1, 1, 2, 3, 5, 8, 13, 21};
		for (int element : set) {
			System.out.println("element="+element);
		}

		int[] primes = {2, 3, 5, 7, 11, 13, 19, 23};
		for(int v = 0; v < primes.length; v++) {
			int p = primes[v];
			System.out.println(p + " is prime!");
		}

		// Fylla en lista
		List<Integer> evenNumbers = new ArrayList<Integer>();  // Eller: ArrayList<Integer> evenNumbers = new ArrayList<Integer>();
		for(int n = 0; n < 100; n++) {
			if (n % 2 == 0) evenNumbers.add(n);
		}
		System.out.println(evenNumbers);



		// 6 - System IO (Läsa och skriva text till filer)

		// 6.1 - Läs innehåll
		// Måste ha: import java.io.File;
		// 			 import java.io.FileReader;
		// 			 import java.io.BufferedReader;

		File file1 = new File("min_fil.txt");
		FileReader fr1 = new FileReader(file1);
		BufferedReader br = new BufferedReader(fr1);
		String line;
		while ((line = br.readLine()) != null) {
			// process the line
			System.out.println(line);
		}
		br.close();


		// 6.2 - Skriv innehåll
		// Måste ha: import java.io.File;
		// 			 import java.io.FileWriter;
		// 			 import java.io.BufferedWriter;
		// 			 import java.io.IOException;

		File file2 = new File("min_fil.txt");
		FileWriter fr2 = new FileWriter(file2);
		BufferedWriter bw = new BufferedWriter(fr2);
		
		String myTextToWrite = "Hello, World!";
		bw.write(myTextToWrite);
		bw.close();


		// 7 - Läs input från användare
		
		// Som vi har använt nu hitills, är System.out.println();
		// Den funktionen skriver en ny rad till vad som kallas för
		// "standard-output", och är i de flesta fallen den terminalen
		// som programmet körs i.
		// Det finns därefter en System.in, som är "standard-input".
		// Därifrån kan vi läsa användarinput. För att göra detta
		// måste vi ha en Scanner, som läser av standard-input

		// 7.1 - Läs olika datatyper
		// Måste ha: import java.util.Scanner;

		Scanner input = new Scanner(System.in);

		System.out.print("Enter an integer: ");
		int numberInt = input.nextInt();
		float numberFloat = input.nextFloat();
		double numberDouble = input.nextDouble();
		String text = input.next();

		System.out.println("You entered int: " + numberInt);
		System.out.println("You entered String: " + text);

		// 8 - Funktioner
		// Funktioner är ett bra sätt att strukturera sin kod så att man bara behöver skriva en viss programsekvens en gång,
		// och sedan återanvända den.

		// Funktioner, eller metoder (methods på engelska) kan inte definieras i andra metoder.
		// Statiska metoder kan bara kalla på andra statiska metoder. Dock kan alla metoder kalla på statiska.

		// 8.1 - Hej
		Hej();

		// 8.1.1 - Return "Hej"
		System.out.println(SägHej());	// Tips, använd inte å,ä,o

		// 8.2 - Addition
		int c = Addition(2, 3);
		int tio = Addition(5, 6) - 1; // addition evalueras först, sen resultatet -1

		// 8.3 - Power
		int tusen = Power(10, 3);

		// 8.4 - Print Even numbers
		PrintEvenNums(20, 50);

		// 8.5 - FizzBuzz (Classic "Easy" Coding Interview Question)
		// Låt alla hjälpa dig skriva den här funktionen, handuppräckning/fråga alla etc...
		// Skriv först conceptet med FizzBuzz på tavlan:
		// 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, 10, 11, 12, 13, 14, FizzBuzz, ...
		FizzBuzz(100);
	}

	// 8 - Funktioner

	// 8.1 - Hej
	static void Hej() {					// Void: När en funktion inte ska returnera något värder (som senare ska användas)
		System.out.println("Hej!");
	}
	
	// 8.1.1 - SägHej
	static String SägHej() { // String: När en funktion returnerar en bit text (som senare kan användas)
		return "Hej!";	// Det här avslutar funktionen
	}

	// 8.2 - Addition
	static int Addition(int a, int b) {	// Här kan man bara stoppa in variabler som är av typen int.
		return a + b;
	}

	// 8.3 - Power
	static int Power(int base, int pow) {
		int result = base;				// Skapar en "buffer" för resultatet
		for(int i = 1; i < pow; i++) {
			result *= base;
		}
		return result;
	}

	// 8.4 - Print Even numbers
	static void PrintEvenNums(int from, int to) {
		for(int i = from; i <= to; i++) {
			if (i % 2 == 0) System.out.println(i + " is even.");
		}
	}

	// 8.5 - FizzBuzz (Classic "Easy" Coding Interview Question)
	static void FizzBuzz(int max) {
		for(int i = 1; i <= max; i++) {

			String toPrint = "";	// Starta tom
			if (i % 3 == 0) {
				toPrint += "Fizz";
			}
			if (i % 5 == 0) {
				toPrint += "Buzz";
			}
			if (toPrint == "") {
				// Här sker det magi, Java vet hur man skriver nummer som text, därför kan vi
				// "casta" ett nummber till en sträng!
				toPrint += i;
			}

			System.out.println(toPrint);

		}
	}

}

/*
 * Fler tips för att utvecklas i Java: 
 * - Kolla på Java Ramverket Processing 3: https://processing.org/
 * 
 * 
 * 
 */