# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

"""
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
"""

"""
입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
"""

"""
출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
"""

import sys
from bisect import bisect_left, bisect_right # binary search library
input = sys.stdin.readline

def main():
  N = int(input()) # 5
  A = list(map(int, input().split()))
  M = int(input()) # 5
  nums = list(map(int, input().split()))

  """
  # 1. Binary Search 직접 구현
  """
  # # Binary Search 하고 싶으면 array 무조건 sorted
  # A.sort() # 내부 정렬 NlogN

  # def binary_search(arr, target):
  #   left = 0 # 맨 왼쪽 인덱스
  #   right = len(arr) - 1 # 맨 오른쪽 인덱스
    
  #   while left <= right: # left와 right 교차 전까지
  #     mid = (left + right) // 2 # 가운데 인덱스, 매번 업데이트
  #     if target == arr[mid]:
  #       return 1 # 찾았음! 여기서는 그냥 1만 출력
  #     elif target > arr[mid]:
  #       left = mid + 1
  #     elif target < arr[mid]:
  #       right = mid - 1

  #   return 0 # 못 찾았을 때
  
  # for num in nums: # O(M)
  #   print(binary_search(A, num)) # O(logM)

  """
  # 2. bisect library 사용
  bisect_left(arr, x): 정렬된 arr에서 x를 넣을 수 있는 가장 왼쪽 위치 반환
  bisect_right(arr, x): 정렬된 arr에서 x를 넣을 수 있는 가장 오른쪽 위치 반환
  """
  A.sort()
  for num in nums:
    idx = bisect_left(A, num)

    # 첫 번째 조건: 배열 범위를 안 벗어났는지 -> 찾고자 하는 값이 모든 원소보다 크면 삽입 위치가 맨 끝, 즉 len(arr)이 됨
    # 두 번째 조건: 그 자리에 실제로 x가 있는지 확인.
    # 두 번째 조건만 있어도 되는거 아닌가 싶지만, 첫 번째 조건 없으면 배열 인덱스 에러남
    # 첫 번째 조건만 있는 것도 안됨. 둘 다 반례 한 번 생각해보기!
    if idx < len(A) and A[idx] == num:
      print(1)
    else:
      print(0)
  """
  # 3. set을 사용, 시간복잡도면에서 더 효율적
  """
  # set 사용하는 풀이, 더 효율적
  # s = set(A)

  # for num in nums:
  #   print(1 if num in s else 0)
if __name__ == "__main__":
  main()