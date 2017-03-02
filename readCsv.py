import csv

def a():

    humidity=[]
    humidityResult=[]

    f = open("C:/Users/dw/Desktop/Mosquito/Mosquito/average_data/2012_average_mosquito.csv")
    csvReader = csv.reader(f)

    for row in csvReader:
        humidity.append(row)

    print (len(humidity))

if __name__ == '__main__':
    a()