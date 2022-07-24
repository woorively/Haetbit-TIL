package sec11.exam01_final;

public class PersonExample {

	public static void main(String[] args) {
		Person p1 = new Person("123456-1234567", "계백");
		
		System.out.println(p1.nation);
		System.out.println(p1.ssn);
		System.out.println(p1.name);
		
		// final 필드는 수정 불가
		p1.name = "을지문덕";
	}

}
