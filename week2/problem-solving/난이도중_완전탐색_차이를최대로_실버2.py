# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

"""
문제
N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
"""

"""
입력
첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.
"""

"""
출력
첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.
"""

import sys
input = sys.stdin.readline

def main():
  N = int(input()) # 6
  arr = list(map(int, input().split()))

  visited = [False] * N
  path = []
  max_sum = [0]

  def backtrack(depth):
    # base case
    if depth == N:
      current_sum = 0
      for i in range(N - 1):
        current_sum += abs(path[i] - path[i + 1])
      
      if current_sum > max_sum[0]:
        max_sum[0] = current_sum
      return

    for i in range(N):
      if not visited[i]:
        # 상태값 추가
        visited[i] = True
        path.append(arr[i])

        backtrack(depth + 1)

        # 상태값 원복
        visited[i] = False
        path.pop()
  
  backtrack(0)
  print(max_sum[0])

if __name__ == "__main__":
  main()

"""
정렬 패턴 구하려고 ㅈㄹ을 했던 문제
입력 조건이 최대 8까지다. 그러니까 배열의 경우의수는 최대 8! = 40,320가지다. 다 돌려도 된다는 소리
Brute Force -> 완전 탐색. 말 그대로 전부 탐색해본다는 뜻

재귀를 푸는 방법은 재귀적으로 사고하지 말 것
1) 베이스 케이스 찾기
2) 문제를 잘게 쪼개기
3) N = 3 일때로 시도해보고 돌아가면 뒤는 Recursive leap of faith
"""



