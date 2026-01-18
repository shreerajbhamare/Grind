class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n, res = len(grid), len(grid[0]), 0
        # prefix sums
        rows = [[0] * (n + 2) for _ in range(m + 2)]
        cols = [[0] * (n + 2) for _ in range(m + 2)]
        d1 = [[0] * (n + 2) for _ in range(m + 2)]
        d2 = [[0] * (n + 2) for _ in range(m + 2)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                rows[i][j] += rows[i][j - 1] + grid[i - 1][j - 1]
                cols[i][j] += cols[i - 1][j] + grid[i - 1][j - 1]
                d1[i][j] += d1[i - 1][j - 1] + grid[i - 1][j - 1]
                d2[i][j] += d2[i - 1][j + 1] + grid[i - 1][j - 1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(min(m - i, n - j), res, -1):
                    curr = d1[i + k][j + k] - d1[i - 1][j - 1]
                    match = curr == d2[i + k][j] - d2[i - 1][j + k + 1]
                    for p in range(k + 1):
                        if not match:
                            break
                        match &= curr == rows[i + p][j + k] - rows[i + p][j - 1]
                        match &= curr == cols[i + k][j + p] - cols[i - 1][j + p]
                    if match:
                        res = k
                        break
        
        return res + 1