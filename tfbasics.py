import tensorflow as tf

#build computation graph
x1 = tf.constant(5)
x2 = tf.constant(6)

#result = tf.mul(x1,x2)

result = x1*x2

print(result)

#build whats supposed to happen
'''
sess = tf.Session()
print(sess.run(result))
sess.close()
'''

#opens and closes your session so you dont have to think about it
with tf.Session() as sess:
	output = sess.run(result)
	print(output)

print(output)
