public class Bil {
	public int Hjul;
	public String Motor;
	public String Farg;
	public int[] Position;
	public double Direction;
	public double Speed;
	
	private double _maxSpeed;
	
	public Bil(int hjul, String motor, String farg, int x, int y, double direction) {
		this.Hjul = hjul;
		this.Motor = motor;
		this.Farg = farg;
		this.Position = new int[2];
		this.Position[0] = x;
		this.Position[1] = y;
		this.Direction = direction;
		
		this.Speed = 0;
		this._maxSpeed = 120;
	}
	
	public Boolean Start() {
		System.out.println("Den " + Farg.toLowerCase() + "a bilen med " + Hjul + " hjul startade sin " + Motor + " motor.");
		return true;
	}
	
	public void Drive() {
		System.out.println("Bilen kör (" + (int)Speed + " km/h)");

		if (Speed < _maxSpeed) Speed += 5;
		
		Position[0] += Math.cos(Direction) * Speed;
		Position[1] += Math.sin(Direction) * Speed;
	}
	
	public void Stop() {
		while((int)Speed > 0) {
			Speed /= 1.33333;
			System.out.println("Bilen saktar ner (" + (int)Speed + " km/h)");
		}
		
		System.out.println("Bilen stannade.");
		Speed = 0;
	}
	
	
}
