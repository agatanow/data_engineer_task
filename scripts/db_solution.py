import sqlite3 as sql
import csv
from datetime import datetime
from .queries import CREATE_CLASS_TABLE, CREATE_TEST_LEVEL_TABLE, CREATE_TEST_TABLE

class EducationDataset:
    def __init__(self, db_name, test_path, class_path, test_level_path):
        self.db = sql.connect(db_name)
        self.cursor = self.db.cursor()
        # create tables
        self.cursor.execute(CREATE_CLASS_TABLE)
        self.cursor.execute(CREATE_TEST_LEVEL_TABLE)
        self.cursor.execute(CREATE_TEST_TABLE)
        # insert values into tables
        self.load_file(class_path, 'CLASS', 9, self.convert_dates)
        self.load_file(test_level_path, 'TEST_LEVEL', 5, self.convert_dates)
        self.load_file(test_path, 'TEST', 17, self.convert_dates, self.convert_test)
        self.db.commit()
    
    def convert_dates(self, row):
        if row['updated_at'] != '':
            row['updated_at'] = datetime.strftime(datetime.strptime(row['updated_at'], '%d.%m.%y %H:%M'), '%Y-%m-%d %H:%M:%S')
        if row['created_at'] != '':
            row['created_at'] = datetime.strftime(datetime.strptime(row['created_at'], '%d.%m.%y %H:%M'), '%Y-%m-%d %H:%M:%S')

    def convert_test(self, row):
        if row['authorized_at'] != '':
            row['authorized_at'] = datetime.strftime(datetime.strptime(row['authorized_at'], '%d.%m.%y %H:%M'), '%Y-%m-%d %H:%M:%S')

    def load_file(self, path, table_name, columns_no, *f_convert):
        """Load file to table table_name in database

        Keyword arguments:
        path -- path f file which contains data to load 
        table_name -- name of table
        columns_no -- number of columns in the file
        *f_convert -- functions that convert the row so that it can be inserted into database
        """

        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            row_pat = ''.join(['?, ' for x in range(columns_no)])[:-2]
            for row in reader:
                for f in f_convert:
                    f(row)
                self.cursor.execute('INSERT OR IGNORE INTO ' + 
                                    table_name + ' VALUES (' + 
                                    row_pat + ')', list(row.values()))

    def do_task(self, task, columns_no):
        output_format = ''.join(['{} ' for x in range(columns_no)])
        res = self.cursor.execute(task).fetchall()
        for r in res:
            print(output_format.format(*r).replace('\n', ''))
            
