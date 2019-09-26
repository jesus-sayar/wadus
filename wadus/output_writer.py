import csv
from terminaltables import AsciiTable

class OutputWriter:
    def __init__(self, output_type='table', filename='output'):
        self.filename = filename
        switch = {
            "table": self.write_console_table,
            "csv": self.write_csv
        }
        self.write =  switch.get(  output_type , self.write_console_table )

    def write_csv(self, table_headers, table_data):
        try:
            with open(self.filename, 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(table_headers)
                for data in table_data:
                    writer.writerow(data)
        except IOError:
            print("I/O error, permission errors or path doesn't exist") 

    def write_console_table(self, table_headers, table_data):
        table_data.insert(0, table_headers)
        table = AsciiTable( table_data )
        print(table.table)
    