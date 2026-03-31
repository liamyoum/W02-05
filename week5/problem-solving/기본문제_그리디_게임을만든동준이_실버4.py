# 그리디 - 게임을 만든 동준이 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/2847

import sys
input = sys.stdin.readline

def main():
  N = int(input())
  scores = [int(input()) for _ in range(N)]

  cnt = 0
  for i in range(N - 1, 0, -1):
    if scores[i] <= scores[i - 1]:
      target = scores[i] - 1
      diff = scores[i - 1] - target
      cnt += diff
      scores[i - 1] = target

  print(cnt)  

if __name__ == "__main__":
  main()