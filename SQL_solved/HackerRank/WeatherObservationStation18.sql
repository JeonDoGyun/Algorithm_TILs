-- a : LAT_N의 MIN
-- b : LONG_W의 MIN
-- c : LAT_N의 MAX
-- d : LONG_W의 MAX
-- 맨하탄 거리 : x1-x2 절댓값 + y1-y2 절댓값
SELECT ROUND(ABS(MIN(LAT_N)-MAX(LAT_N))+ABS(MIN(LONG_W)-MAX(LONG_W)), 4) AS Manhattan_distance
FROM STATION