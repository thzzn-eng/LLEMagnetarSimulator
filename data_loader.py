import csv

def load_data(file_path):
    magnetars = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            magnetars.append(row)
    return magnetars