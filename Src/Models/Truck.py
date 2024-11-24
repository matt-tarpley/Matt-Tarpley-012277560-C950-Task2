#Truck.py
#Model class for Truck objects

from Enums.PackageStatus import PackageStatus

MAX_CAPACITY = 16
AVG_SPEED = 18

class Truck:
    def __init__(self, packages = None, milesDriven = 0.0, currentLocation = None, currentTime = None, departFromHubTime = None):
        self.maxCapacity = MAX_CAPACITY
        self.avgSpeed = AVG_SPEED
        self.packages = packages
        self.milesDriven = milesDriven
        self.currentLocation = currentLocation
        self.currentTime = currentTime
        self.departFromHubTime = departFromHubTime

    ##load packages onto truck and set status via package status enum
    def loadPackages(self, packageNumbers, hashTable):
        packages = []
        for i in packageNumbers:
            i = int(i)
            package = hashTable.find(i)
            package.status = PackageStatus.IN_TRANSIT
            packages.append(package)

        return packages   