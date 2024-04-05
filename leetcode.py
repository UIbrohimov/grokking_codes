from typing import List

def check(strs, harf):
    for item in strs:
        if not item.startswith(harf):
            return harf[:-1]
    return harf

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) > 0 and len(strs[0]) > 0:
            common = strs[0][0]
        else:
            return "" 

        for harf in strs[0]:
            result = check(strs, common)
            if result == common:
                common += harf
            else:
                break
        return result

