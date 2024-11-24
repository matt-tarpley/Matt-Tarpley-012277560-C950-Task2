#Package.py
#Model class for package objects

class Package:
    def __init__(self, id, address, city, state, zip, deliveryDeadline, weight, notes, status, truckLoadedOn, timeOnTruck, timeDelivered):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryDeadline = deliveryDeadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.truckLoadedOn = truckLoadedOn
        self.timeOnTruck = timeOnTruck
        self.timeDelivered = timeDelivered

    def PrintInfo(self):
        #simple formatting for displaying package info
        print(f"{self.id}-{self.address} {self.city},{self.state} {self.zip}-deadline: {self.deliveryDeadline}-weight: {self.weight}-notes: {self.notes}-status: {self.status}-on truck: {self.truckLoadedOn} at {self.timeOnTruck}-delivered at: {self.timeDelivered}\n\n")
