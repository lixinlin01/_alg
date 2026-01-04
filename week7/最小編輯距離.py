def min_edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    # 建立 (m+1) x (n+1) 的 DP 表格
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化 Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # 填表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # 刪除 (Delete)
                    dp[i][j-1],    # 插入 (Insert)
                    dp[i-1][j-1]   # 替換 (Replace)
                )
    
    return dp[m][n]

# 測試
print('第一句：kitten\n第二句：sitting\n結果：',min_edit_distance("kitten", "sitting")) 
print('\n第一句：\n第二句：sitting\n結果：',min_edit_distance("", "sitting")) 
print('\n第一句：ki\n第二句：sit\n結果：',min_edit_distance("ki", "sit")) 