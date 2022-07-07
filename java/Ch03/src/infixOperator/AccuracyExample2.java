package infixOperator;

public class AccuracyExample2 {

	public static void main(String[] args) {
		int apple = 1;
		
		int totalPieces = apple * 10;
		int number = 7;
		int temp = totalPieces - number;
		
		double res = temp/10.0;
		
		System.out.println("사과 한 개에서 ");
		System.out.println("0.7 조각을 뺴면, ");
		System.out.println(res + "조각이 남는다.");

	}

}
