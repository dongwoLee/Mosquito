import tensorflow as tf
import csv

def readCsv(file):
    f = open(file)
    csvReader = csv.reader(f)
