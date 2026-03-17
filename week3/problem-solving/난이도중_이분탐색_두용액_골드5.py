# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

"""

"""

import sys
input = sys.stdin.readline
from bisect import bisect_left

def main():
  N = int(input())

  arr = list(map(int, input().split()))
  arr.sort() # nlogn
  min_sum = 10 ** 10
  left = 0
  right = len(arr) - 1
  liq1 = 0
  liq2 = 0

  """
  Sort + Two pointer
  """
  while left < right:
    if min_sum > abs(arr[left] + arr[right]):
      min_sum = abs(arr[left] + arr[right])
      liq1 = arr[left]
      liq2 = arr[right]

    # 두 합이 양수면 right pointer <- 이동
    if arr[left] + arr[right] > 0:
      right -= 1
    # 두 합이 음수면 left pointer -> 이동
    elif arr[left] + arr[right] < 0:
      left += 1
    # 두 합이 0이면 이게 정답!
    elif arr[left] + arr[right] == 0:
      break
  
  print(f"{liq1} {liq2}")
        
if __name__ == "__main__":
  main()

  # """
  # Sort + Binary Search(bisect 이용)
  # """
  # for i in range(N - 1): 
  #   target = -arr[i]
    
  #   pos = bisect_left(arr, target, i+1) # -target이 들어갈 인덱스 위치 반환
    
  #   if i + 1 <= pos < N:
  #     if abs(arr[i] + arr[pos]) < min_sum:
  #       min_sum = abs(arr[i] + arr[pos])
  #       liq1 = arr[i]
  #       liq2 = arr[pos]
    
  #   if i + 1 <= pos - 1 < N:
  #     if abs(arr[i] + arr[pos - 1]) < min_sum:
  #       min_sum = abs(arr[i] + arr[pos - 1])
  #       liq1 = arr[i]
  #       liq2 = arr[pos - 1]