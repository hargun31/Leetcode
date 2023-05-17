class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        last_value = len(nums)

        factorial = int(last_value(last_value + 1) / 2)

        sum = 0
        for i in nums:
            sum = sum + i
            missing_number = factorial - sum
        return missing_number

