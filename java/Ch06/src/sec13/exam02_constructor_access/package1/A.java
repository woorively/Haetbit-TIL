package sec13.exam02_constructor_access.package1;

public class A {
	// 필드
	A a1 = new A(true);
	A a2 = new A();
	A a3 = new A("문자열");
	
	public A(boolean b) {}
	A(){} // default
	private A(String s) {}
}
