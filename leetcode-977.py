class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = [i ** 2 for i in nums]
        out.sort()
        return out

if __name__ == '__main__':
    a = Solution()
    nums = [-4,-1,0,3,10]
    s = a.sortedSquares(nums)
    print(s)
