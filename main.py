import json
import psycopg2

with open("bigproba.json", "r") as f:
    line=f.readline()
    line = line.replace("{\"result\": {", "[")
    line = line.replace("\"event\": ", "")
    line = line.replace("}}}", "}]")
    print(line)
    with open ('hope.json', 'w') as f1:
        f1.write(line)

with open('hope.json', 'r') as f2:
    data = json.load(f2)
    ndJson = ''
    for j in data:
        ndJson += json.dumps(j, ensure_ascii=False) + '\n'
with open('ndjson1.json','w') as f3:
    f3.write(ndJson)
print(ndJson)