class Solution:   
    def isMagic(self, i, j,g):
        s = "".join(str(g[i + x // 3][j + x % 3]) for x in [0, 1, 2, 5, 8, 7, 6, 3])
        return g[i][j] % 2 == 0 and (s in "43816729" * 2 or s in "43816729"[::-1] * 2)
    def numMagicSquaresInside(self, g):
        return sum(self.isMagic(i, j,g) for i in range(len(g) - 2) for j in range(len(g[0]) - 2) if g[i + 1][j + 1] == 5)