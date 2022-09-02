import tensorflow as tf
from tensorflow.keras import layers
class my_loss(tf.keras.losses.Loss):

    def __init__(self,e1,e2,**kwargs):
        assert e1 > e2 , "e1 must be greater than e2"
        self.e1 = e1
        self.e2 = e2
        super().__init__(**kwargs)

    def call(self,Y_true,Y_pred):
        print(Y_true, Y_pred)
        d = tf.reduce_mean(tf.abs(Y_true-Y_pred), axis=0)
        print(d)
        l1 = d**1.5  # Where the error is large, show the loss much more
        l2 = d*1.5   # Where the error is moderate, show the loss slightly more.
        l3 = d
        print('brah')
        print([self.e2 < d < self.e1])
        # res = tf.experimental.numpy.select([tf.reduce_any(d >= self.e1),tf.reduce_any(self.e2 < d < self.e1), tf.reduce_any(d <= self.e2)], [l1,l2,l3])
        # res = tf.cond(tf.less_equal(d, self.e1), lambda: l1, lambda: tf.cond(tf.less()))
        res = tf.experimental.numpy.select([
            d >= self.e1, 
            tf.math.logical_and(self.e2 < d, d < self.e1),
            self.e2 <= d], [l1,l2,l3]
        )
        return res

    def get_config(self):
        parent_config = super().get_config()
        return {**parent_config,"e1":self.e1,"e2":self.e2}

model = tf.keras.models.Sequential()
model.add(layers.Dense(50,input_dim=9)) # Length of features is 9
model.add(layers.Dense(50))
model.add(layers.Dense(50))
model.add(layers.Dense(1))

import numpy as np
x_train = np.ones((1, 9))
y_train = np.ones((1, 1))
model.compile(
   loss=my_loss(2,0.5),
   optimizer="adam",
   # metrics=["accuracy"]
)

hist = model.fit(x_train,y_train,epochs=50)
