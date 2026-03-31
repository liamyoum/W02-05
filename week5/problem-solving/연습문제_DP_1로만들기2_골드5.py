# DP - 1로 만들기 2 (백준 골드 5)
# 문제 링크: https://www.acmicpc.net/problem/12852
import sys

def main():
    N = int(sys.stdin.readline())
    
    dp = [0] * (N + 1)
    pre = [0] * (N + 1)
    
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + 1
        pre[i] = i - 1
        
        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            pre[i] = i // 2
        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            pre[i] = i // 3
    
    path = []
    curr = N
    while curr != 0:
        path.append(curr)
        curr = pre[curr]

    print(dp[N])
    print(*(path))

if __name__ == "__main__":
    main()