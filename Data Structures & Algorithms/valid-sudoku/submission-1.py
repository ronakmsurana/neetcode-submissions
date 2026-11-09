class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        a = set([1,2,3,4,5,6,7,8,9])
        mat = [[int(j) if j!="." else 0 for j in i ] for i in board]
        tmat = [list(row) for row in zip(*mat)]
        
        s9 = [[mat[r*3 + i][c*3 + j] for i in range(3) for j in range(3)] for r in range(3) for c in range(3)]
        x = [len(set(i)-set([0])) == len(i)-i.count(0) for i in [*mat, *tmat, *s9]]
        return all(x)