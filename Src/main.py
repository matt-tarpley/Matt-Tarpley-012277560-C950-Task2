#Author: Matthew Tarpley
#Student ID: 012277560
#Project Title: WGUPS Routing Program

#import packages
import csv
from datetime import datetime
from datetime import timedelta
from Models.Package import Package
from Models.Truck import Truck
from Infrastructure.HashTable import HashTable
from Enums.PackageStatus import PackageStatus

#retrieve distance, address, and package data
with open("Data\\distanceCSV.csv") as distanceCSV:
    distanceData = list(csv.reader(distanceCSV))

with open("Data\\addressCSV.csv") as addressCSV:
    addressData = list(csv.reader(addressCSV))

with open("Data\packageCSV.csv") as packageCSV:
    packageData = list(csv.reader(packageCSV))


#loop through csv file data, create a package object for each iteration and add to hash table
def loadPackageData(fileName, hashTable):
    with open(fileName) as packageFile:
        packageData = csv.reader(packageFile)
        for package in packageData:
            id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip = package[4]
            deliveryDeadline = package[5]
            weight = package[6]
            status = PackageStatus.AT_HUB

            packageFromFile = Package(id, address, city, state, zip, deliveryDeadline, weight, status)

            #insert into hash table
            hashTable.insert(id, packageFromFile)

#get distance between two addresses
def getDistance(x, y):
    distance = distanceData[x][y]
    if distance == '':
        distance = distanceData[y][x]

    return float(distance)


#get address from string literal
def getAddress(address):
    for row in addressData:
        if address in row[2]:
            return int(row[0])


#create trucks prepped for delivery
truck1 = Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                     timedelta(hours=8))

truck2 = Truck(16, 18, None, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                     "4001 South 700 East", timedelta(hours=10, minutes=20))

truck3 = Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                     timedelta(hours=9, minutes=5))

# Create hash table
hashTable = HashTable()

#Load packages into hash table
loadPackageData("Data\packageCSV.csv", hashTable)

# Method for ordering packages on a given truck using the nearest neighbor algo
# This method also calculates the distance a given truck drives once the packages are sorted
def delivering_packages(truck):
    # Place all packages into array of not delivered
    not_delivered = []
    for packageID in truck.packages:
        package = hashTable.lookup(packageID)
        not_delivered.append(package)
    # Clear the package list of a given truck so the packages can be placed back into the truck in the order
    # of the nearest neighbor
    truck.packages.clear()

    # Cycle through the list of not_delivered until none remain in the list
    # Adds the nearest package into the truck.packages list one by one
    while len(not_delivered) > 0:
        next_address = 2000
        next_package = None
        for package in not_delivered:
            if getDistance(getAddress(truck.address), getAddress(package.address)) <= next_address:
                next_address = getDistance(getAddress(truck.address), getAddress(package.address))
                next_package = package
        # Adds next closest package to the truck package list
        truck.packages.append(next_package.id)
        # Removes the same package from the not_delivered list
        not_delivered.remove(next_package)
        # Takes the mileage driven to this packaged into the truck.mileage attribute
        truck.milesDriven += next_address
        # Updates truck's current address attribute to the package it drove to
        truck.address = next_package.address
        # Updates the time it took for the truck to drive to the nearest package
        truck.departTime += timedelta(hours=next_address / 18)
        next_package.timeDelivered = truck.departTime
        next_package.departTime = truck.departTime


# Put the trucks through the loading process
delivering_packages(truck1)
delivering_packages(truck2)
# The below line of code ensures that truck 3 does not leave until either of the first two trucks are finished
# delivering their packages
truck3.departTime = min(truck1.departTime, truck2.departTime)
delivering_packages(truck3)


class Main:
    # User Interface
    # Upon running the program, the below message will appear.
    print("Western Governors University Parcel Service (WGUPS)")
    print("The mileage for the route is:")
    print(truck1.milesDriven + truck2.milesDriven + truck3.milesDriven)  # Print total mileage for all trucks
    # The user will be asked to start the process by entering the word "time"
    text = input("To start please type the word 'time' (All else will cause the program to quit).")
    # If the user doesn't type "leave" the program will ask for a specific time in regard to checking packages
    if text == "time":
        try:
            # The user will be asked to enter a specific time
            user_time = input("Please enter a time to check status of package(s). Use the following format, HH:MM:SS")
            (h, m, s) = user_time.split(":")
            convert_timedelta = timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            # The user will be asked if they want to see the status of all packages or only one
            second_input = input("To view the status of an individual package please type 'solo'. For a rundown of all"
                                 " packages please type 'all'.")
            # If the user enters "solo" the program will ask for one package ID
            if second_input == "solo":
                try:
                    # The user will be asked to input a package ID. Invalid entry will cause the program to quit
                    solo_input = input("Enter the numeric package ID")
                    package = hashTable.lookup(int(solo_input))
                    package.updateStatus(convert_timedelta)
                    print(str(package))
                except ValueError:
                    print("Entry invalid. Closing program.")
                    exit()
            # If the user types "all" the program will display all package information at once
            elif second_input == "all":
                try:
                    for packageID in range(1, 41):
                        package = hashTable.lookup(packageID)
                        package.updateStatus(convert_timedelta)
                        print(str(package))
                except ValueError:
                    print("Entry invalid. Closing program.")
                    exit()
            else:
                exit()
        except ValueError:
            print("Entry invalid. Closing program.")
            exit()
    elif input != "time":
        print("Entry invalid. Closing program.")
        exit()
