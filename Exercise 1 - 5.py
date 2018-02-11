import numpy as np
import matplotlib.pyplot as plt 
import scipy 
import math


#Exercise 1
def sec_hour_convert(sec):
    sec_in_min = 60
    min_in_hour = 60

    sec_in_hour = sec_in_min * min_in_hour
    
    hour = sec/sec_in_hour
    #print(hour)
    #print('There are ', hour, 'hour(s) in ', sec, 'seconds')
    return hour 


#Exercise 2

#Importing the data to be used in Exercise 1
data = np.loadtxt(fname='/Users/nikourriola/Desktop/Research/Workshop1/MG1655 Chloramphenicol 10 Feb averages simplified sheet.csv', delimiter=',')


row1 = data[0,:]
sec_hour_convert(row1)


'''
print(len(row1))
#110 elements
print(row1[109,])
#110th element is 86221 

'''


'''
sec_hour_convert(row1[109,])
#Answer:  There are  23.9502777778 hour(s) in  86221.0 seconds
'''


'''
#Exercise 2-1
def counterup(n):
    x_values = np.array([])
    for n in range(0,n,1):
        x_values = np.append(x_values, n)
    return x_values




x_values = counterup(11)

def y(x):
    poly = np.array((x**3)-2*(x**2)+4)
    return poly
#Answer:
print('The inputs are ', x_values, 'The output of x^3-2x^2+4 is ', y(x_values) )
'''

'''
#Exercise 2-2
matrix_3_3 = np.random.rand(3,3)
vector = np.random.rand(3,1)

matrix_3_1 = np.dot(matrix_3_3, vector)

#print('matrix_3_3 = ', matrix_3_3)
#print('vector = ', vector)
#print('matrix (dot) vector = ', matrix_3_1)
#print('column 1 of matrix_3_3 = ', matrix_3_3[:,0])
#print('row 1 of matrix_3_3 = ', matrix_3_3[0,:])

'''

#Exercise 3 & Exercise 4
#example_growth_curve = data[1,:]

#plt.plot(row1, example_growth_curve)
#plt.xlabel('Time (hours)')
#plt.ylabel('Absorbance')

#plt.show()

#A plot of all rows of data in 1 plot with properly labeled legend
for i in range(1,7):
    rows = np.array(data[i,:])
    label_data = ('Row ' + str(i))
    plt.plot(sec_hour_convert(row1),rows, label = label_data)
    
plt.legend(loc = 'best')
plt.xlabel('Time(hours)')
plt.ylabel('Absorbance')
    
plt.show()





'''
#One plot for each row of data
for i in range(1,7):
    rows = np.array(data[i,:])
    plt.plot(row1,rows)
    plt.xlabel('Time(hours)')
    plt.xlabel('Absorbance')
    
    plt.show()

'''

#Exercise 5

from scipy.optimize import curve_fit 

#Variables
#k - carrying capacity
#c - constant offset 
#p_0 - initial population size
#r - growth rate
#t - time data from row1[0,:]
#P(t) = ((k*p_0*e^rt)/(k+p_0((e^rt)-1))) + c

def func(time_data):
    k = 1.4
    c = 0.1
    #p_0 = 0.001
    p_0 = 0.001
    r = 1
    
    y = np.array([])
    
    for t in time_data:
        x = (k*p_0*math.exp(r*t))/(k+(p_0*(math.exp(r*t) - 1)))
        y = np.append(y,x)
    #print(y)
    plt.plot(sec_hour_convert(row1), y)
    
    plt.xlabel('Time(hour(s))')
    plt.ylabel('Absorbance')
    
    plt.show()
    return y 

func(sec_hour_convert(row1))

#curve_fit()






    



    





    







