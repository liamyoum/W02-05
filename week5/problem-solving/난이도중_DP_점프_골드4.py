# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

import sys
input = sys.stdin.readline

def main():
  N, M = map(int, input().split())

  small_rocks = set([int(input()) for _ in range(M)])

  # dp[i][j]: i번째 돌에 j칸 점프해서 도착했을 때 최소 점프 횟수
  dp = [[float("inf")] * 151 for _ in range(N + 1)]
  
  # dp[2][1]: 2번째 돌에 1칸 점프해서 도착했을 때, 점프 횟수는 1회
  if 2 not in small_rocks:
    dp[2][1] = 1
  
  for i in range(3, N + 1): # i: 현재 도착한 돌 번호
    if i in small_rocks:
      continue

    # v: 이전 칸에서 점프한 칸 수 (최대 140 정도 까지)
    for j in range(1, 150):
      # i - j: 이전에 있었던 돌 번호
      if i - j < 1:
        break
      # j칸 점프해서 i에 오려면, 이전 돌에서 j-1, j, j+1 중 하나만큼 점프했어야 함
      dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1
  
  answer = min(dp[N])

  print(answer if answer != float('inf') else -1)

if __name__ == "__main__":
  main()