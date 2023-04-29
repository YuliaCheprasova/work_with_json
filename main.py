import json
import psycopg2
import re

"""with open("bigproba.json", "r") as f:
    line=f.readline()
    line = line.replace("{\"result\": {", "[")
    line = line.replace("\"event\": ", "")
    line = line.replace("}}}", "}]")
    line = line.replace("\\u", "")
    line = line.replace("\\/", "")
    line = re.sub()

    with open ('hope.json', 'w') as f1:
        f1.write(line)"""

"""with open ('hope.json', 'r') as f4:
    line = f4.readline()
    line = line.replace("\\u", "")
    line = line.replace("\\/", "")
    with open('hope3.json', 'w') as f5:
        f5.write(line)"""

"""with open ('hope2.json', 'r') as f4:
    line = f4.readline()
    line = line.replace("\"\"", "")
    with open('hope4.json', 'w') as f5:
        f5.write(line)"""

with open('hope4.json', 'r') as f2:
    data = json.load(f2)
    ndJson = ''
    for j in data:
        ndJson += json.dumps(j, ensure_ascii=False) + '\n'
with open('ndjson1.json', 'w') as f3:
    f3.write(ndJson)

