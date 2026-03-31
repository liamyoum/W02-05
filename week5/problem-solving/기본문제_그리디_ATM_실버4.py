# 그리디 - ATM (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/11399

import sys
input = sys.stdin.readline

def main():
  N = int(input())

  time = list(map(int, input().split()))
  time.sort() # O(n log n)
  
  waiting_time = 0
  total_time = 0
  for t in time:
    waiting_time += t
    total_time += waiting_time

  print(total_time)
if __name__ == "__main__":
  main()