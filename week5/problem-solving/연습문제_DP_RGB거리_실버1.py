# DP - RGB거리 (백준 실버 1)
# 문제 링크: https://www.acmicpc.net/problem/1149

import sys
input = sys.stdin.readline

def main():
  N = int(input())

  costs = [list(map(int, input().split())) for _ in range(N)]

  dp = [[0] * 3 for _ in range(N + 1)]
  dp[1] = costs[0]

  for i in range(2, N + 1):
    for j in range(3):
      dp[i][j] = costs[i - 1][j] + min(dp[i - 1][:j] + dp[i - 1][j+1:])
    
  print(min(dp[N]))

if __name__ == "__main__":
  main()