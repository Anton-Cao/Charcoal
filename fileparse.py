import csv
from utils import conv, num_previous

inputfile = "text.txt"
outputfile = "training_data.csv"

with open(inputfile, 'r') as f:
    content = f.readlines()

content = [x.strip() for x in content]

body = ""
for line in content:
    body += line

print("Num chars:", len(body))

data = [tuple(f'p{i}' for i in range(num_previous + 1))]

cur_p = [conv(' ') for _ in range(num_previous)]
for char in body:
    cur_p.insert(0, conv(char))
    if len(cur_p) > num_previous + 1:
        cur_p.pop()
    data.append(list(cur_p))

with open(outputfile, 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(data)
