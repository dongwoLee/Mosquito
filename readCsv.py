import csv

def a():

    humidity=[]
    humidityResult=[]

    f = open("C:/Users/dw/Desktop/urbaneco/temperature.max/temperature.max.2014.csv")
    csvReader = csv.reader(f)

    for row in csvReader:
        humidity.append(row)

    for j in range(0,len(humidity)):
        if(int(humidity[j][0][6]) >= 1 and int(humidity[j][0][6]) <= 4):
            continue
        else:
            humidityResult.append(float(humidity[j][1]))

    print (len(humidityResult))

if __name__ == '__main__':
    a()