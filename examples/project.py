#Numpy deals with large arrays and linear algebra
import numpy as np 
# Library for data manipulation and analysis
import pandas as pd

#Create the variable to retract the csv file
# read_csv function of pandas reads the data in CSV format
# from path given and stores in the variable named train
# the data type of train is DataFrame

# 2 escape carracters needed "\\"
train = pd.read_csv("C:\\Users\\samir\\Desktop\\CFSC-2023\\CFSC-2023\\cfsc2023\\examples\\video_behavior_analysis.csv")


#first we split our data into input and output
# y is the output and is stored in "Class" column of dataframe
# X contains the other columns and are features or input
y = train.MotionEnergy
train.drop(['MotionEnergy'], axis=1, inplace=True)
X = train
print(X)
