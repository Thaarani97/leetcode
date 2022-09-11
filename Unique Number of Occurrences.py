#TC: O(n)
#SC: O(n)
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hm = {}
        for i in range(len(arr)):
            if arr[i] in hm:
                hm[arr[i]]+=1
            else:
                hm[arr[i]] = 1
        if len(hm.values()) == len(set(hm.values())):
            return True
        else:
            return False

#TC: O(n)
#SC: O(n)
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counter = []
        for i in set(arr):
            countocc = arr.count(i)
            if countocc not in counter:
                counter.append(countocc)
            else:
                return False
        return True