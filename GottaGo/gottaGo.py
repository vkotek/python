#!/usr/bin/python
# coding: utf-8

try:
    import urllib2, json
    import ConfigParser
    from math import sqrt, atan, pi
except:
    print "Error importing modules, exiting."
    exit()

config = ConfigParser.RawConfigParser()
config.read('config.ini')
apiKey = config.get('settings','api')
apiWC = "http://opendata.iprpraha.cz/CUR/FSV/FSV_VerejnaWC_b/WGS_84/FSV_VerejnaWC_b.json"

def parseToilets():

    urlJSON = json.loads(urllib2.urlopen(apiWC).read())

    toilets = []

    for item in urlJSON['features']:
        toilet = {}
        jcord = item['geometry']['coordinates']
        toilet["x"] = jcord[0]
        toilet["y"] = jcord[1]

        toilets.append(toilet)
        print toilet

parseToilets()

exit()

# Returns list of nearest bathrooms to given coordinates
def getToilets(coords):

    # URL of Prague OpenData public bathrooms API
    url = "http://opendata.iprpraha.cz/CUR/FSV/FSV_VerejnaWC_b/WGS_84/FSV_VerejnaWC_b.json"

    # Open URL and load JSON into dict?
    urlJSON = json.loads(urllib2.urlopen(url).read())

    # Set resutls var and wcID (primary key)
    results = []
    wcID = 0

    # Iterate through toilets in dict
    for item in urlJSON['features']:
        wcID+=1
        jsonCoords = item['geometry']['coordinates'] # Set location of coordinates in JSON
        # Get raw coordinates
        coor_x = jsonCoords[0]
        coor_y = jsonCoords[1]
        # Get difference in coordiantes and multiply to conver to meters (rough estimate)
        # Assuming that 1 degree is 1/360 the circumference of earth
        dis_x = -(coords['lng'] - coor_x)*104000
        dis_y = -(coords['lat'] - coor_y)*104000
        # use inverse tangent to get the angle formed by the opposite and adjacent sides (coord. diffs)
        head = atan(dis_x/float(dis_y))*(180/pi)
        # Pythagoras to get the distance in metres (length of hypotenuse)
        dis = sqrt(dis_x**2+dis_y**2)
        # This monster tries to covert the angle to 360 degree bearing by using +/- values of distance (unit circle)
        # There might be bug here somewhere, needs to be checked.
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
        try: # Try to get the type of WC (could be missing)
            wcType = item['properties']['TYP']
        except: # Insert N/A if not found
            wcType = "N/A"
            continue
        try: # Try get the address and insert N/A if not found
            wcLocation = item['properties']['LOKALITA']
        except:
            wcLocation = "N/A"
            continue
        try: # Try get open times, N/A if not found
            wcOpen = item['properties']['OTEVRENO']
        except:
            wcOpen = "N/A"
            continue
        try: # Try get price... Convert to ENG
            wcPrice = item['properties']['CENA']
            if wcPrice == 'zdarma':
                wcPrice = "free"
            else: # If there is a price, extract the value from string (trim)
                wcPrice = wcPrice[len(wcPrice)-5:]
        except:
            wcPrice = "N/A"
            continue

        # Add results to the results list
        results.append([wcID,dis,dis_x,dis_y,round(head,2),wcType,wcLocation,wcPrice,wcOpen])
    return results

# Function that takes the results list of lists and displays it with nice formating
def showResults(results):
    toiletSorted = sorted(results, key=lambda wc: wc[1])
    i = 1
    for toilet in toiletSorted:
        distance,dis_x,dis_y,head = toilet[1],toilet[2],toilet[3],toilet[4]
        wcType, location, price, wcOpen = toilet[5], toilet[6], toilet[7], toilet[8]
        print location, "\n\t", format(distance,".0f") + "m\t", format(head,".0f")+ "°\t", price, "\t", wcOpen
        i+=1
        if i>6: # Sets the number of closest toilets to show
            break

# Converts text address to GPS coordinates
def googleGeocode(address):

    # WARNING: Google API key has been removed!!
    googleKey = apiKey
    googleUrl = "https://maps.googleapis.com/maps/api/geocode/json?"
    googleParams = "address=" + address.replace(" ", "+") + "&key=" + googleKey
    coords = json.loads(urllib2.urlopen(googleUrl+googleParams).read())
    latlng = coords['results'][0]['geometry']['location']
    return latlng


# Let user input address, run function to convert it to coordinates
uCoords = googleGeocode(str(raw_input("Your address: ")))
#uCoords = googleGeocode("Legerova 33, Praha 2")

# Input coordinates into toilet formula to get raw results
results = getToilets(uCoords)

# Display formatted results
showResults(results)
