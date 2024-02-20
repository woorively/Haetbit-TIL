package sec08.exam04_overloading;

public class CalculatorExample {

	public static void main(String[] args) {
		Calculator myCalc = new Calculator();
		
		double res1 = myCalc.areaRectangle(10);
		System.out.println(res1);
		
		double res2 = myCalc.areaRectangle(10, 20);
		System.out.println(res2);

	}

}
