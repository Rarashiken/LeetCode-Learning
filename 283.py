class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = j = 0 #i表示第i个非0元素位，j为point
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums

if __name__ == '__main__':
    A = Solution()
    nums = [0,1,0,3,12]
    s = A.moveZeroes(nums )
    print(s)
