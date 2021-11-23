import bisect


class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search(nums, target, look_for_right_most):
            left , right = 0 , len(nums)-1
            target_indx = -1
            while(left<=right):
                mid = left + (right - left) // 2
                if nums[mid]<target:
                    left = mid + 1
                elif nums[mid]>target:
                    right = mid - 1
                else:
                    target_indx = mid

                    if look_for_right_most:
                        left = mid +1
                    else:
                        right = mid -1
            return target_indx
        left = binary_search(nums,target,False)
        right = binary_search(nums, target, True)
        return [left,right]




if __name__ == '__main__':
    a = Solution()
    nums = [5,7,7,8,8,10]
    print(nums[-1])
    Search = a.searchRange(nums,5)
    print(Search)