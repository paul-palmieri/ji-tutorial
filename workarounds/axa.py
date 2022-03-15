from urllib import response
import urllib.request
import json
import pprint
import time


AXA_feed_replica = {"data":[]}
id_dict = {} # track duplicates
num_duplicates = 0
num_offers = 0

# todo change to 96 when done (or more next days) - 0 - 1 0 - 96
for i in range(0, 10):
  print("Scrapping page: " + str(i))
  URL = "https://recrutement.axa.fr/api/jobs?page=" + str(i)
  with urllib.request.urlopen(URL) as url:
    res = json.loads(url.read().decode())


    for job_offer in res["data"]:
      if(job_offer["RequisitionID"] in id_dict):
        print("found duplicate id " + job_offer["RequisitionID"] )
        num_duplicates += 1
        pass
      else:
        id_dict[job_offer["RequisitionID"]] = 1
        AXA_feed_replica["data"].append(job_offer)
        num_offers += 1

      # some prints to follow the scrapping along
      if(num_offers % 100 == 0):
        print("Added " + str(num_offers))
      
    print("Page " + str(i) + " scrapped")

      


print("Writing " + str(num_offers) + " to file")
print("Found " + str(num_duplicates) + " duplicates")

with open("AXA_SCRAPPING_2022_MARCH_15_WITHOUT_DUPLICATES_10_PAGES.txt", "a") as file:
	file.write(json.dumps(AXA_feed_replica))

# JSON_data["data"].append(response_data)

# # print(JSON_data)

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(JSON_data)

# json.dump(JSON_data, "test_file.json")





