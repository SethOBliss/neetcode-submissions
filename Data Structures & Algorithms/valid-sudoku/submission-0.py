class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #all board[i][j]!=board[k][j]
        #all board[i][j]!=board[i][k]
        d1={}
        d2={}
        d3={}
        d4={}
        d5={}
        d6={}
        d7={}
        d8={}
        d9={}
        r={}
        c={}
        k=[]
        m=0
        for i in range(9):
            for j in range(9): 
                if board[i][j].isnumeric():
                    if board[i][j] in r:
                        return False
                    else: 
                        r[board[i][j]]= i
                if board[j][i].isnumeric():
                    if board[j][i] in c:
                        return False
                    else: 
                        c[board[j][i]]= j
                if (board[i][j].isnumeric()):
                    if 0<=i<3:
                        if 0<=j<3:
                            if (board[i][j] in d1):
                                return False
                            else: 
                                d1[board[i][j]]=[i,j]
                        if 3<=j<6:
                            if (board[i][j] in d2) :
                                return False
                            else: 
                                d2[board[i][j]]=[i,j]
                        if 6<=j<8:
                            if (board[i][j] in d3) :
                                return False
                            else: 
                                d3[board[i][j]]=[i,j]
                if (board[i][j].isnumeric()):
                    if 3<=i<6:
                        if 0<=j<3:
                            if (board[i][j] in d4):
                                return False
                            else: 
                                d4[board[i][j]]=[i,j]
                        if 3<=j<6:
                            if (board[i][j] in d5) :
                                return False
                            else: 
                                d5[board[i][j]]=[i,j]
                        if 6<=j<8:
                            if (board[i][j] in d6) :
                                return False
                            else: 
                                d6[board[i][j]]=[i,j]
                if (board[i][j].isnumeric()):
                    if 6<=i<9:
                        if 0<=j<3:
                            if (board[i][j] in d7):
                                return False
                            else: 
                                d7[board[i][j]]=[i,j]
                        if 3<=j<6:
                            if (board[i][j] in d8) :
                                return False
                            else: 
                                d8[board[i][j]]=[i,j]
                        if 6<=j<8:
                            if (board[i][j] in d9) :
                                return False
                            else: 
                                d9[board[i][j]]=[i,j]
            r={}
            c={}
                        
            

            
            
        return True