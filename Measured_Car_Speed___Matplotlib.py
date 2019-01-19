import matplotlib.pyplot as plt
import random

random.seed(123)

speed_ny = [random.normalvariate(55, 5) for i in range(10000)] #creates 10,000 normal distributed numbers with mean=55 and std=5
speed_bo = [random.normalvariate(60, 8) for i in range(10000)]
speed_ch = [random.normalvariate(50, 10) for i in range(10000)]

plt.style.use("seaborn") #change style to seaborn
plt.figure(figsize = (12,6)) #change size of graph

plt.hist(speed_ny, bins = 100, label = "New York Data", alpha = 0.5, color = "red") #Histrogramm of NY Data
plt.hist(speed_bo, bins = 100, label = "Boston Data", alpha = 0.5, color = "blue") #Histogramm of Boston Data
plt.hist(speed_ch, bins = 100, label = "Chicago Data", alpha = 0.5, color = "green") #Histogramm of Chicago Data

plt.title("Measured Car Speed (Speed Limit 50 mph)", fontsize = 15) #set title
plt.xlabel("Speed") #label x-axis
plt.ylabel("occurences") #label y-axis

plt.vlines(sum(speed_ny)/len(speed_ny),0,400, color = "red", linestyle = "--", label = "Mean New York") #vertical line at NY mean
plt.vlines(sum(speed_bo)/len(speed_bo),0,400, color = "blue", linestyle = "-.", label = "Mean Boston") #vertical line at Boston mean 
plt.vlines(sum(speed_ch)/len(speed_ch),0,400, color = "green", linestyle = "-.", label = "Mean Chicago") #vertical line at Boston mean 

plt.axis((30,90,0,400)) #set range of axis
plt.xticks(range(30,91,5)) #set ticks of x-axis
plt.yticks(range(0,401,50))  #set ticks of y-axis
plt.grid(True) #enable/disable grid
plt.legend(loc = "center right", fontsize = 13) #include legend
plt.show()