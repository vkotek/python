# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 22:58:50 2015

@author: pirate

Python 2
"""

"""

1) Set details: Continent, min city size, number of cities
2) Import cities from file into dictionary
3) Get random selection from dictionary
4) Print to CSV

"""     

import csv
from math import sqrt
import time
import random

file = "cities15000.txt"

arrayContinents = { 1:'Europe',
                    2:'America',
                    3:'Pacific',
                    4:'Asia',
                    5:'Africa',
                    6:'Atlantic'
                    }
listConts = []
for cont in arrayContinents:
    listConts.append(arrayContinents[cont])


def setVars(): # Start menu and set variables
    print "Choose the continent.."
    for item in arrayContinents:
        print item, arrayContinents[item]
    try:
        xContinent = int(raw_input(": "))
        xSize = int(raw_input("Minimum city population: "))
        
    except:
        print "Wrong input, try again!\n"
        time.sleep(1)
        setVars()

    # Create fancy population (1000000 => 1M)
    if (xSize / 1000000) > 0:
        xSizeFormatted = "%d%s" % ((xSize / 1000000), "M")
    elif (xSize / 1000) > 0:
        xSizeFormatted = "%d%s" % ((xSize / 1000), "K")
    else:
        xSizeFormatted = xSize
        
    print "\nContinent: %s\n%s population\n" % (getContinent(xContinent),xSizeFormatted)
    #time.sleep(2)
    raw_input("Enter to continue...")

    # set filename with fancy population
    filename = "%s_%s" % (getContinent(xContinent), xSizeFormatted)
    
    getCities(xContinent,xSize,filename)
    
    
def getCities(xContinent,xSize,filename):
           
    # Open read and write files
    cityList = []
    with open(file, mode='r') as csvfile:
        openCSV = csv.reader(csvfile, delimiter="\t")
        for row in openCSV:
            wData = row[17].split('/')
            wCont = wData[0]
            pop = int(row[14])
            if wCont == getContinent(xContinent) and pop >= xSize:
                city = row[2]
                country = row[8]
                pos_lat = row[4]
                pos_long = row[5]
                cityList.append([city,country,pop,pos_lat,pos_long])
        print "Total cities found:", len(cityList)
        xCount = int(raw_input("Number of cities to select: "))
    csvfile.close()
    
    filename = "%s_%d" % (filename, xCount)
    
    try:
        citySelect = random.sample(cityList,xCount)
    except ValueError:
        print "Sample larger than population.\n"
        time.sleep(1)
        setVars()
        
    for city in citySelect:
        print city[1], "\t", city[0].ljust(16), "\t", city[2]
    confirm = raw_input("Confirm? (y/n)")
    if confirm == 'y':
        writeCities(citySelect,filename)
    elif confirm == 'n':
        choice = int(raw_input("1) New random sample\n2) New search\n..."))
        if choice == 1:
            getCities(xContinent,xSize,filename)
        elif choice == 2:
            setVars()
        else:
            print "Error"
                
                
def writeCities(citySelect,filename):
    newFile = open("%s.csv" % filename, mode="w")
    csvWriter = csv.writer(newFile, delimiter=",")
    # csvWriter.writerow(["City","Country","Population","Latitude","Longitude"]) # Write headers
    for city in citySelect:
        csvWriter.writerow([city[0],city[1],city[2],city[3],city[4]])
    print "Written %d items to %s.csv" % (len(citySelect), filename)
    newFile.close()
    exit()
    


def getContinent(xContinent): #Gets continent name from number
    return arrayContinents[xContinent]

def dbExport():
    with open(file, mode='r') as infile:
        x = 0
        outfile = open('db_all.csv', mode='w')
        outwrite = csv.writer(outfile, delimiter=",")
        inData = csv.reader(infile, delimiter="\t")
        for city in inData:
            inCont= city[17].split('/')
            inCont = inCont[0]
            if inCont in listConts:
                cityInfo = ",".join([inCont,city[2],city[14],city[4],city[5     ]])
                outwrite.writerow(cityInfo)
                x+=1
        print x, "items exported"
    infile.close()
    outfile.close()
                

# Set variables 
def menu():
    print """
    1) Make cards
    2) Export all
    """
    menu_choice = int(raw_input(".."))
    if menu_choice == 1:
        setVars()
    elif menu_choice == 2:
        dbExport()
        

menu()
# Confirm cities, export

