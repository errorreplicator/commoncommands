# import tensorflow as tf
import tensorflow as tf
import numpy as np
# Create a zero filled tensor. Use the following:
zero_tsr = tf.zeros([3, 5])

# Create a one filled tensor. Use the following:
ones_tsr = tf.ones([3, 5])

# Create a constant filled tensor. Use the following:
filled_tsr = tf.fill([3, 5], 42)

# Create a tensor out of an existing constant. Use the following:\
constant_tsr = tf.constant([1, 2, 3])

zeros_similar = tf.zeros_like(constant_tsr)
ones_similar = tf.ones_like(constant_tsr)

# tensors that contain defined intervals
linear_tsr = tf.linspace(start=5.0, stop=11.0, num=3)
integer_seq_tsr = tf.range(start=6, limit=15, delta=3)

#random numbers
randunif_tsr = tf.random_uniform([3, 5], minval=0, maxval=1)

#To get a tensor with random draws from a normal distribution, as follows:
randnorm_tsr = tf.random_normal([3, 5], mean=0.0, stddev=1.0)

# generate normal random values that are assured within certain bounds
runcnorm_tsr = tf.truncated_normal([3, 5], mean=0.0, stddev=1.0)

# placecholder
x = tf.placeholder(tf.float32,shape=[2,3])
y = tf.identity(x)
x_values = np.random.rand(2,3)


sess = tf.Session()
sess = tf.InteractiveSession()

init = tf.global_variables_initializer() #init all variables
# sess.run(init)
# print(sess.run(y,feed_dict={x: x_values}))
# print(x.eval())


# sess = tf.Session()
first_var = tf.Variable(tf.zeros([2,3]))
# print(sess.run(first_var.initializer))
second_var = tf.Variable(tf.zeros_like(first_var))
# Depends on first_var
# sess.run(second_var.initializer)

identity_matrix = tf.diag([1.0, 1.0, 1.0])
A = tf.truncated_normal([2, 3])
B = tf.fill([2,3], 5.0)
C = tf.random_uniform([3,2])
D = tf.convert_to_tensor(np.array([[1., 2., 3.],[-3., -7., -1.],[0., 5., -2.]]))
# print(sess.run(identity_matrix))
# print(sess.run(A))
# print(sess.run(B))
# print(sess.run(C))
print(sess.run(D))
print(sess.run(tf.transpose(D)))
print(sess.run(tf.matrix_inverse(D)))
