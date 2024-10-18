nums: list[int] = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(nums)):
  min_index: int = i # 가장 작은 원소의 인덱스
  for j in range(i+1, len(nums)):
    if nums[min_index] > nums[j]:
      min_index = j
  nums[i], nums[min_index] = nums[min_index], nums[i]

print(nums)