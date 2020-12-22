'''
Created on 5 Nov 2020

@author: aki
'''


import os

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)