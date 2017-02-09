import tensorflow as tf
import csv,os

#This is for processing about outlier data

def outLierProcess(file):

    newMosquito = []
    f = open(file,"r")
    original = csv.reader(f)

    for row in original:
        newMosquito.append(row)

    for i in range(len(newMosquito)-2):
        if(abs(float(newMosquito[i+1][1])-float(newMosquito[i][1]))>=300):
            (newMosquito[i+1][1])=str((float(newMosquito[i][1])+float(newMosquito[i+2][1]))/2)
        else:
            continue

    myfile = open("C:/Users/dw/Desktop/urbaneco/mosquito_result/result_2014_윤중초등학교_모기포집.csv", "w")
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(newMosquito)


if __name__ == '__main__':
    outLierProcess("C:/Users/dw/Desktop/urbaneco/catch_mosquito/AllData/2014_윤중초등학교_모기포집.csv")


