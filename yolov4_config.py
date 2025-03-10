# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:41:08 2020

@author: Quang Nguyen
"""

""" 
Generating custom cfg/yolov4_custom_train.cfg
and cfg/yolov4_custom_test.cfg

"""

classes=1
max_batches=2000
batch=16
subdivisions=16
width=320
height=224
channels=3
momentum=0.949
decay=0.0005
learning_rate=0.001
steps= (6400,7200)
scales=(0.1,0.1)
