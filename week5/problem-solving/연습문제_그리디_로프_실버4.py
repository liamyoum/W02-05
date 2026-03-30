# DP - 로프 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/2217
import sys
input = sys.stdin.readline

def main():
  N = int(input())

  ropes = [int(input()) for _ in range(N)]
  ropes.sort(reverse = True)

  max_w = 0
  for i in range(len(ropes)):
    w = ropes[i] * (i + 1)
    if max_w < w:
      max_w = w
  
  print(max_w)

if __name__ == "__main__":
  main()