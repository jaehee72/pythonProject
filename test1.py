import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

t2 = tf.ones(shape=(10, 3))
print(t2)
