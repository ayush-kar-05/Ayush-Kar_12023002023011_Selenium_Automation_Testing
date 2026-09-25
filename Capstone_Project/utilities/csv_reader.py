import csv


def read_test_data(file_path):
    data = []

    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)  #DictReader reads the CSV file and treats each row like a dictionary.

        for row in reader:
            data.append(row)

    return data