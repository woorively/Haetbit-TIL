package com.ssafy.mvc.controller;

import java.util.HashSet;
import java.util.Random;
import java.util.Set;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.ssafy.mvc.dto.Lotto;


@Controller
public class MainController {
	@GetMapping("/")
	public String index() {
		return "index";
	}
	
	@GetMapping("login")
	public String loginForm() {
		return "login";
	}
	
	// 로또 조회 폼으로 이동
	@GetMapping("lotto")
	public String lottoForm() {
		return "lotto";
	}
	
	// 로또 숫자 입력
	@PostMapping("lotto")
	public String input(@ModelAttribute Lotto lotto, Model model) {
		int[] targetLotto = generateLotto();
		
		int cnt = 0; // 개수 초기화
		for (int num : targetLotto) {
            if (num == lotto.getNum1()) cnt++;
            if (num == lotto.getNum2()) cnt++;
            if (num == lotto.getNum3()) cnt++;
            if (num == lotto.getNum4()) cnt++;
            if (num == lotto.getNum5()) cnt++;
            if (num == lotto.getNum6()) cnt++;
        }
		
		model.addAttribute("count", cnt);
	    model.addAttribute("targetLotto", targetLotto);
	    model.addAttribute("inputLotto", lotto);
	    
		return "result";
	}
	
	public int[] generateLotto() {
		int[] targetLotto = new int[6];
		Set<Integer> lottoNumbers = new HashSet<>(); // 중복을 피하기 위해 Set 사용
        Random random = new Random();

        while (lottoNumbers.size() < 6) {
            int number = random.nextInt(45) + 1; // 1부터 45까지의 랜덤 숫자 생성
            lottoNumbers.add(number); // Set에 추가 (중복 제거)
        }

        // Set의 숫자를 배열에 담기
        int index = 0;
        for (int number : lottoNumbers) {
            targetLotto[index++] = number;
        }
        
        return targetLotto;
	}	
	
}
