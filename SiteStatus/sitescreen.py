import argparse
import time, os, csv
from selenium import webdriver

screens = "screens"
if not os.path.exists(screens):
    os.makedirs(screens)

parser = argparse.ArgumentParser(description="testparse")

parser.add_argument('-sites',
    action='store',
    dest='sites',
    default='sites.csv',
    required=False,
    help='CSV file with one site per line.')

args = parser.parse_args()

#start web driver
drv = webdriver.Chrome('/Users/ares/Applications/chromedriver')
try:
    drv.set_window_size(1024,768)
    lines = [line.rstrip('\n') for line in open(args.sites)]
    for line in lines:
        drv.get(line)
        time.sleep(2)
        name = line[7:]
        print(name)
        drv.save_screenshot('%s/%s.png' % (screens, name) )
except Exception as e:
    print("Fatal: "+str(e))
drv.quit()
