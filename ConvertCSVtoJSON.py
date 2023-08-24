import csv
import json
import os
import sys

def csv_to_json(csv_filename):
    # Get the path and filename without extension
    path, csv_file = os.path.split(csv_filename)
    filename_without_extension = os.path.splitext(csv_file)[0]

    # Construct the JSON filename
    json_filename = os.path.join(path, f"{filename_without_extension}.json")

    # Read CSV and convert to JSON
    data = []
    with open(csv_filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    # Write JSON file
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"CSV file '{csv_filename}' has been converted and saved as '{json_filename}'.")

def convert_all_csv_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            csv_filename = os.path.join(folder_path, filename)
            csv_to_json(csv_filename)

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "-a":
        current_folder = os.path.dirname(os.path.abspath(__file__))
        convert_all_csv_files_in_folder(current_folder)
    elif len(sys.argv) == 2:
        csv_filename = sys.argv[1]
        if csv_filename.endswith(".csv"):
            csv_to_json(csv_filename)
        else:
            print("Please provide a CSV file as input.")
    else:
        print("Usage: python script_name.py [-a] [input_csv_filename.csv]")
