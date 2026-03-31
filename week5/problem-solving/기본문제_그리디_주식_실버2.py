# 그리디 - 주식 (백준 실버 2)
# 문제 링크: https://www.acmicpc.net/problem/11501

import sys
input = sys.stdin.readline

def main():
  T = int(input())

  for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))

    total = 0
    max_price = 0
    for i in range(N - 1, -1, -1):
      if prices[i] > max_price:
        max_price = prices[i]
      elif prices[i] < max_price:
        total += max_price - prices[i]
    
    print(total)

if __name__ == "__main__":
  main()