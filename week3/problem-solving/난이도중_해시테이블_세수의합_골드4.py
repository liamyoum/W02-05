# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

import sys

def sys_input():
  return sys.stdin.readline().rstrip()

def main():
  N = int(sys_input())
  U = [int(sys_input()) for _ in range(N)]
  
  sum_x_y = {U[i] + U[j] for i in range(N) for j in range(N)}

  U.sort(reverse=True) # 내림차순 정렬

  for i in range(U):
    for j in range(U):
      if (U[i] - U[j]) in sum_x_y:
        print(U[i])
        return

if __name__ == "__main__":
  main()