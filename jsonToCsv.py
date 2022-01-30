import json
import csv

with open("UN_Hscode.json") as f:
    data = json.load(f)
 
 
with open("unHscode.csv", "w") as f:
    csv_file = csv.writer(f)
    csv_file.writerow(["Classification","Code",	"Description",	"Code Parent",	"Level", "isLeaf"])
    for item in data:
        csv_file.writerow([item['classification'], item['code'], item['description'], item['parent_code'],item['level'],item['isLeaf']])
    