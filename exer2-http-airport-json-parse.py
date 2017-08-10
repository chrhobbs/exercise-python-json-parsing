import requests

url = "http://data.maryland.gov/api/views/6jva-hr4v/rows.json"

response = requests.get(url)

json_response = response.json()
raw_data = json_response["meta"]["view"]["columns"]
# display the average / max number of passengers per month per airline traveling through BWI airport

sanitized_data = list()

# Collect Data
for i in raw_data:
        if "cachedContents" in i:
            cached = i["cachedContents"]
            airline_id = i["id"]
            name = i["name"]
            if "average" in cached:
                avg = i["cachedContents"]["average"]
                avg = round(float(avg), 2)

            else:
                avg = "-"

            if "largest" in cached:
                lrg = i["cachedContents"]["largest"]

            else:
                lrg = "-"

            sanitized_data.append((airline_id, name, avg, lrg))

# Display Data

template = "{0:10} {1:30} {2:20} {3:20}"
print("=" * 10, "=" * 30, "=" * 20, "=" * 20)
print(template.format("ID", "Airline", "Average", "Largest"))
print("-" * 10, "-" * 30, "-" * 20, "-" * 20)

for i in sanitized_data:
    print(template.format(*i))
