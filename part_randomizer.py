import random
import json

in_file = 'polling_locations_subset_2011.json'

in_json = open(in_file)
in_json = in_json.read()
in_json = json.loads(in_json)

output = []
with open('checkout.json','w') as out_file:
    i = 0

    while i < len(in_json["features"]):
        struct = {"lat": in_json["features"][i]["geometry"]["coordinates"][1],"lng": in_json["features"][i]["geometry"]["coordinates"][0], "turnout": int(random.random() * 50)}
        output.append(struct)
        i += 1
    json.dump(output, out_file)

