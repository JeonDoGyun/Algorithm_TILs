-- a : LAT_N의 MIN
-- b : LONG_W의 MIN
-- c : LAT_N의 MAX
-- d : LONG_W의 MAX
-- 맨하탄 거리 : x1-x2 절댓값 + y1-y2 절댓값
select ROUND(abs(a-c)+abs(b-d), 4) as Manhattan_distance
from (
    select
        min(LAT_N) as a, 
        min(LONG_W) as b, 
        max(LAT_N) as c, 
        max(LONG_W) as d
    from station
) a