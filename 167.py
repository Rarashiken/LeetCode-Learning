class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(numbers) -1
        sum = 0
        while left != right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left+1 , right+1]
if __name__ == '__main__':
    A = Solution()
    nums = [2,7,11,15]
    s = A.twoSum(nums,9)
    print(s)
