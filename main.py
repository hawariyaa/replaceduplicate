# remove duplicates form sorted array, the array is sorted in acsending order
# you cant use extra space meaning o(1), meaning you cant create another array
# you are going to have to use the same array and sort that array it self
# for example: [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# so the out-put is going to be how many unique numbers are inside the array
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if array is empty return 0
        if not nums:
           return 0
        L = 1
        for R in range(1, len(nums)): # here we can intialize R =1 like that, R starts from 1
            if nums[R] != nums[R-1]:
                nums[L] = nums[R]
                L += 1
        return L 
array = [0,0,1,1,1,2,2,3,3,3,4,4]
answer = Solution()
first = answer.removeDuplicates(array)
print(first)