# 그리디 - 뒤집기 (백준 실버 5)
# 문제 링크: https://www.acmicpc.net/problem/1439

import sys

def main():
  S = sys.stdin.readline().rstrip()

  cnt0 = 0
  cnt1 = 0

  if S[0] == '0':
    cnt0 += 1
  else:
    cnt1 += 1

  for i in range(1, len(S)):
    if S[i] != S[i - 1]:
      if S[i] == '0':
        cnt0 += 1
      else:
        cnt1 += 1
  
  print(min(cnt0, cnt1))
  
if __name__ == "__main__":
  main()