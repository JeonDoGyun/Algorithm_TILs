-- 코드를 입력하세요
SELECT ri.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) AS REVIEW_SCORE
FROM REST_INFO ri INNER JOIN REST_REVIEW rr ON ri.REST_ID = rr.REST_ID
WHERE LEFT(ADDRESS, 2) = '서울'
GROUP BY ri.REST_ID
ORDER BY REVIEW_SCORE DESC, FAVORITES DESC