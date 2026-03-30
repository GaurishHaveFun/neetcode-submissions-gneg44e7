class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_count = {}
        l = 0
        res = 0

        for r in range(len(s)):
            freq_count[s[r]] = freq_count.get(s[r], 0) + 1

            #window size
            window_size = r - l + 1
            max_freq = max(freq_count.values())

            if window_size - max_freq > k:
                freq_count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
        