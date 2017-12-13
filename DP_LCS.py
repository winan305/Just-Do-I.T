# https://www.acmicpc.net/problem/9251

import sys

def LCS(str1, str2) :
    len1 = len(str1)
    len2 = len(str2)

    DP = [[0 for col in range(0, len2+1)] for row in range(0, len1+1)]

    for i in range(1, len1+1) :
        for j in range(1, len2+1) :
            if(str1[i-1] == str2[j-1]) :
                DP[i][j] = DP[i-1][j-1] + 1

            else :
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])

    return DP[-1][-1]

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

print(LCS(str1, str2))