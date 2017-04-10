import csv
import tensorflow as tf

def readCsvToList(file):
    with open(file,'r') as f:
        reader = csv.reader(f)
        factor_list = list(reader)

    return factor_list

def makeList(fList):

    factor = []
    for i in range(len(fList)):
        factor.append(float(fList[i][0]))

    return (factor)

if __name__ == '__main__':
    humidityList = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_data/humidity_result.csv")))
    rainfallList = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_data/rainfall_result.csv")))
    temperatureMaxList = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_data/temperature.max_result.csv")))
    temperatureMinList = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_data/temperature.min_result.csv")))
    temperatureAvgList = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_data/temperature.avg_result.csv")))
    mosquitoList = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/average_mosquito_data/mosquito_result.csv")))

    W1 = tf.Variable(tf.random_uniform([1], -2.0, 2.0))
    W2 = tf.Variable(tf.random_uniform([1], -2.0, 2.0))
    W3 = tf.Variable(tf.random_uniform([1], -2.0, 2.0))
    W4 = tf.Variable(tf.random_uniform([1], -2.0, 2.0))
    W5 = tf.Variable(tf.random_uniform([1], -2.0, 2.0))

    b = tf.Variable(tf.random_uniform([1], -2.0, 2.0))

    hypothesis = W1 * humidityList + W2 * rainfallList + W3 * temperatureMaxList + W4 * temperatureAvgList + W5 * temperatureMinList + b

    cost = tf.reduce_mean(tf.square(hypothesis - mosquitoList))

    learning_rate = 0.01

    optimizer = tf.train.AdamOptimizer(learning_rate)
    train = optimizer.minimize(cost)

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    for step in range(100001):
        sess.run(train)
        if step % 100 == 0:
            print(step, sess.run(cost), sess.run(W1), sess.run(W2), sess.run(W3), sess.run(W4), sess.run(W5),sess.run(b))
