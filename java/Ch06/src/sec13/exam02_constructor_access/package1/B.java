package sec13.exam02_constructor_access.package1;

public class B {
	A a1 = new A(true);
	A a2 = new A();
	
	// 컴파일 에러 - private
    // A a3 = new A("문자열");
}
