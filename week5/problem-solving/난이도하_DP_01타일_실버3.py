# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904
import sys

def main():
  N = int(sys.stdin.readline())

  if N == 1 or N == 0:
    print(1)

  dp = [1] * (10 ** 6 + 1)

  for i in range(2, 10 ** 6 + 1):
    dp[i] = dp[i-1] + dp[i-2]

  print(dp[N])

if __name__ == "__main__":
  main()