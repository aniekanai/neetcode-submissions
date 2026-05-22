class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
        # #edges case:
        # #if the board is filled wiht dots then return false

        # #check row by row
        # #set for each row
        # #for loop
        # # reset the set to null

        # #time complexity = O(1)
        # #space complexiiy = O(1)


        # #check colum by column
        # #set for each row
        # #for loop
        # # reset the set to null
        # #time complexity = O(1)
        # #space complexiiy = O(1)

        # # check subboxes 
        #     #check row by row - boundary
        #     #set for each row
        #     #for loop
        #     # reset the set to null

        #     #check colum by column - boundary
        #     #set for each row
        #     #for loop
        #     # reset the set to null
        #     #time complexity = O(1)
        #     #space complexiiy = O(1)

        # cols = len(board) # 9
        # rows = len(board[0]) # 9

        # #checking for duplciates row by row
        
        # for i in range(rows):
        #     seen_rows = set()
        #     for j in range(cols):
        #         if board[i][j] in set:
        #             return False
        #         seen_rows.add(board[i][j])
        
        # #check for duplciates column by column

        # for j in range(cols):
        #     seen_cols = set()
        #     if board[j][i]
        #     for i in range(rows):
        #         if board[]
                




