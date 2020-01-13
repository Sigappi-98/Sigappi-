# -*- coding: utf-8 -*-
"""
@script-author:Sigappi
@script-name: KNN
@external-packages used:math

"""
import math
 

train_data = [[1,2,30.6],
              [2,3,56.9],
              [5,4,34.7]]
train_data_1 = train_data.copy()
test_data=[1,6,23.7]

k=2

diff=[] #difference matrix

for i in range(len(train_data)):
    for j in range(len(train_data)-1):
        diff.append((train_data[i][j]-test_data[j])**2) #Squares of the distances

sum_dist=[]

for j in range(0,len(diff),2):
    sum_dist.append(diff[j]+diff[j+1]) #sum of the distances

sqrt=[]

for i in sum_dist:
    sqrt.append(math.sqrt(i))   #square root of the distances
    
for i in range(0,len(train_data)):
    train_data_1[i].append(sqrt[i]) #inserting the distances with their corresponding row


train_data_1.sort(key = lambda train_data_1: train_data_1[1]) #sorting the list in ascending order of distance

avrg=0
for i in range(k):
    avrg=avrg+(train_data_1[i][len(train_data_1)-1])
output=avrg/k      
#output when k=2
output




