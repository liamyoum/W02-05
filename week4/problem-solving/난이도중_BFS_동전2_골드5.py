# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294

import sys
from collections import deque
input = sys.stdin.readline

def main():
  n, k = map(int, input().split())

  # 동전 종류 리스트 [1, 5, 12]
  coins = [int(input()) for _ in range(n)]
  
  q = deque([(0, 0)])
  visited = [False] * (k + 1)

  visited[0] = True

  while q:
    cur_sum, cnt = q.popleft()

    if cur_sum == k:
      print(cnt)
      break
    
    for coin in coins:
      nxt = cur_sum + coin
      if 0 < nxt <= k and not visited[nxt]:
        visited[nxt] = True
        q.append((nxt, cnt + 1))
  
  print(-1)

if __name__ == "__main__":
  main()