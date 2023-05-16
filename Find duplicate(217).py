class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        NewSet = set()
        for i in nums:
             if i in NewSet:
                return True
             NewSet.add(i)
        return False
