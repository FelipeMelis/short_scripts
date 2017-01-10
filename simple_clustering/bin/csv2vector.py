#!/usr/bin/env python

import sys
import csv
from itertools import islice


csv.register_dialect('excel', delimiter=';', quoting=csv.QUOTE_NONE)

def open_excel_csv():
    csv_file = open(sys.argv[1], 'rb')
    global reader
    reader = csv.reader(csv_file, 'excel')
        
def vector_numbers():
    for i in reader:
        number = len(i)-1
    print number    
            
def create_vector():
    for line in islice(reader, 1, None):
        print line[0]
        for vector in line[1:]:
            print vector    

#sys.stdout = open('csv.vec', 'w')
        
open_excel_csv()
vector_numbers()
open_excel_csv()
create_vector()