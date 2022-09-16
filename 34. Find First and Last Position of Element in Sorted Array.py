#TC: O(logn)
#SC: O(1)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        starting_pos = self.binarysearch(nums,target,True)
        if starting_pos == -1:
            return [-1,-1]
        ending_pos = self.binarysearch(nums,target,False)
        return [starting_pos,ending_pos]
    
    def binarysearch(self,nums,target,startpos):
        l = 0
        h = len(nums)-1
        while l <= h:
            mid = l + (h-l)//2
            if nums[mid] == target:

                if startpos:
                    if mid == l or nums[mid-1] < target: # we found the lower bound
                        return mid
                    else:
                        h = mid-1
                else:
                    if mid == h or nums[mid+1] > target: # we found the upper bound
                        return mid
                    else:
                         l = mid+1

            elif nums[mid] > target:
                h = mid-1
            else:
                l = mid+1

        return -1