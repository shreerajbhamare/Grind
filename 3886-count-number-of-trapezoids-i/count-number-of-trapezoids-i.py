class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        dic = defaultdict(int)
        for x, y in points:
            dic[y] += 1
        
        combs = [comb(f, 2) for f in dic.values()]
        total = sum(combs)
        
        ans = sum(c * (total - c) for c in combs)
        return ans // 2 % MOD