#-*- coding: UTF-8 -*-
import tensorflow as tf

class TransitionSLSTM:
  def __init__(self):
    # 参数初始化
    self.dtype = tf.float32
    self.alpha = 0.2
    self.embed_size = 100
    self.hidden_unit = 50
    self.action_count = 5
    # 数据初始化

    # 构建模型
    self.sess = tf.Session()
    self.stack = tf.placeholder(tf.float32,[self.embed_size,None])
    self.buffer = tf.placeholder(tf.float32,[self.embed_size,None])
    self.history_action = tf.placeholder(tf.float32,[self.embed_size,None])
    self.action = tf.Variable(tf.random_uniform([self.action_count,self.hidden_unit],-1,1,dtype=self.dtype))
    self.action_bias = tf.Variable(tf.random_uniform([self.action_count,self.hidden_unit],-1,1,dtype=self.dtype))
    #self.