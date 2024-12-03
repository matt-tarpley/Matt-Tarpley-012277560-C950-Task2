#Package.py
#Model class for package objects
#citing source:
#c950: Primary Steps Video1of3 by Robert Ferdinand

from Enums.PackageStatus import PackageStatus

class Package:
    def __init__(self, id = None, details = None, truck = None, status = PackageStatus.AT_HUB, timeLoaded = None, timeDelivered = None):
        self.id = id
        self.details = details
        self.truck = truck
        self.status = status
        self.timeLoaded = timeLoaded
        self.timeDelivered = timeDelivered

    #print all package info
    def printDetails(self):
        print('\nid: ',self.id)
        print(f'details: [ Address: \'{self.details[0]} {self.details[1]}, {self.details[2]} {self.details[3]}\' Deadline: \'{self.details[4]}\' weight: \'{self.details[5]}\' Notes: \'{self.details[6]}\' ]')
        print('truck package was loaded on: ', self.truck)
        print('status: ', self.status.value)
        print('time loaded on truck: ', self.timeLoaded)
        print('time package was delivered: ', self.timeDelivered)

    def printNotDeliveredDetails(self):
        print('\nid: ',self.id)
        print(f'details: [ Address: \'{self.details[0]} {self.details[1]}, {self.details[2]} {self.details[3]}\' Deadline: \'{self.details[4]}\' weight: \'{self.details[5]}\' Notes: \'{self.details[6]}\' ]')
        print('truck package was loaded on: ', self.truck)
        print('status: ', self.status.value)
        print('time loaded on truck: ', self.timeLoaded)
        print('ETA: ', self.timeDelivered)

    def printAtHubDetails(self):
        print('\nid: ',self.id)
        print(f'details: [ Address: \'{self.details[0]} {self.details[1]}, {self.details[2]} {self.details[3]}\' Deadline: \'{self.details[4]}\' weight: \'{self.details[5]}\' Notes: \'{self.details[6]}\' ]')
        print('truck package was loaded on: ', self.truck)
        print('status: ', self.status.value)
        print('Estimated loading time: ', self.timeLoaded)
        print('ETA: ', self.timeDelivered)