# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541
import sys

def main():
  segments = sys.stdin.readline().split('-')
    
  ans = 0
  for i, segment in enumerate(segments):
      if i == 0:
        ans += sum(list(map(int, segment.split('+'))))
      else:
        ans -= sum(list(map(int, segment.split('+'))))
    
  print(ans)
  
if __name__ == "__main__":
  main()