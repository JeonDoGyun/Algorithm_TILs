WITH PARENT_GENOTYPE AS (
    SELECT ID, GENOTYPE
    FROM ECOLI_DATA A
)

SELECT A.ID, A.GENOTYPE, PG.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA A
    INNER JOIN PARENT_GENOTYPE PG
    ON A.PARENT_ID = PG.ID
WHERE (A.GENOTYPE & PG.GENOTYPE) = PG.GENOTYPE
ORDER BY ID