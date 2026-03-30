# DP - 1로 만들기 (백준 실버 3)
# 문제 링크: https://www.acmicpc.net/problem/1463
import sys

def main():
    N = int(sys.stdin.readline())
    
    dp = [0] * (N + 1)
    
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + 1
        
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    print(dp[N])

if __name__ == "__main__":
    main()