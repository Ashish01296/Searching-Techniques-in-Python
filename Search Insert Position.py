class Solution:
    def searchInsert(self, nums, target):
        s = 0
        e = len(nums) - 1

        mid = s + (e - s) // 2

        while s <= e:
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                s = mid + 1
            else:
                e = mid - 1
            mid = s + (e - s) // 2

        return s




nums = [1, 3, 5, 6]
target = 4

solution = Solution()
result = solution.searchInsert(nums, target)

print(result)



#output

#2
