# 그리디 - 보물 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/1026

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())), reverse=True)
    
    print(sum(x * y for x, y in zip(A, B)))
if __name__ == "__main__":
    main()