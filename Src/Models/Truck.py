#Truck.py
#Model class for Truck objects

from Enums.PackageStatus import PackageStatus

class Truck:
    def __init__(self, maxCapacity = 16, avgSpeed = 18, load = None, packages = None, milesDriven = None, address = None, departTime = None):
        self.maxCapacity = maxCapacity
        self.avgSpeed = avgSpeed
        self.load = load
        self.packages = packages
        self.milesDriven = milesDriven
        self.address = address
        self.departTime = departTime

    def __str__(self):
        return (f'max capacity: {self.maxCapacity} avg speed: {self.avgSpeed} load: {self.load} packages: {self.packages} miles driven: {self.milesDriven} address: {self.address} depart time: {self.departTime}')