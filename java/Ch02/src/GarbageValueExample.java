
public class GarbageValueExample {

	public static void main(String[] args) {
		byte v1 = 125;
		int v2 = 125;
		
		for(int i=0; i<5; i++) {
			v1++;
			v2++;
			System.out.println("v1: " + v1 + "\t" + "v2: " + v2);
		}

	}

}
