import csv

matrix=[]

f = open("C:/Users/dw/mosquito_predict/result_factor_data/resTemperature.min.csv")
csvReader = csv.reader(f)

for row in csvReader:
    matrix.append(row)

print (len(matrix[0]))