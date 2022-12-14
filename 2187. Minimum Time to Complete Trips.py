#TC - O(nlogn)
#SC - O(1)
class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        self.l = 1
        self.r = min(time)*totalTrips
        self.time = time
        while  self.l < self.r:
            self.mid = self.l+(self.r-self.l)//2
            trips_Completed = self.tripsCompleted(self.mid,self.time)
            if trips_Completed >= totalTrips:
                self.r = self.mid
            else:
                self.l = self.mid+1
        return self.l
    
    def tripsCompleted(self,mid,time):
        trips_Completed = sum([mid//t for t in time])
        return trips_Completed
            
            
           
            
        