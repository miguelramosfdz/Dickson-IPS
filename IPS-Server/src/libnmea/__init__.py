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

    time= today.strftime("%H%M%S.%f").rstrip('0')
    warning="A" # "A" for good, "V" for bad. I'm an optimist.
    latD=dd2dm(lat)
    if lat<0: latH="S"
    else: latH="N"
    lonD=dd2dm(lon)
    if lon<0: lonH="W"
    else: lonH="E"
    speed="0" # ?
    course="" # ?
    dateUTC=today.strftime("%d%m%y") # Using UTC time.
    mag=geomag.declination(lat,lon,time=today.date() ) # See geomag library
    magD="E" if mag<0 else "W" # West or East declination?
    mag=abs(mag) # Data stored in magD 

    gprmcData="GPRMC,%s,%s,%s,%s,%s,%s,%s,%s,%s,%f.00,%s"%(
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
    gprmcFormat="$%s*%X\r\n"%(gprmcData,check)

    return gprmcFormat

# Covert meter coordinates, with origin (0,0), to latitude and longitude.
def metric2ll(x,y):
    base=[0.0,0.0]
    ll = [ base[0]+x/(30.0+13.0/15.0) , base[1]+y/(30.0+13.0/15.0) ]
    return latlong

if __name__=="__main__":
    lat=-35.249391
    lon=149.153513
    psrint(gprmc(lat,lon))
