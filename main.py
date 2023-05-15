import random as rnd
import matplotlib.pyplot as plt
import math

print("Input number of maximum repetitions")
N_rep = int(input())

#number of point in the circle
p_in = 0
#number of all points
p_all = 0
n = 0
Xvalues = [None]
Yvalues = [None]

XvaluesIN = [None]
YvaluesIN = [None]

XvaluesPI = [None]
YvaluesPI = [None]

for a in range(N_rep):
    n +=1
    for i in range(n):
        #generate random number
        x = rnd.uniform(-10,10)
        y = rnd.uniform(-10,10)

        if(i % 10 == 0):
            #write percentage
            percentage = (i*100)/n
            print(str(percentage) + " %" + "|||| REP NUMBER     " + str(a) + " OF " + str(N_rep))
        #check distance
        d = math.sqrt((x*x)+(y*y))
        if(d < 10):
            #set point
            #IN CIRCLE
            p_in += 1
            p_all += 1
            XvaluesIN.append(x)
            YvaluesIN.append(y)

        else:
            #set point
            #IN SQUARE
            p_all += 1
            Xvalues.append(x)
            Yvalues.append(y)

        
        if(len(XvaluesIN) > 5000000 or len(Xvalues) > 5000000):
            #after some time there might be to much RAM USSAGE
            print("scattering points IN TO PREVENT RAM OVERUSSAGE")
            plt.scatter(XvaluesIN,YvaluesIN,1,c='#ff0000')
            print("scattering points OUT TO PREVENT RAM OVERUSSAGE")
            plt.scatter(Xvalues,Yvalues,1,c='#00ff00')

            Xvalues = [None]
            Yvalues = [None]

            XvaluesIN = [None]
            YvaluesIN = [None]
    
    #generating pi 
    pi = (4 * p_in)/p_all
    YvaluesPI.append(pi)
    XvaluesPI.append(a)


#line below draws a red line at aproximate value of pi
plt.axhline(y = 3.141592653589793238462643383279, color = 'r', linestyle = '-')
plt.plot(XvaluesPI,YvaluesPI)
plt.show()

    

