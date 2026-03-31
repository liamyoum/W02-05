# DP - 2*n 타일링 (백준 실버 3)
# 문제 링크: https://www.acmicpc.net/problem/11726

import sys

def main():
  n = int(sys.stdin.readline())

  a, b = 1, 1

  for _ in range(2, n + 1):
    a, b = b, (a + b) % 10007
  
  print(b)
  
if __name__ == "__main__":
  main()