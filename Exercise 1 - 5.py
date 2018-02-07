import numpy as np
import matplotlib.pyplot as plt 



#Exercise 1
def sec_hour_convert(sec):
    sec_in_min = 60
    min_in_hour = 60

    sec_in_hour = sec_in_min * min_in_hour
    
    hour = sec/sec_in_hour
    
    print('There are ', hour, 'hour(s) in ', sec, 'seconds')
    return hour 


#Exercise 2

#Importing the data to be used in Exercise 1
data = np.loadtxt(fname='/Users/nikourriola/Desktop/Research/Workshop1/MG1655 Chloramphenicol 10 Feb averages simplified sheet.csv', delimiter=',')

#Uncomment these for the main answers to the exercise.
'''
row1 = data[0,:]


print(len(row1))
#110 elements
print(row1[109,])
#110th element is 86221 

time = row1

sec_hour_convert(time[109,])
'''


#Answer:  There are  23.9502777778 hour(s) in  86221.0 seconds

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



