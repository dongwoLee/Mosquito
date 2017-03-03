import tensorflow as tf
import csv

def readCsvToList(file):
    with open(file,'r') as f:
        reader = csv.reader(f)
        factor_list = list(reader)

    return factor_list

if __name__ == '__main__':
    
