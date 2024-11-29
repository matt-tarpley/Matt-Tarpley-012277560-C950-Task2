#Author: Matthew Tarpley
#Student ID: 012277560
#Project Title: WGUPS Routing Program

#import packages
import os
from Services.DataService import DataService
from Infrastructure.HashTable import HashTable
import csv
from datetime import timedelta
from datetime import datetime
from Models.Package import Package
from Models.Truck import Truck
from Infrastructure.HashTable import HashTable
from Enums.PackageStatus import PackageStatus
from Services.DataService import DataService


TRUCK_SPEED = 18/60 #miles per minute
TODAY = datetime.now()
START = datetime(TODAY.year, TODAY.month, TODAY.day, 8, 0, 0, 0)


services = DataService()
table = HashTable()

file = os.path.join(os.path.dirname(__file__), '..', 'Data', 'packageCSV.csv')
table = services.loadPackageData(file, table)


table.printContents()

distanceFile = os.path.join(os.path.dirname(__file__), '..', 'Data', 'distanceCSV.csv')
distanceData = services.loadDistanceData(distanceFile)

print(distanceData)

addressFile = os.path.join(os.path.dirname(__file__), '..', 'Data', 'addressCSV.csv')
addressData = services.loadAddressData(addressFile)

print(f'{addressData}\n')