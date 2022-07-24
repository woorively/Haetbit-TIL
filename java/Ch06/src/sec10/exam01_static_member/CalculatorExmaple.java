package sec10.exam01_static_member;

public class CalculatorExmaple {

	public static void main(String[] args) {
		double res1 = 10 * 10 * Calculator.pi;
		// Math.pi
		int res2 = Calculator.plus(10, 5);
		int res3 = Calculator.minus(10,  5);
		
		System.out.println(res1);
		System.out.println(res2);
		System.out.println(res3);
	}

}
