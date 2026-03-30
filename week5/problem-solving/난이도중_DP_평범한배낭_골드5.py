# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

def main():
  # 물건의 수 N, 최대 가방 무게 K
  N, K = map(int, input().split())

  things = [tuple(map(int, input().split())) for _ in range(N)]
  
  dp = [[0] * (K + 1) for _ in range(N + 1)]

  # 테이블 맨 윗줄 초기화
  for i in range(K + 1):
    dp[0][i] = 0
  
  for i in range(1, N + 1):
    W, V = things[i - 1][0], things[i - 1][1]
    for j in range(K + 1):
      dp[i][j] = dp[i - 1][j]
      if j - W >= 0:
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W] + V)
  
  print(dp[N][K])

if __name__ == "__main__":
  main()