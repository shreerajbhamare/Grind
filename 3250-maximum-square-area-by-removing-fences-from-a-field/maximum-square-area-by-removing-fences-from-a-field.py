class Solution:
    def maximizeSquareArea(
        self, 
        m: int, 
        n: int, 
        hFences: List[int], 
        vFences: List[int]
    ) -> int:
        """
        What the problem asks is the same as finding the maximum interval by 
        removing fences that can be achieved in both hFences and vFences
        """
        hFences.extend([1, m])
        vFences.extend([1, n])
        h_side_lens = {abs(fence1 - fence2) for fence1 in hFences
                       for fence2 in hFences}
        area = 0
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                side_len = abs(vFences[i] - vFences[j])
                if side_len in h_side_lens:
                    area = max(area, side_len**2)
        return -1 if not area else area % (10**9 + 7)