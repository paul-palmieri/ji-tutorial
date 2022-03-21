from fileinput import filename
from urllib import response
import urllib.request
import json
import pprint
import time

pages_to_scrap = 103
FILE_NAME = "AXA_SCRAPPING_2022_MARCH_21_WITHOUT_DUPLICATES.json"
BASE_URL = "https://recrutement.axa.fr/api/jobs?page="

AXA_feed_replica = {"data":[]}
id_dict = {} # track duplicates
num_duplicates = 0
num_offers_parsed = 0

# load pages one by one
for i in range(0, pages_to_scrap):
  page_URL = BASE_URL + str(i)

  with urllib.request.urlopen(page_URL) as url:
    res = json.loads(url.read().decode())

    # parse each reponse payload
    for job_offer in res["data"]:

      # handle dupliacates
      if(job_offer["RequisitionID"] in id_dict):
        print("Found duplicate: " + job_offer["RequisitionID"] )
        num_duplicates += 1
      else:
        id_dict[job_offer["RequisitionID"]] = 1
        AXA_feed_replica["data"].append(job_offer)
        num_offers_parsed += 1
      
    print("Page " + str(i) + " scrapped")

# breakdown
print("Found " + str(num_duplicates) + " duplicates")
print("Writing " + str(num_offers_parsed) + " to file")
print("Analyzed total of " + str(num_duplicates + num_offers_parsed) + " offers")

with open(FILE_NAME, "a") as file:
	file.write(json.dumps(AXA_feed_replica))
