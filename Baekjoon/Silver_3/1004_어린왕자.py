t = int(input())

for _ in range(t):
  count = 0
  x1, y1, x2, y2 = map(int, input().split())
  n = int(input())
  for _ in range(n):
    cx, cy, cr = map(int, input().split())
    distance_1 = (x1-cx)**2 + (y1-cy)**2
    distance_2 = (x2-cx)**2 + (y2-cy)**2
    # 진입/이탈을 위해선 원 안에 1개, 원 밖에 1개 점이 있어야 함
    if (distance_1 < cr**2 and distance_2 > cr**2) or (distance_1 > cr**2 and distance_2 < cr**2):
      count += 1
  print(count)