import numpy as np
import pandas as pd
import _pickle as cPickle
import random

from utils import conv, num_previous

global model

with open('model.pkl', 'rb') as f:
    global model
    model = cPickle.load(f)

def predict_next_char(s):
    '''
    Given string s of previous chars, returns predicted next char based on highest probability
    '''
    global model
    while len(s) < num_previous: s = ' ' + s
    s = s[::-1]
    s = s[:num_previous]
    arr = list(s)
    x_input = np.array([list(map(lambda c : conv(c), arr))])
    return conv(model.predict(x_input))

def predict_next_chars(s):
    '''
    Returns array of all predicted chars sorted in decreasing probability
    '''
    global model
    while len(s) < num_previous: s = ' ' + s
    s = s[::-1]
    s = s[:num_previous]
    arr = list(s)
    x_input = np.array([list(map(lambda c : conv(c), arr))])
    probs = model.predict_proba(x_input).flatten().tolist()
    chars = list(zip([conv(i) for i in range(len(probs))], probs))
    chars = sorted(chars, key = lambda c : c[1], reverse=True)
    return list(map(lambda c : c[0], chars))

def generate_story(seed, length, var):
    '''
    Generates a story using predict_next_chars with starting seed and length 
    '''
    story = seed
    while len(story) < length:
        story += predict_next_chars(story)[random.randint(0, var)]
    return story
