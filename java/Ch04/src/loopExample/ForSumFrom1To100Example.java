package loopExample;

public class ForSumFrom1To100Example {

	public static void main(String[] args) {
		int sum = 0;
		
		int i;
		for(i=0; i<=100; i++) {
			sum += i;
		}

		System.out.println("1~" + i + " 합: " + sum);
	}

}
