nums: list[int] = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end:
    return
  
  pivot: int = start
  left: int = start + 1
  right: int = end
  
  while (left <= right):
    # pivot보다 큰 데이터를 찾을 때까지 반복
    while (left <= end and array[left] <= array[pivot]):
      left += 1
    # pivot보다 작은 데이터를 찾을 때까지 반복
    while (right > start and array[right] >= array[pivot]):
      right -= 1
      
    if (left > right): # 엇갈렸다면 작은 데이터와 pivot을 교체
      array[right], array[pivot] = array[pivot], array[right]
    else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
      array[left], array[right] = array[right], array[left]
      
  # 분할된 두 그룹에 다시 퀵 정렬 수행
  quick_sort(array=array, start=start, end=right-1)
  quick_sort(array=array, start=right+1, end=end)

quick_sort(array=nums, start=0, end=len(nums)-1)
print(nums)