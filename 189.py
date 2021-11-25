class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        lens = len(nums)

        left = nums[lens - k:lens]

        right = nums[0: lens - k]

        a = left + right
        return a
        '''



        k = k % len(nums)
        nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums) - k]
        return nums

if __name__ == '__main__':
    A = Solution()
    nums = [1,2,3,4,5,6,7]
    s = A.rotate(nums, 3)
    print(s)
