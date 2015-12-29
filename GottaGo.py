# -*- coding: utf-8 -*-


import urllib2
import json
import turtle as tr
import time
from math import sqrt, atan, pi

def getToilets(coords):
    url = "http://opendata.iprpraha.cz/CUR/FSV/FSV_VerejnaWC_b/WGS_84/FSV_VerejnaWC_b.json"

    urlJSON = json.loads(urllib2.urlopen(url).read())
    
    results = []
    wcID = 0
    for item in urlJSON['features']:
        wcID+=1
        jsonCoords = item['geometry']['coordinates']
        coor_x = jsonCoords[0]
        coor_y = jsonCoords[1]
        dis_x = -(coords['lng'] - coor_x)*104000
        dis_y = -(coords['lat'] - coor_y)*104000
        head = atan(dis_x/float(dis_y))*(180/pi)
        dis = sqrt(dis_x**2+dis_y**2)
        if dis_x > 0 and dis_y > 0:
            head = head
        elif dis_x > 0 and dis_y < 0:
            head = 180 + head
        elif dis_x < 0 and dis_y < 0:
            head = 180 + head
        elif dis_x < 0 and dis_y > 0:
            head = 360 + head
        else:
            continue
        try: # Try type of WC
            wcType = item['properties']['TYP']
        except:
            wcType = "N/A"
            continue
        try: # Try get address
            wcLocation = item['properties']['LOKALITA']
        except:
            wcLocation = "N/A"
            continue
        try: # Try get open times
            wcOpen = item['properties']['OTEVRENO']
        except:
            wcOpen = "N/A"
            continue
        try: # Try get price
            wcPrice = item['properties']['CENA']
            if wcPrice == 'zdarma':
                wcPrice = "free"
            else:
                wcPrice = wcPrice[len(wcPrice)-5:]
        except:
            wcPrice = "N/A"
            continue
            
        results.append([wcID,dis,dis_x,dis_y,round(head,2),wcType,wcLocation,wcPrice,wcOpen])
    return results

def showResults(results):
    toiletSorted = sorted(results, key=lambda wc: wc[1])
    i = 1
    for toilet in toiletSorted:
        distance,dis_x,dis_y,head = toilet[1],toilet[2],toilet[3],toilet[4]
        wcType, location, price, wcOpen = toilet[5], toilet[6], toilet[7], toilet[8]
        print location, "\n\t", format(distance,".0f") + "m\t", format(head,".0f")+ "°\t", price, "\t", wcOpen
        turtleDraw(head,distance)
        i+=1
        if i>6:
            break
            
def googleGeocode(address):

    googleKey = "REMOVED"
    googleUrl = "https://maps.googleapis.com/maps/api/geocode/json?"
    googleParams = "address=" + address.replace(" ", "+") + "&key=" + googleKey
    coords = json.loads(urllib2.urlopen(googleUrl+googleParams).read())
    latlng = coords['results'][0]['geometry']['location']
    return latlng

def turtleDraw(heading, distance):
    tr.goto(0,0)
    tr.seth(heading)
    tr.forward(distance/10)

uCoords = googleGeocode(str(raw_input("Your address: ")))
#uCoords = googleGeocode("Legerova 33, Praha 2")
results = getToilets(uCoords)
showResults(results)

while True:
    time.sleep(1)
