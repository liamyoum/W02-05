# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639

import sys
sys.setrecursionlimit(10**6)

def main():
  preorder = list(map(int, sys.stdin.read().split()))

  def postorder(start, end):

    # base case
    if start > end:
      return
    
    # 얘는 재귀 호출되면서 계속 바뀜 (서브트리의 루트로)
    root = preorder[start]

    split = end + 1 # 오른쪽 서브트리 없이 루트보다 값이 다 작으면, split은 end 보다 커야함
    for i in range(start + 1, end + 1):
      if preorder[i] > root:
        split = i
        break # 꼭 멈춰줘라 제발~~~~
    
    postorder(start + 1, split - 1)
    postorder(split, end)
    print(root)

  postorder(0, len(preorder) - 1)
if __name__ == "__main__":
  main()