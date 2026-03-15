def binary_search_recursion(arr, target, start, end):
  # 못 찾았을 때  
  if start > end:
    return None
  
  mid = (start + end) // 2
  
  # 찾은 경우
  if arr[mid] == target:
    return mid
  
  elif arr[mid] < target:
    return binary_search_recursion(arr, target, mid + 1, end)
  
  elif arr[mid] > target:
    return binary_search_recursion(arr, target, start, mid - 1)
  
