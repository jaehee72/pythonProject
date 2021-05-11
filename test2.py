import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

with tf.compat.v1.Session() as sess:
    h = tf.constant("Hello")
    w = tf.constant("World!")
    hw = h + w
    ans = sess.run(hw)
    print(ans)