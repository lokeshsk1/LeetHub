class RideSharingSystem:

    def __init__(self):
        self.drivers = deque()
        self.riders = deque()
        self.waiting = set()
        self.cancelled = set()
        
    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        self.waiting.add(riderId)
        
    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:

        while self.riders and self.riders[0] in self.cancelled:
            rider = self.riders.popleft()
            self.cancelled.remove(rider)

        if len(self.drivers)==0 or len(self.riders)==0:
            return [-1,-1]
            
        driver = self.drivers.popleft()
        rider = self.riders.popleft()
        self.waiting.remove(rider)
        return [driver, rider]
        
    def cancelRider(self, riderId: int) -> None:
        if riderId in self.waiting:
            self.cancelled.add(riderId)
            self.waiting.remove(riderId)

        


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)