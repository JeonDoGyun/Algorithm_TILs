WITH RECURSIVE CTE AS (
    SELECT ID, PARENT_ID, 1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    
    UNION ALL
    
    SELECT E.ID, E.PARENT_ID, 1+CTE.GENERATION AS GENERATION
    FROM ECOLI_DATA E INNER JOIN CTE ON E.PARENT_ID = CTE.ID
)

SELECT COUNT(ID) AS COUNT, GENERATION
FROM CTE
WHERE ID NOT IN (
    SELECT DISTINCT PARENT_ID
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NOT NULL
)
GROUP BY GENERATION
ORDER BY GENERATION