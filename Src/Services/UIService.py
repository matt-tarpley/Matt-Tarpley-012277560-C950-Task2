#UIService.py contains methods to handle UI functionality
from datetime import datetime
from Enums.PackageStatus import PackageStatus

class UIService:
    #prints option menu
    def printMenu(self):
        print()

        print('MENU')
        print(' 1. type \'all\' to view all packages and delivery data.')
        print(' 2. type \'time\' to view packages and delivery data at a specific time')
        print(' 3. type \'find\' to search for an individual package.')
        print(' 4. type \'summary\' to see the total miles traveled and return times for all trucks')
        print(' 5. type \'exit\' to end the program.')
        print()

        command = input('type command: ')

        return command
    
    #prints all truck info ordered by truck
    def printAllTruckInfo(self, packageList1, packageList2, packageList3, hashTable):
        print()
        print('TRUCK A')
        print('*' * 20)
        for i in packageList1:
            hashTable.lookup(i).printDetails()

        print()
        print('TRUCK B')
        print('*' * 20)
        for i in packageList2:
            hashTable.lookup(i).printDetails()
        
        print()
        print('TRUCK C')
        print('*' * 20)
        for i in packageList3:
            hashTable.lookup(i).printDetails()

    #prints truck info at a time specified by the user
    def printInfoAtTime(self, day, hashTable):
        #get input time
        timeInput = input('Enter time in 24-hour format (HH:MM): ')

        #simple validation to verify that the user entered a valid time
        try:
            hr, minutes = map(int, timeInput.split(':'))
            if hr < 0 or hr > 23 or minutes < 0 or minutes > 59:
                print("Invalid time format. Please enter a valid time between '00:00' and '23:59'.")
                return
        except ValueError:
            print("Invalid time format. Please enter a valid time in 'HH:MM' format.")
            return

        # create datetime from user entry
        timeEntered = datetime(day.year, day.month, day.day, hr, minutes, 0)

        #print according to user entered time
        NUM_PACKAGES = 40
        for i in range(1, NUM_PACKAGES+1):
            package = hashTable.lookup(i)
            package.printDetailsAtTime(day ,timeEntered)

    #finds package based on user entry and prints package data
    def printPackageInfoById(self, hashTable):
        idInput = input('Enter package ID \'1-40\': ')
        id = int(str.strip(idInput))

        package = hashTable.lookup(id)

        if(package == None):
            print('invalid ID. Please try again.')
            return
        
        print()
        print('PACKAGE FOUND')
        print('*' * 20)
        package.printDetails()

    #displays each truck's return time and total miles driven
    def printSummary(self, totalMilesDriven, truckAReturnTime, truckBReturnTime, truckCReturnTime):
        endTime = max(truckAReturnTime, truckBReturnTime, truckCReturnTime)

        print()
        print('SUMMARY')
        print('*' * 20)
        print(f'start time: 08:00:00')
        print(f'end time: {endTime.strftime("%H:%M:%S")}')
        print()
        print(f'Truck A returned at {truckAReturnTime}')
        print(f'Truck B returned at {truckBReturnTime}')
        print(f'Truck C returned at {truckCReturnTime}')
        print()
        print(f'total miles driven for all trucks: {totalMilesDriven}')

        
        

