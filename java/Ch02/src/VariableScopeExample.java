
public class VariableScopeExample {

	public static void main(String[] args) {
		int v1 = 15;
		
		if (v1 > 10) {
			int v2 = v1 - 10;
			System.out.println(v2);
		}
		
		// int v3 = v1 + v2 + 5 // 컴파일 에러
		int v3 = v1 + 5;
		System.out.println(v3);
	}

}
