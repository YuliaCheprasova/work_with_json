


import json
import psycopg2

def json_to_ndjson(data):
        ndJson = ''
        for j in data:
            ndJson += json.dumps(j, ensure_ascii=False) + '\n'
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
        for tuple in cursor.fetchall():
            what = json_to_ndjson(tuple[0])
            print(what)
            insert_q = " INSERT INTO temp4 (data) VALUES ((%s)::json);"
            cursor.execute(insert_q, what)

except Exception as _ex:
    print("Error while working with PostgreSQL: ", _ex)
finally:
    if connection:
        connection.close()
        print("PostgreSQL connection closed")