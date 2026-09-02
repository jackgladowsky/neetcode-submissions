class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            freqs[tuple(count)].append(s)
        
        return list(freqs.values())
            
        