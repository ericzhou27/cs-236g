import requests
import json
import time
import csv

total = 0
offset = 0
limit = 50
collection_slug = "doodles-official"
results = []
url = f"https://api.opensea.io/api/v1/assets?order_direction=desc&offset={offset}&limit={limit}&collection={collection_slug}"

headers = {
    "Accept": "application/json",
    "X-API-KEY": "KEY HERE"
}

outputFile = open('scrapedURLs.csv', 'a')
writer = csv.writer(outputFile)

try:
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.content)
    results = data['assets']
    for result in results:
        if "image_url" in result:
            writer.writerow([result["image_url"]])
            print(total, result["image_url"])
        else:
            writer.writerow(["NULL"])
            print(total, "NULL")
        total += 1
    offset += len(results)
    url = f"https://api.opensea.io/api/v1/assets?order_direction=desc&offset={offset}&limit={limit}&collection={collection_slug}"
except Exception as e:
    print("ERROR - ", e)

while len(results) == limit:
    try:
        response = requests.request("GET", url, headers=headers)
        data = json.loads(response.content)
        results = data['assets']
        for result in results:
            if "image_url" in result:
                writer.writerow([result["image_url"]])
                print(total, result["image_url"])
            else:
                writer.writerow(["NULL"])
                print(total, "NULL")
            total += 1
        offset += len(results)
        url = f"https://api.opensea.io/api/v1/assets?order_direction=desc&offset={offset}&limit={limit}&collection={collection_slug}"
    except Exception as e:
        print("ERROR - ", e)
    time.sleep(2)