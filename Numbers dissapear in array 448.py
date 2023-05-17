class Solution(object):
    def findDisappearedNumbers(self, nums):
        new_set = set(nums)

        l = []

        for i in range(1,len(nums)+1):
            if i in new_set:
                continue
            l.append(i)

        return l
