import csv

import pytest


def read_csv(file):
    data=[]
    with open(file) as file:
        reader = csv.reader(file,delimiter=';')
        for rows in reader:
            if reader.line_num==1:
                pass
            else:
                data.append(rows)
    return data

# print(read_csv())