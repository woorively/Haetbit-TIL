package sec06.exam01_field_declaration;

public class CarExample {

	public static void main(String[] args) {
		Car myCar = new Car();
		
		System.out.println(myCar.company);
		System.out.println(myCar.model);
		System.out.println(myCar.color);
		System.out.println(myCar.maxSpeed);
		
		// 기본 초기화 값인 0
		System.out.println(myCar.speed);
		
		myCar.speed = 60;
		System.out.println(myCar.speed);
	}

}
