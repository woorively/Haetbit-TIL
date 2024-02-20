package sec08.exam01_method_declaration;

public class CalculatorExample {

	public static void main(String[] args) {
		Calculator myCalc = new Calculator();
		myCalc.powerOn();
		
		int res1 = myCalc.plus(5, 6);
		System.out.println(res1);
		
		byte x = 10;
		byte y = 4;
		double res2 = myCalc.divide(x, y);
		System.out.println(res2);
		
		myCalc.powerOff();

	}

}
