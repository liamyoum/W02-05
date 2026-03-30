# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    meetings = [tuple(map(int, input().split())) for _ in range(N)]
    meetings.sort(key=lambda x: (x[1], x[0]))
    
    available = [meetings[0]]
    end = meetings[0][1]
    for i in range(1, N):
        start = meetings[i][0]
        if start >= end:
            available.append(meetings[i])
            end = meetings[i][1]
    
    print(len(available))

if __name__ == "__main__":
    main()