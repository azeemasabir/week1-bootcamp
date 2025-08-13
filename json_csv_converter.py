import csv
import json

def csv_to_json(csv_file, json_file):
    """Converts a CSV file to JSON format."""
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    with open(json_file, mode='w') as file:
        json.dump(data, file, indent=4)

def json_to_csv(json_file, csv_file):
    """Converts a JSON file to CSV format."""
    with open(json_file, mode='r') as file:
        data = json.load(file)
    if data:
        fieldnames = data[0].keys()
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

if __name__ == "__main__":
    # Example usage:
    csv_to_json("grades.csv", "grades.json")
    json_to_csv("grades.json", "grades_from_json.csv")
    print("Conversion complete!")
