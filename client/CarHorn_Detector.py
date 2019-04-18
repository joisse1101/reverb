# -*- coding: utf-8 -*-
"""ReDesign

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12xS9ST-wVdYhVQjCSDsYY_v6AowgY6i5
"""

import h5py
import keras

import numba
import numpy as np 
import librosa

from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical


from keras.models import load_model
model = load_model('/home/pi/reverb/client/weights.best.basic_mlp.hdf5')


def extract_feature(file_name):
   
    try:
        audio_data, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 
        mfccs = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=40)
        mfccsscaled = np.mean(mfccs.T,axis=0)
        
    except Exception as e:
        print("Error encountered while parsing file: ", file)
        print("error: ", e)
        return None, None

    return np.array([mfccsscaled])

def print_prediction(file_name):
    #file_name = '/home/pi/reverb/client/temp/' + file_name
    print('file name ' + file_name)
    prediction_feature = extract_feature(file_name) 

    predicted_vector = model.predict_classes(prediction_feature)
    predicted_class = le.inverse_transform(predicted_vector) 
    print("The predicted class is:", predicted_class[0], '\n') 

    predicted_proba_vector = model.predict_proba(prediction_feature) 
    predicted_proba = predicted_proba_vector[0]
    for i in range(len(predicted_proba)): 
        category = le.inverse_transform(np.array([i]))
        print(category[0], "\t\t : ", format(predicted_proba[i], '.32f') )



category = ['air_conditioner', 'car_horn', 'children_playing', 'dog_bark', 'drilling', 'engine_idling', 'gun_shot', 'jackhammer', 'siren', 'street_music']

le = LabelEncoder()
le.fit(category)

#filename = '419698__14fvaltrovat__short-horn.wav' 
#print_prediction(filename)