
public class FromIntToFloat {

	public static void main(String[] args) {
		int num1 = 123456780;
		int num2 = 123456780;
		
		float num3 = num2;
		num2 = (int)num3;
		
		int res = num1 - num2;
		System.out.println(res);

		/*
		예상된 값은 0인데 결과값은 -4가 나옴
		*/
	}

}
