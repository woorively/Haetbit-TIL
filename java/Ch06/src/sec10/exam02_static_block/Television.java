package sec10.exam02_static_block;

public class Television {
	static String company = "Samsung";
	static String model = "LCD";
	static String info;
	static int from1To10Sum;
	
	static {
		info = company + "-" + model;
		
		// 복잡한 초기화 작업  
		int sum = 0;
		for(int i=0; i<=10; i++) {
			sum += i;
		}
		from1To10Sum = sum;
	}
}
