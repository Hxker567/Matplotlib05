#Simple Program to draw a line Chart
#import matplotlib.pyplot as plt 
#plt.plot([1,2,3],[8,7,4])
#plt.show()

#import matplotlib.pyplot as plt 
#plt.plot([2001,2003,2004,2005],[10000,20000,30000,50000])
#plt.show()

#To plot a line chart for section-wise students strength
#import matplotlib.pyplot as plt
#Eco=[20,30,40,60,80]
#Socio=[10,50,70,85,35]
#Polsc=[100,90,110,65,95]
#Phe=[120,130,140,150,160]
#Eng=[210,220,240,225,235]
#X = ["Economics","Sociology","Poltical science","Physical Education","English"]
#plt.plot(X,Eco, color = "m", label="Eco", linewidth=2, linestyle='--', marker="s", markeredgecolor='b', markersize=7)
#plt.plot(X,Socio, color = "r", label="Socio", linewidth=2, linestyle='-', marker='*', markeredgecolor='b')
#plt.plot(X,Polsc, color = "b", label="Polsc", linewidth=2, linestyle='-.', marker='*', markeredgecolor='b')
#plt.plot(X,Phe, color = "g", label="Phe", linewidth=2, linestyle=':', marker='*', markeredgecolor='b')
#plt.plot(X,Eng, "bh:")
#plt.legend()
#plt.grid()
#plt.show()


#import pandas as pd
#import matplotlib.pyplot as plt
#df =pd.read_csv(r"c:\Users\HP\OneDrive\Desktop\Bugatti Monthly Sales.csv")
#df.plot(kind="barh", x="Day", color= ["red","pink","black"], heigth=0.4, align='edge')                          {*In BAR(H)(Horizontal) (HEIGHT) will be the parameter   $    *In BAR(WIDTH) will be the parameter}  }
#plt.title("Bugatti Monthly Sales FY23")
#print(df)
#plt.show()

#import numpy as np
#import matplotlib.pyplot as plt
#t = np.arange(0.0, 10.0, 1)
#s = [1,2,3,4,5,6,7,8,9,10]

#plt.subplot(2,1,1)     ????????????????????           
#plt.ylabel('Value')
#lt.title('First Chart')
#plt.grid()
#plt.plot(t,s)
#plt.subplots_adjust (hspace=0.4, wspace=0.4)           ?????????????????????
#plt.show()

#PROGRAM TO PLOT A BAR CHART SHOWING THE CHOICE OF FAVOURITE MOVIE GENRE AMONG THE PEOPLE


#import matplotlib.pyplot as plt
#import numpy as np 
#import pandas as pd
#objects = ('Comedy','Action','Romance','Drama','Sci-fi')
#y_pos = np.arange(len(objects))
#types = (4,5,6,1,4)
#df.plot(kind="bar", x='y_pos', y='types', align='center', color='blue')
#plt.xticks(y_pos, objects)
#plt.ylabel('Neha')
#plt.title('Favourite Type of Movie')
#plt.show()
