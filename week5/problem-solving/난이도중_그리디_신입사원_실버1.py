# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        
        candidates = [tuple(map(int, input().split()))for _ in range(N)]
        candidates.sort(key=lambda x: x[0])
        
        ans = 0
        min_rank2 = float('inf')
        for rank1, rank2 in candidates:
            if rank2 > min_rank2:
                continue
            ans += 1
            min_rank2 = rank2
        
        print(ans)
        
if __name__ == "__main__":
    main()