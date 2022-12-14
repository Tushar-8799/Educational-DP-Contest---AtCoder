# Problem Statement:
# There are N stones, numbered 1,2,…,N. For each i (1≤i≤N), the height of Stone i is hi
# There is a frog who is initially on Stone 1. He will repeat the following action some number of times to reach Stone N:
#   -If the frog is currently on Stone i, jump to Stone i+1 or Stone i+2. Here, a cost of ∣hi−hj∣ is incurred, where j is the stone to land on.
# Find the minimum possible total cost incurred before the frog reaches Stone N.

n  = int(input())
arr = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(1, n):
  second = float('inf')
  first = abs(arr[i]-arr[i-1]) + dp[i-1]
  if i > 1:
    second = abs(arr[i]-arr[i-2]) + dp[i-2]
  dp[i] = min(first, second)
print(dp[n-1])
