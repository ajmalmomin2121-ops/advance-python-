import csv
import json

# Open the CSV file for reading and JSON file for writing
with open('data.csv', mode='r', encoding='utf-8') as csv_file, \
     open('output.json', mode='w', encoding='utf-8') as json_file:
    
    # Read CSV rows as dictionaries and convert them into a list
    data = list(csv.DictReader(csv_file))
    
    # Write the list into the JSON file with indentation
    json.dump(data, json_file, indent=4)

print("Conversion complete!")




