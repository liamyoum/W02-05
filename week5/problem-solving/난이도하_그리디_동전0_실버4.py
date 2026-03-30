# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline

def main():
  N, K = map(int, input().split())

  coins = [int(input()) for _ in range(N)]

  min_cnt = 0
  for i in range(N - 1, -1, -1): # 이렇게 하면 정렬 안 하고 가능해서 더 효율적
    coin = coins[i]
    if K < coin: continue

    cnt, K = divmod(K, coin)
    min_cnt += cnt

    if K == 0:
      print(min_cnt)
      break  
    
if __name__ == "__main__":
  main()