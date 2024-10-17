# SQL 프로그래밍

- **IN()**

```sql
SELECT mem_name, addr
FROM member
WHERE addr IN ('경기', '전남', '경남');
```

- **출력의 개수를 제한 LIMIT
LIMIT 시작, 개수;
LIMIT 3; = LIMIT 0, 3;**

```sql
SELECT mem_name, height
FROM member
ORDER BY 2 DESC
LIMIT 3, 2; -- 3번째부터 2건만 조회
```

- **중복된 결과를 제거 DISTINCT
 + COUNT(DISTINCT)**

```sql
SELECT DISTINCT addr
FROM member;
```

- **HAVING 절
꼭 GROUP BY 절 다음에 와야 함**

```sql
SELECT mem_id, SUM(price * amount)
FROM buy
GROUP BY mem_id
HAVING SUM(price * amount) > 1000
ORDER BY 2 DESC;
```

- **DATEDIFF()**

```sql
SELECT CAR_ID, 
	ROUND(AVG(DATEDIFF(END_DATE, START_DATE) + 1), 1) as AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING AVERAGE_DURATION >= 7
ORDER BY 2 DESC, 1 DESC;
```

- **DATE_FORMAT( , '%Y-%m-%d’)**

```sql
SELECT ANIMAL_ID , NAME , DATE_FORMAT(DATETIME, '%Y-%m-%d') AS DATETIME
FROM ANIMAL_INS
```