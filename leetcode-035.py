class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left, right = 0, len(nums) - 1
        target_indx = -1
        while (left <= right):
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                target_indx = mid

        if nums[target_indx]<target:
            return target_indx + 1
        else:
            return target_indx
