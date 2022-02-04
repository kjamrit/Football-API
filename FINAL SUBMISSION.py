import requests
import csv
import json

plan=input("Enter the required tier in format <TIER_NO.>,for example.. TIER_TWO   :- ")

url='http://api.football-data.org'

finalurl= f'{url}/v2/competitions?plan={plan}'

headers = { 'X-Auth-Token': 'cda82a1bdbc84333b46a6f82df30cb60' }

response = requests.get(finalurl, headers=headers).json()

fields=['id','Name','Area/Country','Available Seasons','Tier']

rows=[]

for i in response["competitions"]:
    p=i["plan"]
    if p==plan:
        instance=[]
        instance.append(i["id"])
        instance.append(i["name"])
        instance.append(i["area"]["name"])
        instance.append(i["numberOfAvailableSeasons"])
        instance.append(i["plan"])
        rows.append(instance)


with open('footballdata.csv', 'w') as d:
    csvwriter=csv.writer(d)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

print(finalurl)

