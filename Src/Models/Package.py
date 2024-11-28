#Package.py
#Model class for package objects
#from Enums.PackageStatus import PackageStatus

class Package:
    def __init__(self, id, address, city, state, zip, deliveryDeadline, weight, notes, status, truck = None, timeOnTruck = None, timeDelivered = None):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryDeadline = deliveryDeadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.truck = truck
        self.timeOnTruck = timeOnTruck
        self.timeDelivered = timeDelivered

    # def updateStatus(self, convert_timedelta):
    #     if self.delivery_time < convert_timedelta:
    #         self.status = PackageStatus.DELIVERED
    #     elif self.departure_time > convert_timedelta:
    #         self.status = PackageStatus.IN_TRANSIT
    #     else:
    #         self.status = PackageStatus.AT_HUB

    def __str__(self):
        #simple formatting for displaying package info
        return(f"ID:{self.id} - {self.address} {self.city},{self.state} {self.zip} - deadline:{self.deliveryDeadline} - weight:{self.weight} - notes:{self.notes} - status:{self.status.value} - on truck:{self.truck} at {self.timeOnTruck} - delivered at:{self.timeDelivered}\n\n")
