# Website tester
import requests, csv

websites = "sites.csv"

with open(websites, 'r') as sites:
    status = {}
    for site in csv.reader(sites):
        data = requests.get(site[0], allow_redirects=True)
        status[site[0]] = data.status_code
        print(str(data.status_code)+"\t"+site[0])
sites.close()

print(status)
