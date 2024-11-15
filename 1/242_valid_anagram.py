# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)    : [Video_Link](https://youtu.be/elYr_BtGtW0?si=LsDqfGmnIlAO0QDv)

# using sort method
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
"""

# using Counters
"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
"""


# using dictionary / hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm_s = {}
        hm_t = {}
        for i in s:
            if i in hm_s.keys():
                hm_s[i] += 1
            else:
                hm_s[i] = 1
        for i in t:
            if i in hm_t.keys():
                hm_t[i] += 1
            else:
                hm_t[i] = 1
        if hm_s.keys() != hm_t.keys():
            return False
        for i in hm_s.keys():
            if hm_s[i] != hm_t[i]:
                return False
        return True
