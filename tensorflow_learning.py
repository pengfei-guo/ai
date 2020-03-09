import tensorflow as tf

# form computation graph, include layers, inputs, functions
x1 = tf.constant(2)
x2 = tf.constant(3)
result = tf.multiply(x1,x2)
print ('tf.multiply(x1,x2) directly looks like ', result)

# use session to run the graph
with tf.Session() as sess:
	output = sess.run(result)
	print(output)

print(output + 100)
