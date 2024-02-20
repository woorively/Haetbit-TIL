package sec08.exam01_method_declaration;

public class Calculator {
	void powerOn() {
		System.out.println("전원을 켭니다.");
	}
	
	int plus(int x, int y) {
		int res = x + y;
		return res;
	}
	
	double divide(int x, int y){
		double res = (double)x / y;
		return res;
	}
	
	void powerOff() {
		System.out.println("전원을 끕니다.");
	}
	
}
