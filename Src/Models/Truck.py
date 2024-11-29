#Truck.py
#Model class for Truck objects

from Enums.PackageStatus import PackageStatus

class Truck:
    def __init__(self, packages = None, currentLocation = None, currentTime = None, timeLeftHb = None):
        self.packages = packages
        self.currentLocation = currentLocation
        self.currentTime = currentTime
        self.timeLeftHub = timeLeftHb

        return
    
    def loadPackagesOntoTruck(self, packageNums, hashTable):
        packages = []
        for i in packageNums:
            i = int(i)
            hashTable.lookup(i).status = PackageStatus.IN_TRANSIT
            packages.append(hashTable.lookup(i))
        return packages