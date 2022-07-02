import json
import csv


with open('veryfi-json-extracted-Grocerie.json','r') as f:
    data= json.load(f)
    line_items = data['line_items']

with open('veryfi-json-extracted-Grocerie.csv','w') as f:
    fieldnames = line_items[1].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()


