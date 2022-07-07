package quiz;

public class Exercise08 {

	public static void main(String[] args) {
		double x = 5.0;
		double y = 0.0;
		
		double z = x % y;
		
		if (Double.isNaN(z)) {
			System.out.printf("%.1f으로 나눌 수 없습니다.\n", y);
		} else {
			double res = z + 10;
			System.out.println("결과: " + res);
		}
	}

}
