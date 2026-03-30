# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

import sys
input = sys.stdin.readline

def main():
  T = int(input()) # 테스트 케이스의 개수

  for _ in range(T):
    N = int(input()) # 동전 종류의 개수

    coins = tuple(map(int, input().split()))

    N = len(coins)
    M = int(input()) # 만들어야 하는 금액

    # 1. DP 배열 초기화 (N+1행, M+1열)
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # 2. 초기값 설정: 어떤 동전들로든 0원을 만드는 방법은 1가지
    for i in range(N + 1):
      dp[i][0] = 1
    
    # 3. DP 테이블 채우기
    for i in range(1, N + 1):
      coin = coins[i - 1] # 현재 고려 중인 동전
      for j in range(1, M + 1):
        # 기본적으로 이전 동전들까지만 사용해서 j원을 만드는 경우를 가져옴
        dp[i][j] = dp[i - 1][j]
        
        # 현재 동전을 사용할 수 있는 금액이라면 (j >= coin)
        # 현재 동전을 하나 쓴 상태의 경우의 수를 더해줌
        if j >= coin:
          dp[i][j] += dp[i][j - coin]
    
    print(dp[N][M])
if __name__ == "__main__":
  main()