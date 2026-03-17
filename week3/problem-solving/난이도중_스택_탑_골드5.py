# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

import sys
input = sys.stdin.readline

def main():
  N = int(input()) # 5, 1 <= N <= 500,000
  tops = list(map(int,input().split()))
  stack = [] # index, height
  result = []

  for idx, top in enumerate(tops):
    # 1) 현재 탑보다 낮은 애들 pop
    while stack and stack[-1][1] < top:
      stack.pop()
    
    # 2) 답 기록
    # 스택이 비었으면 -> 수신할 탑 없음 -> 0
    # 스택이 안 비었고 앞에 나보다 큰 놈 있으면 -> 그 탑 인덱스 + 1 기록
    if stack:
      result.append(stack[-1][0])
    else:
      result.append(0)

    # 3) 현재 탑 push
    stack.append((idx + 1, top))

  print(" ".join(list(map(str, result))))

if __name__ == "__main__":
  main()