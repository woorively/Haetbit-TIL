
public class StringEqualsExample {

	public static void main(String[] args) {
		String str1 = "김우리";
		String str2 = "김우리";
		
		if (str1 == str2) {
			System.out.println("str1과 str2는 참조가 같음");
		} else {
			System.out.println("str1과 str2는 참조가 다름");
		}
		
		if (str1.equals(str2)) {
			System.out.println("str1과 str2는 문자열이 같음");
		}
		
		System.out.println();
		
		String str3 = new String("김우리");
		String str4 = new String("김우리");
		
		if (str3 == str4) {
			System.out.println("str3과 str4는 참조가 같음");
		} else {
			System.out.println("str3과 str4는 참조가 다름");
		}
		
		if (str3.equals(str4)) {
			System.out.println("str3과 str4는 문자열이 같음");
		}

	}

}
