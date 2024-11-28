#PackageStatus.py
#contains package statuses in an enum to manage hard coded values

from enum import Enum

class PackageStatus(Enum):
    AT_HUB = 'At Hub'
    IN_TRANSIT = 'In Transit'
    DELIVERED = 'Delivered'
    FAILED = 'Failed'