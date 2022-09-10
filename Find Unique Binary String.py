#TC: 2^n
#SC: 2^n
class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        dec = []
        for i in range(len(nums)):
            dec.append(int(nums[i],2))
        for i in range(pow(2,len(nums))):
            if i not in dec:
                return str(format(i,'b').zfill(len(nums)))