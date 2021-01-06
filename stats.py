import csv
import matplotlib.pyplot as plt
import statistics
import matplotlib
import pandas as pd


    
    

def mean(data):
    MeanGlucose=statistics.mean([int(i[1]) for i in data])
    StandardDeviation=statistics.stdev([int(i[1]) for i in data])

   
 
  
def timeinrange(data):
    
    low=eval(input("Enter low range"))
    high=eval(input("Enter high range"))
    count_high=0
    count_low=0
    count_total=len(data)
    for i in data:
        if int(i[1])>high:
            count_high += 1
        elif int(i[1])<low:
            count_low += 1
    lowpercent=(count_low/count_total)*100
    highpercent=(count_high/count_total)*100
    targetpercent=((count_total-count_high-count_low)/count_total)*100
    #Plotting graph
    labels = 'High', 'Low', 'Target'
    sizes = [highpercent, lowpercent, targetpercent]
    colors = ['yellow', 'lightcoral', 'lightgreen']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()




def dailytrend(data):
    date=input("Enter date")
    x=[]
    y=[]
    for i in data:
        a=i[0].split()
        if a[0]==date:
            time=a[1]
            x.append(time)
            y.append(int(i[1]))
    #Plotting graph
    plt.scatter(x, y)
    title="Trend",date
    plt.title(title)
    plt.xticks(range(0,288,36))
    plt.xlabel('Time')
    plt.ylabel('Change in blood sugar (mg/dl)')
    plt.show()




        
with open('bg.csv') as csvfile:
    reader= csv.reader(csvfile)
    data=list(reader)

   
