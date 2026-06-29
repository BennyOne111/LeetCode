class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def lower_bound(nums, target):
            left, right = 0, len(nums)

            while left < right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left

        start = lower_bound(nums, target)
        end = lower_bound(nums, target + 1) - 1

        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        return [start, end]
        
        