def n_queen_max_score(board):
    n = 8
    max_score = [0]
    
    cols = [False] * n
    diag1 = [False] * (2 * n)
    diag2 = [False] * (2 * n)
    
    def backtrack(row, current_sum):
        if row == n:
            max_score[0] = max(max_score[0], current_sum)
            return
        
        for col in range(n):
            if not cols[col] and not diag1[row - col] and not diag2[row + col]:
                # Place queen
                cols[col] = diag1[row - col] = diag2[row + col] = True
                backtrack(row + 1, current_sum + board[row][col])
                # Remove queen (backtrack)
                cols[col] = diag1[row - col] = diag2[row + col] = False
    
    backtrack(0, 0)
    return max_score[0]


# ---- Driver Code ----
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        board = [list(map(int, input().split())) for _ in range(8)]
        print(n_queen_max_score(board))
