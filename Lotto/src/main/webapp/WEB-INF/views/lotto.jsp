<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>로또 번호 입력하기</title>
</head>
<body>
	<h2>로또 번호 입력 페이지</h2>
	<p>1~45 숫자 입력</p>
	<form action="lotto" method="POST">
		<p>첫 번째 숫자</p>
		<input type="number" name="num1">
		<p>두 번째 숫자</p>
		<input type="number" name="num2">
		<p>세 번째 숫자</p>
		<input type="number" name="num3">
		<p>네 번째 숫자</p>
		<input type="number" name="num4">
		<p>다섯 번째 숫자</p>
		<input type="number" name="num5">
		<p>여섯 번째 숫자</p>
		<input type="number" name="num6">
		<input type="submit"><br>
	</form>
</body>
</html>