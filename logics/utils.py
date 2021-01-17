import csv
import sqlite3
from dateutil.parser import parse


def migrate_csv_to_db(path):

    conn = sqlite3.connect('C:\\Users\\risha\\Documents\\PyCharm\\InsuranceDashboard\\db.sqlite3')
    cur = conn.cursor()
    cur.execute("DELETE FROM logics_customerpolicydetails")
    with open(path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row.
        for row in reader:
            d = parse(row[1]).date()
            row[1] = d
            cur.execute(
                "INSERT INTO logics_customerpolicydetails VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                row
            )
    conn.commit()


migrate_csv_to_db('C:\\Users\\risha\\Documents\\PyCharm\\InsuranceDashboard\\Data Set - Insurance Client.csv')
