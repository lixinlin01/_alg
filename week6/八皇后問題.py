def is_safe(board, row, col):
    # 檢查同一列
    for i in range(row):
        if board[i] == col:
            return False
    # 檢查左上對角線
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False
    # 檢查右上對角線
    for i, j in zip(range(row-1, -1, -1), range(col+1, 8)):
        if board[i] == j:
            return False
    return True

def solve_queens(board, row, results):
    if row == 8:
        results.append(list(board))
        return
    
    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col  # 放置皇后
            solve_queens(board, row + 1, results) # DFS 遞迴
            # 回溯 (Backtrack) 隱含在循環中，嘗試下一個 col

# 初始化並執行
results = []
solve_queens([-1] * 8, 0, results)

# 印出前 12 組解
for idx, res in enumerate(results[:12]):
    # 轉換為 1-indexed 方便閱讀
    print(f"解 {idx+1}: {[c + 1 for c in res]}")
