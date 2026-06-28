class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        for i, c in enumerate(citations):
            h = n - i
            if c >= h:
                break
        
        return h
        