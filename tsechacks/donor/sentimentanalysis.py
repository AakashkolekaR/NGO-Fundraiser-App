import numpy as np
#import bz2
#from keras.layers import *
from keras.models import Model,load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pandas as pd
import pickle
import tensorflow as tf

global graph,model
graph = tf.get_default_graph()
#tf.keras.backend.clear_session()
filename='C:/Users/Aakash/Desktop/Web Technology june 18/django/tsechacks/donor/finalmodel'
from sklearn.externals import joblib
tokenizer = joblib.load(filename)
model = load_model('C:/Users/Aakash/Desktop/Web Technology june 18/django/tsechacks/donor/model.h5')


def sentiment(twt):
    tf.keras.backend.clear_session()
    #twt=['good']
    
    max_features = 8192
    maxlen = 128
    embed_size = 64
    twt = tokenizer.texts_to_sequences(twt)
    twt = pad_sequences(twt, maxlen=maxlen, padding='post')
    #print(twt)
    with graph.as_default():
        sentiment = model.predict(twt,batch_size=1,verbose = 2)[0]
        if(np.argmax(sentiment) == 0):
            return 0
        elif (np.argmax(sentiment) == 1):
            return 1
