WITH FIRST_GEN AS (
    SELECT ID
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
), SECOND_GEN AS (
    SELECT ED.ID
    FROM FIRST_GEN FG INNER JOIN ECOLI_DATA ED ON FG.ID = ED.PARENT_ID
)

SELECT ED.ID
FROM SECOND_GEN SG INNER JOIN ECOLI_DATA ED ON SG.ID = ED.PARENT_ID
ORDER BY ID