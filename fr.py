#Importing necessary packages
from time import time
import matplotlib.pyplot as plt
import numpy as np

#importing machine learning packages
from sklearn.datasets import fetch_lfw_people

lfw_people = fetch_lfw_people(min_faces_per_people=70)
