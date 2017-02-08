import csv

matrix=[]

f = open("C:/Users/dw/Desktop/urbaneco/result/resHumidity.csv")
csvReader = csv.reader(f)

for row in csvReader:
    matrix.append(row)

print (len(matrix[0]))