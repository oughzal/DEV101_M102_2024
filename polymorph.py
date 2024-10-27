# donner la solution de 136. Single Number de LeetCode
# https://leetcode.com/problems/single-number/
# date: 2020-01-18
# auteur: l'etudiant
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
