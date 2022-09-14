#TC: O(n)
#SC: O(n)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split(' ')
        res = []
        for i in range(len(arr)-1,-1,-1):
            if arr[i] != "":
                res.append(arr[i])
        return (" ".join(res).strip())