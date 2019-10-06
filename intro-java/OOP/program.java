public class program {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Bil minBil = new Bil(4, "Honda", "Röd", 50, 1280, Math.PI/3);
		
		minBil.Start();
		for(int i = 0; i < 40; i++) {
			minBil.Drive();
		}
		minBil.Stop();
		

		Bil minTrehjuling = new Bil(3, "Mänskliga", "Grön", 0, 0, 1.2);
		minTrehjuling.Start();
		minTrehjuling.Drive();
		minTrehjuling.Drive();
		minTrehjuling.Stop();
	}

}