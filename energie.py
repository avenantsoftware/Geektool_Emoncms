#!/usr/bin/python
# encoding: utf-8
import urllib                                       

sock = urllib.urlopen("http://yourserver.com/data/energie.php") 

htmlSource = sock.read()                            

sock.close()                                        

s = htmlSource

getal = s.split(',')

wattage = getal[0]
lengte = len(wattage)

stroomtotaal = float(getal[1])
stroomsom = (stroomtotaal-7517)

gastotaal = float(getal[2])
gassom = (gastotaal-28302)

stroomprijs = float(getal[3])
gasprijs = float(getal[4])

som = (stroomprijs+gasprijs)

if (str(lengte) == 2):
  print 'Stroomverbruik:          ' + wattage + ' W  '
if (str(lengte) == 3):
  print 'Stroomverbruik:         ' + wattage + ' W  '
else:
  print 'Stroomverbruik:        ' + getal[0] + ' W  '
print 'Stroom Meter:  ' + getal[1] + ' kWh'
print 'Gas Meter:        ' + getal[2] + ' m³ '
print 'Stroom Totaal: ' + ("%.3f" % stroomsom) + ' kWh'
print 'Gas Totaal:           ' + ("%.2f" % gassom) + ' m³ '
print 'Kosten Totaal:   € ' + ("%.2f" % som) + '   '
