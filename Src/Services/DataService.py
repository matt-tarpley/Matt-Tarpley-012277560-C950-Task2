#DataService.py contains all of the data/csv interaction code for the application

import csv
from Models.Package import Package
from Enums.PackageStatus import PackageStatus

class DataService:

    #reads package data from a csv file and loads each corresponding object into the hashtable
    def loadPackageData(self, packageFile, hashTable):
        with open(packageFile) as csvFile:
            reader = csv.reader(csvFile, delimiter=',')
            for row in reader:
                package = Package()
                package.id = int(str.strip(row[0]))
                package.truck = None,
                package.details = [str.strip(x) for x in row [1::]]
                package.status = PackageStatus.AT_HUB
                package.timeDelivered = None
                hashTable.insert(package.id, package)

        return hashTable
    
    #reads distance data from a csv file and returns an array of arrays containing distance pairs
    def loadDistanceData(self, distanceFile):
        distances = []
        with open(distanceFile) as csvFile:
            reader = csv.reader(csvFile, delimiter=',')
            for row in reader:
                distanceSet = [float(x) for x in row[0 : :] if x != '']
                distances.append(distanceSet)

        return distances
    
    #reads address data from a csv file and returns an array of address data
    def loadAddressData(self, addressFile):
        addresses = []
        with open(addressFile) as csvFile:
            reader = csv.reader(csvFile, delimiter=',')
            for row in reader:
                addresses.append(str.strip(row[2]))
        return addresses