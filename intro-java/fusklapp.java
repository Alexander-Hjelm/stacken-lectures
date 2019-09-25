package fusklapp;

public class fusklapp {

	public static void main(String[] args) {
		// 1 - Skriv: hello world
		System.out.println("Hello, World!");
		
		// 1.1 - L�gga ihop text
		System.out.println("Hello, " + "World!");

		// 1.1 - Skriv: 123
		System.out.println( 123 );
		
		// 1.2 - L�gga ihop text och nummer
		System.out.println( "Mitt nummer=" + 123 );
		
		// 2 - Variabler
		
		// 2.1 - Heltal (int)
		int ett_tva_tre = 123;
		System.out.println( "ett tv� tre=" + ett_tva_tre );
		
		int num = 19;				// Variabler kan ha vilka namn som helst, bara de inte �r samma som n�gonting som redan finns i Java (int, float, System, etc)
		System.out.println("nummer=" + num);

		// 2.1 - Decimaltal (float, decimal, double)
		float f1 = 5/3;
		float f2 = 5/3f;         // Notera: f-suffix
		System.out.println("f1=" + f1);
		System.out.println("f2=" + f2);

		// double har h�gre precition �n float
		double d1 = 5/3;
		double d2 = 5/3d;		// Notera: d-suffix
		System.out.println("d1=" + d1);
		System.out.println("d2=" + d2);
		
		// 2.2 - Andra nummer typer (g�r inte igenom)
		
		byte minbyte = 0x10;
		short s = 1;
		long l = 13;
		// ...
		
		// 2.3 - Str�ngar (Text)
		String str = "hej! ���";           // String deklareras med stort "S", eftersom det �r ett objekt, och inte en "ren" datatyp

		System.out.println("str=" + str);
		
		// 2.4 - Booleans
		
	}

}
