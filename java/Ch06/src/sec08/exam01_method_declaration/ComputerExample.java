package sec08.exam01_method_declaration;

public class ComputerExample {

	public static void main(String[] args) {
		Computer myCom = new Computer();
		
		int[] val1 = {1, 2, 3};
		int res1 = myCom.sum1(val1);
		System.out.println(res1);
		
		int res2 = myCom.sum1(new int [] {1, 2, 3, 4, 5});
		System.out.println(res2);
		
		
		int res3 = myCom.sum2(1, 2, 3);
		System.out.println(res3);
		
		int res4 = myCom.sum2(1, 2, 3, 4, 5);
		System.out.println(res4);

	}

}
