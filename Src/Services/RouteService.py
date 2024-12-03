#RouteService.py
#contains route optimization functions, utility functions necessary to implement deliveries, and the delivery implementation
#citing sources:
    #c950: Primary Steps Video2of3 by Robert Ferdinand
    #c950: Primary Steps Video3of3 by Robert Ferdinand

from Enums.PackageStatus import PackageStatus
from datetime import timedelta

class RouteService:

    #returns the distance between two addresses
    def getDistanceBetweenAddresses(self, address1, address2, addressList, distancesList):
        if(address1 not in addressList or address2 not in addressList):
            print('unable to locate one or both addresses in the address list provided.')
            return
        else:
            i = addressList.index(address1)
            j = addressList.index(address2)
            if(i > j): #distances list is a two dimmensional array with values corressponding to each address
                return distancesList[i][j]
            else:
                return distancesList[j][i]
            
    #returns the package whos distance is closest to the trucks current location
    def getNextClosestPackage(self, truck, addressList, distancesList, hashTable):
        packageDistanceDict = dict() #<package,distance>

        for package in truck.packages:
            if(package.status != PackageStatus.DELIVERED and package.details[0] != truck.currentLocation): #if package is not delivered and the truck is not currently at its address
                #add to dictionary the package's id as the key and the distance between the trucks current location and the package's destination as the value
                packageDistanceDict[package.id] = float(self.getDistanceBetweenAddresses(truck.currentLocation, package.details[0], addressList, distancesList))

        if(len(packageDistanceDict) > 0):
            #return the min value will be the package closest to the current location (nearest neighbor)
            return hashTable.lookup(int(min(packageDistanceDict.items(), key = lambda x : x[1])[0]))
        else:
            return None
        
    #deliver packages using nearest neighbor approach
    def deliverPackages(self, truck, addressList, distancesList, hashTable):
        TRUCK_SPEED = 18/60 #.3 miles per minute
        stillHasPackages = True
        totalDistance = 0.0

        while stillHasPackages:
            package = self.getNextClosestPackage(truck, addressList, distancesList, hashTable) #get the next closest package
            if(package == None):
                stillHasPackages = False
                break
            else:
                # Correct the address for package 9
                if package.id == 9:
                    package.details[0] = "410 S State St"
                    package.details[1] = "Salt Lake City"
                    package.details[2] = "UT"
                    package.details[3] = "84111"
                    package.details[6] = "Incorrect address was corrected"

                #deliver package and update package/truck data
                package.status = PackageStatus.DELIVERED
                distance = self.getDistanceBetweenAddresses(truck.currentLocation, package.details[0], addressList, distancesList)
                truck.currentTime += timedelta(minutes = float(distance/TRUCK_SPEED))

                package.timeDelivered = truck.currentTime
                totalDistance += distance
                truck.currentLocation = package.details[0]
                hashTable.update(package.id, package)

        #used to determine start time of third truck
        distanceToHub = self.getDistanceBetweenAddresses(truck.currentLocation, addressList[0], addressList, distancesList)
        truck.currentTime += timedelta(minutes = float(distanceToHub/TRUCK_SPEED))

        return [distanceToHub, totalDistance, truck.currentTime]

