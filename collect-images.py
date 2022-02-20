import requests
import json
import time
import csv
import urllib.request

index = 0
inputFile = open('scrapedURLs.csv', 'rt', newline='')
reader = csv.reader(inputFile)

for row in reader:
    # if index < 2:
    url = row[0]
    urllib.request.urlretrieve(url, f"data/doodles/{index}.jpg")
    print('COMPLETE - ', index)
    index += 1



