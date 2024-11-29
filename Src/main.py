#Author: Matthew Tarpley
#Student ID: 012277560
#Project Title: WGUPS Routing Program

#import packages
import os
from Services.DataService import DataService
from Services.RouteService import RouteService
from Infrastructure.HashTable import HashTable
import csv
from datetime import timedelta
from datetime import datetime
from Models.Package import Package
from Models.Truck import Truck
from Infrastructure.HashTable import HashTable
from Enums.PackageStatus import PackageStatus
from Services.DataService import DataService


TRUCK_SPEED = 18/60 #.3 miles per minute
TODAY = datetime.now()
START = datetime(TODAY.year, TODAY.month, TODAY.day, 8, 0, 0, 0)

#initializing services
dataService = DataService()
routeService = RouteService()
table = HashTable()

#get package, distance, and address data from the csv files
packageFile = os.path.join(os.path.dirname(__file__), '..', 'Data', 'packageCSV.csv')
table = dataService.loadPackageData(packageFile, table)

distanceFile = os.path.join(os.path.dirname(__file__), '..', 'Data', 'distanceCSV.csv')
distanceData = dataService.loadDistanceData(distanceFile)

addressFile = os.path.join(os.path.dirname(__file__), '..', 'Data', 'addressCSV.csv')
addressData = dataService.loadAddressData(addressFile)

#initialize truck A
packageList1 = [1, 13, 5, 14, 15, 16, 19, 20, 29, 30, 31, 37, 40]

truckA = Truck()
truckA.loadPackagesOntoTruck(packageList1, table)

truckA.currentTime = START
truckA.timeLeftHub = START
truckA.currentLocation = addressData[0]

for i in packageList1:
    package = table.lookup(i)
    package.timeLoaded = truckA.timeLeftHub
    package.truck = 'truck A'
    table.update(i, package)

#initialize truck B at 9:30 to acommodate constraints
packageList2 = [2, 3, 4, 7, 8, 18, 6, 25, 32, 34, 28, 36, 38]
START = datetime(TODAY.year, TODAY.month, TODAY.day, 9, 5, 0, 0)

truckB = Truck()
truckB.loadPackagesOntoTruck(packageList2, table)

truckB.currentTime = START
truckB.timeLeftHub = START
truckB.currentLocation = addressData[0]

for i in packageList2:
    package = table.lookup(i)
    package.timeLoaded = truckB.timeLeftHub
    package.truck = 'Truck B'
    table.update(i, package)

#deliver truck A and truck B packages
distanceToHub1, truckATotalDistance, truckAReturnTime = routeService.deliverPackages(truckA, addressData, distanceData, table)
distanceToHub2, truckBTotalDistance, truckBReturnTime = routeService.deliverPackages(truckB, addressData, distanceData, table)

#after truck A and B begin, intialize truck C
if(truckAReturnTime > truckBReturnTime):
    START = truckAReturnTime
    distanceToHub = distanceToHub1
else: 
    START = truckBReturnTime
    distanceToHub = distanceToHub2

packageList3 = [9, 10, 11, 12, 17, 21, 35, 22, 23, 24, 26, 27, 33, 39]

truckC = Truck()
truckC.loadPackagesOntoTruck(packageList3, table)

truckC.currentTime = START
truckC.timeLeftHub = START
truckC.currentLocation = addressData[0]

for i in packageList3:
    package = table.lookup(i)
    package.timeLoaded = truckC.timeLeftHub
    package.truck = 'Truck C'
    table.update(i, package)

#deliver truck C packages
distanceToHub3, truckCTotalDistance, truckCReturnTime = routeService.deliverPackages(truckC, addressData, distanceData, table)


table.printContents()