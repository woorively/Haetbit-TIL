<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>결과 페이지</title>
</head>
<body>
    <h2>몇 개를 맞혔는가!</h2>
    <p>겹치는 숫자의 개수: ${count}</p>

    <h3>입력한 로또 번호:</h3>
    <p>
        ${inputLotto.num1} ${inputLotto.num2} ${inputLotto.num3} ${inputLotto.num4} ${inputLotto.num5} ${inputLotto.num6}
    </p>

    <h3>생성된 로또 번호:</h3>
    <p>
        <c:forEach var="num" items="${targetLotto}" varStatus="status">
            <c:out value="${num}"/>
            <c:if test="${status.last}"> </c:if>
            <c:if test="${!status.last}"> </c:if> <!-- Add a space after each number except the last -->
        </c:forEach>
    </p>
</body>
</html>
