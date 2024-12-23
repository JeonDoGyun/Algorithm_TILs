SELECT HISTORY_ID, 
    ROUND(DAILY_FEE * (DATEDIFF(END_DATE, START_DATE) + 1) * (100 - IFNULL(DISCOUNT_RATE, 0)) / 100) AS FEE
FROM (
        SELECT *, CASE
            WHEN DATEDIFF(END_DATE, START_DATE) + 1 < 7 THEN NULL
            WHEN DATEDIFF(END_DATE, START_DATE) + 1 < 30 THEN '7일 이상'
            WHEN DATEDIFF(END_DATE, START_DATE) + 1 < 90 THEN '30일 이상'
            ELSE '90일 이상'
        END AS DURATION_TYPE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
) A INNER JOIN CAR_RENTAL_COMPANY_CAR B ON A.CAR_ID = B.CAR_ID
    LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN C 
    ON B.CAR_TYPE = C.CAR_TYPE AND A.DURATION_TYPE = C.DURATION_TYPE
WHERE B.CAR_TYPE = '트럭'
ORDER BY FEE DESC, HISTORY_ID DESC