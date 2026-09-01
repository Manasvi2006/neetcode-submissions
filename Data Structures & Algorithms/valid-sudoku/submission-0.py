class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #There are 3 ways a sudoku board isn't valid.
        #if there is duplicate in current rows, current cols, or in the current 3x3 square.
        #create a hashset for each way

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) #key is tuple (r//3,c//3) for the square

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        
        return True


        