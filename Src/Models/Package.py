#Package.py
#Model class for package objects
from Enums.PackageStatus import PackageStatus

class Package:
    def __init__(self, id = None, details = None, truck = None, status = PackageStatus.AT_HUB, timeLoaded = None, timeDelivered = None):
        self.id = id
        self.details = details
        self.truck = truck
        self.status = status
        self.timeLoaded = timeLoaded
        self.timeDelivered = timeDelivered

        return
    #print all package info
    def printDetails(self):
        print('\nid: ',self.id)
        print('details: ', self.details)
        print('truck package was loaded on: ', self.truck)
        print('status: ', self.status.value)
        print('time loaded on truck: ', self.timeLoaded)
        print('time package was delivered: ', self.timeDelivered)

        return
