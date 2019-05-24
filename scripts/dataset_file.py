import csv
# from collections import defaultdict


def load_data(file_path, f_validate, key_name='id', show_incorrect=False):
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        return {row[key_name]: row for row in reader if f_validate(row, show_incorrect)}
    

def save_dataset(data, filename, fieldnames):
    with open(filename, 'w') as res_file:
        writer = csv.DictWriter(res_file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for x in sorted(data, key = lambda x: int(x)):
            writer.writerow(data[x])
