#Package.py
#Model class for package objects
from Enums.PackageStatus import PackageStatus

class Package:
    def __init__(self, id, address, city, state, zip, deadlineTime, weight, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadlineTime = deadlineTime
        self.weight = weight
        self.status = status
        self.departTime = None
        self.timeDelivered = None

        return

    #updates status based on time delta(difference in time)
    def updateStatus(self, convert_timedelta):
        if self.timeDelivered < convert_timedelta:
            self.status = PackageStatus.DELIVERED
        elif self.departTime > convert_timedelta:
            self.status = PackageStatus.IN_TRANSIT
        else:
            self.status = PackageStatus.AT_HUB

    def __str__(self):
        #simple formatting for displaying package info
        return(f"ID:{self.id} address: {self.address} {self.city},{self.state} {self.zip} deadline:{self.deadlineTime} departed at: {self.departTime} delivered at:{self.timeDelivered}\n\n")
