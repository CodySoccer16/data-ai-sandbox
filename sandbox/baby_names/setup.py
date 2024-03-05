from pathlib import Path
import csv
import re

data_dir = Path.cwd() / 'data' / 'baby_names'
file_paths = data_dir.glob('yob*.txt')
target_file = data_dir / 'merged.csv'
target_file2 = data_dir / 'gregory.csv'
target_file3 = data_dir / 'vowels.csv'

with open(target_file, "w", newline="") as outfile, \
     open(target_file2, "w", newline="") as outfile2, \
     open(target_file3, "w", newline="") as outfile3:
    writer = csv.writer(outfile)
    writer.writerow(["Year", "Name", "Gender", "Count"])
    writer2 = csv.writer(outfile2)
    writer2.writerow(["Year", "Name", "Gender", "Count"])
    writer3 = csv.writer(outfile3)
    writer3.writerow(["Year", "Name", "Gender", "Count"])
    for file_path in file_paths:
        data_field = re.search("\d+", file_path.name).group(0)
        with open(file_path, "r") as infile:
            reader = csv.reader(infile)
            for row in reader:
                row.insert(0, data_field)
                writer.writerow(row)
                if row[1] == "Gregory":
                    writer2.writerow(row)
                if row[1][0].lower() in ["a", "e", "i", "o", "u"]:
                    writer3.writerow(row)
