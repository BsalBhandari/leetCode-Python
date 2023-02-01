import collections


class Solution:
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        c_rn = collections.Counter(ransomNote)
        c_mg = collections.Counter(magazine)

        for k , v in c_rn.items():
            if k not in c_mg or c_mg[k]<v:
                return False
        return True

test1 = Solution
print(test1.canConstruct(ransomNote="aac", magazine="aabcfd"))

'''
ouput : true
'''
