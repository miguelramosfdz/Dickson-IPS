#!/usr/bin/python
# -*- coding: utf-8 -*-

""" libnmea """

from datetime import datetime
import geomag
import operator

__author__ = 'Noah Ingham'
__email__ = 'noah@ingham.com.au'

def dd2dm(dd):
    dd=abs(dd)
    d=int(dd)
    dd=str(60*(dd-d))
    m=dd if dd[2]=='.' else '0'+dd
    return "%s%s"%(d,m)

def checksum(data):
    return reduce(operator.xor, (ord(s) for s in data), 0)

def gprmc(lat,lon): # Assuming the Land of Oz

    today=datetime.utcnow()

    time= today.strftime("%H%M%S") 
    warning="A" # "A" for good, "V" for bad. I'm an optimist.
    latD=dd2dm(lat)
    if lat<0: latH="S"
    else: latH="N"
    lonD=dd2dm(lon)
    if lon<0: lonH="W"
    else: lonH="E"
    speed="000.5" # ?
    course="054.7" # ?
    dateUTC=today.strftime("%d%m%y") # Using UTC time.
    #latV=lat if latH=="N" else -lat # Combine hemisphere and latitude
    #lonV=lon if lonH=="N" else -lon # Combine hemisphere and longitude
    mag=geomag.declination(lat,lon,time=today.date() ) # See geomag library
    magD="E" if mag<0 else "W" # West or East declination?
    mag=abs(mag) # Data stored in magD 

    gprmcData="GPRMC,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"%(
            time,
            warning,
            latD,
            latH,
            lonD,
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
    lat=-35.249391
    lon=149.153513
    print(gprmc(lat,lon))
