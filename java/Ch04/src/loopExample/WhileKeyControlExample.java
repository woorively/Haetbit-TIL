package loopExample;

import java.io.IOException;

public class WhileKeyControlExample {

	public static void main(String[] args) {
		boolean run = true;
		int speed = 0;
		int keyCode = 0;
		
		while(run) {
			if(keyCode != 13 && keyCode != 10) {  // 캐리지리턴(10), 라인피드(13) 제
				System.out.println("------------------------");
				System.out.println("1. 증속 | 2. 감속 | 3. 중지");
				System.out.println("------------------------");
			}
			
			try {
				keyCode = System.in.read();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			if (keyCode == 49) {   // 1을 읽었을 경우
				speed ++;
				System.out.println("현재 속도=" + speed);
			} else if (keyCode == 50) {   // 2를 읽었을 경우
				speed --;
				System.out.println("현재 속도=" + speed);
			} else if (keyCode == 51) {    // 3을 읽었을 경우
				run = false;
			}
		}
		
		System.out.println("프로그램 종료");

	}

}
