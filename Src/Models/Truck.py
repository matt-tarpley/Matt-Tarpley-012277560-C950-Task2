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
        packagesArray = []
        for i in packageNums:
            i = int(i)
            package = hashTable.lookup(i)
            package.status = PackageStatus.IN_TRANSIT
            packagesArray.append(package)
            self.packages = packagesArray