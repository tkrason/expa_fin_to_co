# importing the requests library
import requests
import json


START_DATE = "2019-04-01"
END_DATE = "2019-09-30"

EXPA_TOKEN = ""

TO_FOLDER = "leto18"


for i in range(1,5000):
    URL = "https://analytics.api.aiesec.org/v2/applications/analyze.json?access_token=" + EXPA_TOKEN + "&histogram[office_id]=" + str(i) + "&end_date=" + END_DATE + "&start_date=" + START_DATE + "&histogram[type]=opportunity&histogram[interval]=month"

    print("Fetching for ID: " + str(i))

    r = requests.get(url=URL)
    data = r.json()

    try:
        data['analytics']
    except KeyError:
        print("Entity with ID [" + str(i) + "] does not exist")
        continue

    with open("./" + TO_FOLDER + "/json-"+ str(i) + ".txt", "w") as out:
        json.dump(data, out)
