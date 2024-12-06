#Package.py
#Model class for package objects
#citing source:
#c950: Primary Steps Video1of3 by Robert Ferdinand

from Enums.PackageStatus import PackageStatus
from datetime import datetime

class Package:
    def __init__(self, id = None, details = None, truck = None, status = PackageStatus.AT_HUB, timeLoaded = None, timeDelivered = None):
        self.id = id
        self.details = details
        self.truck = truck
        self.status = status
        self.timeLoaded = timeLoaded
        self.timeDelivered = timeDelivered

    #print all package info (only used once delivered)
    def printDetails(self):
        self.status = PackageStatus.DELIVERED
        #account for package 9
        if self.id == 9:
            self.details[0] = "410 S State St"
            self.details[1] = "Salt Lake City"
            self.details[2] = "UT"
            self.details[3] = "84111"
            self.details[6] = "address was corrected at 10:20am"

        print('\nid: ',self.id)
        print(f'details: [ Address: \'{self.details[0]} {self.details[1]}, {self.details[2]} {self.details[3]}\' Deadline: \'{self.details[4]}\' weight: \'{self.details[5]}\' Notes: \'{self.details[6]}\' ]')
        print('truck package was loaded on: ', self.truck)
        print('status: ', self.status.value)
        print('time loaded on truck: ', self.timeLoaded)
        print('time package was delivered: ', self.timeDelivered)

    #print package info based on a time and account for the note update @10:20am
    def printDetailsAtTime(self, day, timeEntered):
        #update package 9 info if time entered is after the time we can account for the note
        noteUpdateTime = datetime(day.year, day.month, day.day, 10, 20, 0)

        if self.id == 9:
            if(timeEntered < noteUpdateTime):
                self.details[0] = "300 State St"
                self.details[1] = "Salt Lake City"
                self.details[2] = "UT"
                self.details[3] = "84103"
                self.details[6] = "Wrong address listed"
            elif(timeEntered >= noteUpdateTime):
                self.details[0] = "410 S State St"
                self.details[1] = "Salt Lake City"
                self.details[2] = "UT"
                self.details[3] = "84111"
                self.details[6] = "address was corrected at 10:20am"

        #package is at hub
        if(self.timeLoaded > timeEntered):
            self.status = PackageStatus.AT_HUB
            #print details
            print('\nid: ',self.id)
            print(f'details: [ Address: \'{self.details[0]} {self.details[1]}, {self.details[2]} {self.details[3]}\' Deadline: \'{self.details[4]}\' weight: \'{self.details[5]}\' Notes: \'{self.details[6]}\' ]')
            print('truck package to be loaded on: ', self.truck)
            print('status: ', self.status.value)
            print('Estimated loading time: ', self.timeLoaded)
            print('ETA: ', self.timeDelivered)

        #package is in transit
        elif(timeEntered >= self.timeLoaded and timeEntered < self.timeDelivered):
            self.status = PackageStatus.IN_TRANSIT
            print('\nid: ',self.id)
            print(f'details: [ Address: \'{self.details[0]} {self.details[1]}, {self.details[2]} {self.details[3]}\' Deadline: \'{self.details[4]}\' weight: \'{self.details[5]}\' Notes: \'{self.details[6]}\' ]')
            print('truck package was loaded on: ', self.truck)
            print('status: ', self.status.value)
            print('time loaded on truck: ', self.timeLoaded)
            print('ETA: ', self.timeDelivered)

        #package has been delivered
        elif(timeEntered >= self.timeDelivered):
            self.status = PackageStatus.DELIVERED
            self.printDetails()