import json
import math
# import .pincode.json
import os

class PincodeDistance:
    def __init__(self):
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, 'pincode.json')
        f = open (file_path, "r")
        self.codes = json.loads(f.read())

    def toRad(self,value):
        RADIANT_CONSTANT = 0.0174532925199433
        return value * RADIANT_CONSTANT


    def calculategeoDistance(self,start, end):
        KM_RATIO = 6371
        dLat = self.toRad(end["lat"] - start["lat"])
        dLon = self.toRad(end["lng"] - start["lng"])
        lat1Rad = self.toRad(start["lat"])
        lat2Rad = self.toRad(end["lat"])
        a =math.sin(dLat / 2) * math.sin(dLat / 2) +math.sin(dLon / 2) * math.sin(dLon / 2) * math.cos(lat1Rad) * math.cos(lat2Rad)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        dMtrs = KM_RATIO * c
        return dMtrs

    def getlatLng(self,pincode):
        if str(pincode) not in self.codes:
            return self.codes["110001"]
        return self.codes[str(pincode)]

    def getDistance(self,toPincode, fromPincode):
        distance = 1
        toCoords = self.getlatLng(toPincode)
        fromCoords = self.getlatLng(fromPincode)
        distance = self.calculategeoDistance(toCoords, fromCoords)
        if toPincode is fromPincode:
            distance = 1
        return distance
