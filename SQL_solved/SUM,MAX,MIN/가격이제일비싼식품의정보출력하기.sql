-- 코드를 입력하세요
-- SELECT *
-- FROM FOOD_PRODUCT
-- ORDER BY PRICE DESC
-- LIMIT PRICE

-- MAX를 이용하여 구하기
SELECT *
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT)