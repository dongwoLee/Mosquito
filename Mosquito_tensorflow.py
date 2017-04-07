import tensorflow as tf
import numpy as np

xy = np.loadtxt('mosquito_factor_data.csv',delimiter=',',dtype='float32')

x_data = xy[0:-1]
y_data = xy[-1]

W = tf.Variable(tf.random_uniform([1, len(x_data)],-1,1))
b = tf.Variable(tf.random_uniform([1],-1,1))

hypothesis = tf.matmul(W ,x_data)

