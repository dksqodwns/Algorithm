class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == word[0] and self.dfs(board, i, j, word):
                    return True
        return False
    
    def dfs(self, board, i, j, word):                
        row_size = len(board)
        col_size = len(board[0])

        if len(word) == 0:  # 다 찾은 경우
            return True
        
        if i < 0 or i >= row_size or j < 0 or j >= col_size or board[i][j] != word[0]:
            return False
        
        temp = board[i][j]
        board[i][j] = "0"  # 이미 지나간 곳은 0으로 바꿔줌
        
        # 왼쪽, 오른쪽, 위쪽, 아래쪽 확인
        res = (self.dfs(board, i-1, j, word[1:]) or 
               self.dfs(board, i+1, j, word[1:]) or 
               self.dfs(board, i, j-1, word[1:]) or 
               self.dfs(board, i, j+1, word[1:]))
        
        board[i][j] = temp  # 다시 원상복귀
        return res
