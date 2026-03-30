# DP - 1, 2, 3 더하기 (백준 실버 3)
# 문제 링크: https://www.acmicpc.net/problem/9095
import sys
input = sys.stdin.readline

def main():
  T = int(input())

  for _ in range(T):
    n = int(input())
    
    if n < 2:
        print(1)
        continue
    
    if n == 2:
        print(2)
        continue

    dp = [1] * (n + 1)
    dp[2] = 2
    dp[3] = 4 

    for i in range(4, n + 1):
      dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp[n])

if __name__ == "__main__":
  main()