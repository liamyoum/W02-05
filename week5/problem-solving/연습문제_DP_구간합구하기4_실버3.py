# DP - 구간 합 구하기 4 (백준 실버 3)
# 문제 링크: https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline

def main():
  N, M = map(int, input().split())

  nums = list(map(int, input().split()))

  dp = [0] * (N + 1)

  for n in range(1, N + 1):
    dp[n] = nums[n - 1] + dp[n - 1]
  
  for _ in range(M):
    i, j = map(int, input().split())

    print(dp[j] - dp[i - 1])

if __name__ == "__main__":
  main()  