# DP - 계단 오르기 (백준 실버 3)
# 문제 링크: https://www.acmicpc.net/problem/2579
import sys
input = sys.stdin.readline

def main():
  N = int(input())

  stairs = [int(input()) for _ in range(N)]

  if N == 0:
    print(0)
    return
  
  if N == 1:
    print(stairs[0])
    return
  
  dp = [0] * (N + 1)

  dp[0] = 0
  dp[1] = stairs[0]
  dp[2] = dp[1] + stairs[1]

  for i in range(3, N + 1):
    dp[i] = max(dp[i - 2], dp[i - 3] + stairs[i - 2]) + stairs[i - 1]
  
  print(dp[N])

if __name__ == "__main__":
  main()