
nums = [14, 9, 15, 12, 6, 8, 13]
#9,14,15,12,6,8,13
#9, 14, 12, 15, 

class Solution:
    def insertionSort(self, nums):
        
        for i in range(len(nums)-1):
            j = i
            while  j >= 0 and nums[j+1] < nums[j]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
                j-=1
        return nums


print(Solution().insertionSort(nums))