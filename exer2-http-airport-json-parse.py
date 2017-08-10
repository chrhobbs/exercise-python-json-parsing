import requests

url = "http://data.maryland.gov/api/views/6jva-hr4v/rows.json"

response = requests.get(url)

json_response = response.json()
data = json_response["meta"]["view"]["columns"]
# display the average / max number of passengers per month per airline traveling through BWI airport

print(
    "========== ============================== ==================== =========" "\n"
    "ID         Airline                        Average              Largest " "\n" 
    "---------- ------------------------------ -------------------- ---------")
for i in data:
        if "cachedContents" in i:
            cached = i["cachedContents"]
            id = i["id"]
            name = i["name"]
            if "average" in cached:
                avg = i["cachedContents"]["average"]
                avg = round(float(avg),2)

            else:
                avg = "-"

            if "largest" in cached:
                lrg = i["cachedContents"]["largest"]

            else:
                lrg = "-"

            print("{0:10} {1:30} {2:20} {3:20}".format(id, name, avg, lrg))


