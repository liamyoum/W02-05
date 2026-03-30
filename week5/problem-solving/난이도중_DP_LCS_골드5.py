# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251

import sys
input = sys.stdin.readline

def main():
  A = input().rstrip()
  B = input().rstrip()

  n, m = len(A), len(B)

  dp = [[0] * (n + 1) for _ in range(m + 1)]

  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if A[j - 1] == B[i - 1]:
        dp[i][j] = dp[i - 1][j - 1] + 1
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
  
  print(dp[m][n])

if __name__ == "__main__":
  main()

