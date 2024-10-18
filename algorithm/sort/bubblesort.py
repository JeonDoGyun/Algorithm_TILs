nums: list[int] = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
cnt: int = len(nums)

for i in range(0, cnt, 1):
  for j in range(0, cnt-i-1, 1):
    if nums[j] > nums[j+1]:
      nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)