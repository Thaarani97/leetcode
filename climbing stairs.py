#TC - O(2^n)
#SC - O(n)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.num = n
        self.count=0
        print(self.recur(0,n),self.count)
    
    def recur(self,i,n):
        self.count+=1
        if i == self.num:
            return 1
        if n < 0:
            return 0
       
        return self.recur(i+1,n-1) + self.recur(i+2,n-2)        
obj = Solution()   
obj.climbStairs(30)

#TC - O(n)
#SC - O(n)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.num = n
        self.memo = {}
        #self.count = 0
        print(self.recur(0,n,self.memo),self.count)

    def recur(self,i,n,memo):
        #self.count+=1
        #print(memo)
        if i in self.memo :
            return self.memo[i]
        elif i == self.num:
            return 1
        elif n < 0:
            return 0
        
        self.memo[i] = self.recur(i+1,n-1,self.memo) + self.recur(i+2,n-2,self.memo)
        return self.memo[i]
        
obj = Solution()
obj.climbStairs(30)