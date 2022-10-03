# Problem Statement:

# Taro's summer vacation starts tomorrow, and he has decided to make plans for it now.
# The vacation consists of N days. For each i (1≤i≤N), Taro will choose one of the following activities and do it on the i-th day:
# A: Swim in the sea. Gain ai points of happiness.
# B: Catch bugs in the mountains. Gain bi points of happiness.
# C: Do homework at home. Gain ci points of happiness.
# As Taro gets bored easily, he cannot do the same activities for two or more consecutive days.
# Find the maximum possible total points of happiness that Taro gains.

n = int(input())
mat = [list(map(int, input().split())) for j in range(n)]
dp = [[0 for i in range(3)] for j in range(n)]
dp[0][0] = mat[0][0]
dp[0][1] = mat[0][1]
dp[0][2] = mat[0][2]
 
for i in range(1, n):
    for j in range(3):
        if j == 0: 
            dp[i][0] = mat[i][0] + max(dp[i-1][1], dp[i-1][2])
        elif j == 1: 
            dp[i][1] = mat[i][1] + max(dp[i-1][0], dp[i-1][2])
        else: 
            dp[i][2] = mat[i][2] + max(dp[i-1][0], dp[i-1][1])
        # print(dp[i][j])
print(max(dp[n-1][0], dp[n-1][1], dp[n-1][2]))
