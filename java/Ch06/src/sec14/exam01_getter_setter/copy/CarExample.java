package sec14.exam01_getter_setter.copy;

public class CarExample {

	public static void main(String[] args) {
		Car myCar = new Car();
		System.out.println(myCar.getSpeed());
		
		// 올바른 속도 변경
		myCar.setSpeed(60);
		System.out.println(myCar.getSpeed());
		
		if(!myCar.isStop()) {
			myCar.setStop(true);
		}
		
		System.out.println(myCar.getSpeed());
	}

}
