import tensorflow as tf
import numpy as np
import csv

xy = np.loadtxt('mosquito_factor_data.csv',delimiter=',',dtype=np.float32)

x_data = xy[:,0:-1] #factor data
y_data = xy[:,[-1]] #mosquito data

h = open('result.txt','w')

X = tf.placeholder(tf.float32,shape=[None,5])
Y = tf.placeholder(tf.float32,shape=[None,1])

W = tf.Variable(tf.random_normal([5, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.matmul(X,W) + b

cost = tf.reduce_mean(tf.square(hypothesis-Y))

optimizer=tf.train.AdamOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(50001):
    cost_val, hy_val, _ = sess.run([cost,hypothesis,train],feed_dict={X:x_data, Y:y_data})
    if step % 100 == 0:
        h.write (str(step)+" "+"Cost : "+" "+str(cost_val)+ "\nPrediction:\n"+str(hy_val))
h.close()

with open('2015_mosquito_factor_data.csv','r') as f:
    reader = csv.reader(f)
    factor_2015 = list(reader)

print (sess.run(hypothesis,feed_dict={X:[[64.6,0.5,20.7,26,15.8]]}))






