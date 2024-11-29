#RouteService.py contains route optimization functions as well as utility functions necessary to implement deliveries
from Enums.PackageStatus import PackageStatus

class RouteService:

    def getDistanceBetweenAddresses(self, address1, address2, addressList, distancesList):
        if(address1 not in addressList or address2 not in addressList):
            print('unable to locate one or both addresses in the address list provided.')
            return
        else:
            i = addressList.index(address1)
            j = addressList.index(address2)
            if(i > j): #distances list is a two dimmensional array mapped corressponding to each address
                return distancesList[i][j]
            else:
                return distancesList[j][i]
            
    def getNextClosestPackage(self, truck, addressList, distancesList, hashTable):
        packageDistanceDict = dict() #<package,distance>

        for package in truck.packages:
            if(package.status != PackageStatus.DELIVERED and package.info[0] != truck.currentLocation): #if package is not delivered and the truck is not currently at its address
                #add to dictionary the package's id as the key and the distance between the trucks current location and the package's destination as the value
                packageDistanceDict[package.id] = float(self.getDistanceBetweenAddresses(truck.currentLocation, package.info[0], addressList, distancesList))

        if(len(packageDistanceDict) > 0):
            #return the min value will be the package closest to the current location (nearest neighbor)
            return hashTable.lookup(int(min(packageDistanceDict.items(), key = lambda x : x[1])[0]))
        else:
            return None