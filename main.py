import json
import psycopg2

def json_to_ndjson(data):
    ndJson = ''
    for j in data:
        ndJson += json.dumps(j, ensure_ascii=False) + '\n'
        for m in j["laureates"]:
            ndJson += json.dumps(m, ensure_ascii=False) + '\n'
    return ndJson

try:
    connection = psycopg2.connect(
        user="postgres",
        password="22424",
        host="127.0.0.1",
        port="5432",
        database="work_with_json"
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        show_table_q = f"SELECT * FROM temp3;"
        cursor.execute(show_table_q)
        what = json_to_ndjson([{"year":"2022","category":"chemistry","laureates":[{"id":"1015","firstname":"Carolyn","surname":"Bertozzi","motivation":"\"for the development of click chemistry and bioorthogonal chemistry\"","share":"3"},{"id":"1016","firstname":"Morten","surname":"Meldal","motivation":"\"for the development of click chemistry and bioorthogonal chemistry\"","share":"3"},{"id":"743","firstname":"Barry","surname":"Sharpless","motivation":"\"for the development of click chemistry and bioorthogonal chemistry\"","share":"3"}]},{"year":"2022","category":"economics","laureates":[{"id":"1021","firstname":"Ben","surname":"Bernanke","motivation":"\"for research on banks and financial crises\"","share":"3"},{"id":"1022","firstname":"Douglas","surname":"Diamond","motivation":"\"for research on banks and financial crises\"","share":"3"},{"id":"1023","firstname":"Philip","surname":"Dybvig","motivation":"\"for research on banks and financial crises\"","share":"3"}]}])
        print(what)
        #for tuple in cursor.fetchall():


            #insert_q = " INSERT INTO temp4 (data) VALUES ((%s)::json);"
            #cursor.execute(insert_q, what)

except Exception as _ex:
    print("Error while working with PostgreSQL: ", _ex)
finally:
    if connection:
        connection.close()
        print("PostgreSQL connection closed")