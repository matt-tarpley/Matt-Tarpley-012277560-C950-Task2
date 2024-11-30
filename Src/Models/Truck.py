#Truck.py
#Model class for Truck objects
#citing source:
#c950: Primary Steps Video1of3 by Robert Ferdinand

from Enums.PackageStatus import PackageStatus

class Truck:
    def __init__(self, packages = None, currentLocation = None, currentTime = None, timeLeftHb = None):
        self.packages = packages
        self.currentLocation = currentLocation
        self.currentTime = currentTime
        self.timeLeftHub = timeLeftHb

        return
    
    #loads packages onto truck based on a list of package id's
    def loadPackagesOntoTruck(self, packageNums, hashTable):
        packagesArray = []
        for i in packageNums:
            i = int(i)
            package = hashTable.lookup(i)
            package.status = PackageStatus.IN_TRANSIT
            packagesArray.append(package)
            self.packages = packagesArray