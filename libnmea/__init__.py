#!/usr/bin/python
# -*- coding: utf-8 -*-

""" libnmea """

from datetime import datetime
import geomag
import operator

__author__ = 'Noah Ingham'
__email__ = 'noah@ingham.com.au'

def checksum(data):
    return reduce(operator.xor, (ord(s) for s in data), 0)

def gprmc(lat,lon,latH="N",lonH="E"): # Assuming the Land of Oz

    today=datetime.utcnow()

    time= today.strftime("%H%M%S") 
    warning="A" # "A" for good, "V" for bad. I'm an optimist.
    speed="000.5" # ?
    course="054.7" # ?
    dateUTC=today.strftime("%d%m%Y") # Using UTC time.
    latV=lat if latH=="N" else -lat # Combine hemisphere and latitude
    lonV=lon if lonH=="N" else -lon # Combine hemisphere and longitude
    mag=geomag.declination(latV,lonV,time=today.date() ) # See geomag library
    magD="E" if mag<0 else "W" # West or East declination?
    mag=abs(mag) # Data stored in magD 

    gprmcData="GPRMC,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"%(
            time,
            warning,
            lat,
            latH,
            lon,
            lonH,
            speed,
            course,
            dateUTC,
            mag,
            magD,
            )

    check=checksum(gprmcData)
    gprmcFormat="$%s*%X"%(gprmcData,check)

    return gprmcFormat

if __name__=="__main__":
    lat=139.1244
    lon=35.3075
    print(gprmc(lat,lon))
