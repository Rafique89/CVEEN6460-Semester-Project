#Bismillahirehman_Nirraheeem
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ggplot import *

x = (float(raw_input("Number of people in the building: "))) # Enter the Number of People in the buildings
print("\n")
print("\n")
x1 = float(raw_input("press 1 for using default values. Press 2 to use different values: "))
#Indoor_Usage
a="Toilets"
b="Shower"
c="Washing_Machine"
d="Dishwasher"
e="Faucets"
f="Baths"


#Default_Use_Rate

a1=float (4.0)  #flushes per person per day
b1=float (4.8)  #minutes per person per day
c1=float (0.30)  #loads per person per day
d1=float (0.17)  #loads per person per day
e1=float (8.5) #gpd
f1=float (0.14) #baths per person per day

#Default_Flow_Rate

a2=float(1.6) #gallons
b2=float(2.5) #gallons
c2=float(40.2)  #gal_per_load
d2=float(8.5) #gallons
e2=float(8.5) #gpd
f2 = float(50.1) #gal_per_bath

raw_data2={ 'Hour':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24], 
            'Toilet_multiplier':[0.1,0.1,0.1,0.1,0.1,1.3,1.2,1.1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.8], 
            'Shower_multiplier': [0.1,0,0,0,0,1.5,1.4,1.3,0.9,0.6,0.6,1.2,1.2,1.2,0.8,0.8,0.7,0.9,0.8,0.7,0.6,0.6,0.6,0.6], 
            'Washing_Machine_multiplier':[0,0,0,0,0,0,0,0,0,0,0,0,1.2,1.2,1.2,1.2,1.2,1.2,1.4,1.4,1.2,1.2,1.2,1.2], 
            'Dishwasher_multiplier':[0,0,0,0,0,0,1.2,1.2,1.2,1.2,0.9,1.2,1.2,1.2,1.6,0.9,0.9,0.9,0.9,0.9,0.9,0.6,0.6,0.6], 
            'Faucet_multiplier':[0,0,0,0,0,0,1.2,1.2,1.2,1.2,0.9,1.2,1.2,1.2,1.6,0.9,0.9,0.9,0.9,0.9,0.9,0.6,0.6,0.6], 
            'Bath_multiplier':[0.1,0,0,0,0,1.5,1.4,1.3,0.9,0.6,0.6,1.2,1.2,1.2,0.8,0.8,0.7,0.9,0.8,0.7,0.6,0.6,0.6,0.6]}

raw_data3={ 'Month':[1,2,3,4,5,6,7,8,9,10,11,12], 
            'Toilet_Month':[1.1,1.1,1.1,1.1,0.8,0.3,0.3,0.9,1.1,1.1,1.1,1.1], 
            'Shower_Month':[1.1,1.1,1.1,1.1,0.8,0.3,0.3,0.9,1.1,1.1,1.1,1.1], 
            'Washing_Machine_Month':[1.1,1.1,1.1,1.1,0.8,0.3,0.3,0.9,1.1,1.1,1.1,1.1], 
            'Dishwasher_Month':[1.1,1.1,1.1,1.1,0.8,0.3,0.3,0.9,1.1,1.1,1.1,1.1], 
            'Faucet_Month':[1.1,1.1,1.1,1.1,0.8,0.3,0.3,0.9,1.1,1.1,1.1,1.1], 
            'Bath_Month':[1.1,1.1,1.1,1.1,0.8,0.3,0.3,0.9,1.1,1.1,1.1,1.1]}


if x1==1:
    a3 = float (x * a1 * a2) #Total Toilet Usage
    print("Total Toilet Usage in gpd" + " " + str(float(a3)))
    print("\n")
    print("\n")    
    b3 = float (x * b1 * b2) #Total Shower Usage
    print("Total Shower Usage in gpd" + " " + str(float(b3)))    
    print("\n")
    print("\n")        
    c3 = float (x * c1 * c2) #Total Washing Machine Usage in gpd
    print("Total Washing Machine Usage in gpd" + " " + str(float(c3))) 
    print("\n")
    print("\n")    
    d3 = float (x * d1 * d2) #Total Dishwasher Usage in gpd
    print("Total Dishwasher Usage in gpd" + " " + str(float(d3)))            
    print("\n")
    print("\n")
    e3 = float (e2) #Total Faucets Usage in gpd
    print("Total Faucets Usage in gpd" + " " + str(float(e3)))
    print("\n")
    print("\n")    
    f3 = float (x * f1 * f2) #Total bath Usage in gpd
    print("Total bath Usage in gpd" + " " + str(float(f3)))    
    print("\n")
    print("\n")    
    print("Total INDOOR usage is" + " " + str(float(a3+b3+c3+d3+e3+f3)) + " " + "gpd")
    print("\n")
    print("\n")    

    #GRAPHS
    a3_1= round((a3 / (a3+b3+c3+d3+e3+f3)) * 100,2)
    b3_1 = round ((b3 / (a3+b3+c3+d3+e3+f3)) * 100,2)
    d3_1 = round((d3/ (a3+b3+c3+d3+e3+f3)) * 100,2)
    c3_1 = round((c3 / (a3+b3+c3+d3+e3+f3)) * 100,2)
    e3_1 = round((e3 / (a3+b3+c3+d3+e3+f3)) * 100,2)
    f3_1 = round((f3 / (a3+b3+c3+d3+e3+f3)) * 100,2)

    print(a3_1)
    print(b3_1)
    print(c3_1)
    print(d3_1)
    print(e3_1)
    print(f3_1)
    print(a3_1 + b3_1 + c3_1 + d3_1 + e3_1 + f3_1)

    ##pie chart

    raw_data1={ 'Category_name': ['Toilet' , 'Shower' , 'Washing_Machine' , 'Dishwasher' , 'Faucet' , 'Bath'],              
                'Category_Usage_gpd':[a3, b3, c3, d3, e3, f3],
                'Category_percent': [a3_1 , b3_1 , c3_1 , d3_1 , e3_1 , f3_1]}
    df=pd.DataFrame(raw_data1, columns=['Category_name','Category_Usage_gpd','Category_percent'])
    df

    df2=pd.DataFrame(raw_data2, columns=['Hour','Toilet_multiplier','Shower_multiplier','Washing_Machine_multiplier','Dishwasher_multiplier','Faucet_multiplier','Bath_multiplier'])
    df2

    df2['total']=(df2['Toilet_multiplier']*a3) + (df2['Shower_multiplier']*b3)+(df2['Washing_Machine_multiplier']*c3)+ (df2['Dishwasher_multiplier']*d3)+(df2['Faucet_multiplier']*e3)+ (df2['Bath_multiplier']*f3)


    df2['Toilet']=df2['Toilet_multiplier']*a3*100/df2['total']
    df2['Shower']=df2['Shower_multiplier']*b3*100/df2['total']
    df2['Washing_Machine']=df2['Washing_Machine_multiplier']*c3*100/df2['total']
    df2['Dishwasher']=df2['Dishwasher_multiplier']*d3*100/df2['total']
    df2['Faucet']=df2['Faucet_multiplier']*e3*100/df2['total']
    df2['Bath']=df2['Bath_multiplier']*f3*100/df2['total']





    df3=pd.DataFrame(raw_data3, columns=['Month','Toilet_Month','Shower_Month','Washing_Machine_Month','Dishwasher_Month','Faucet_Month','Bath_Month'])
    df3

    df3['total']=(df3['Toilet_Month']*a3) + (df3['Shower_Month']*b3)+(df3['Washing_Machine_Month']*c3)+ (df3['Dishwasher_Month']*d3)+(df3['Faucet_Month']*e3)+ (df3['Bath_Month']*f3)




    df3['Toilet']=df3['Toilet_Month']*a3
    df3['Shower']=df3['Shower_Month']*b3
    df3['Washing_Machine']=df3['Washing_Machine_Month']*c3
    df3['Dishwasher']=df3['Dishwasher_Month']*d3
    df3['Faucet']=df3['Faucet_Month']*e3
    df3['Bath']=df3['Bath_Month']*f3



    plt.pie(
        # using data Category_per(gpd)cent
        df['Category_percent'],
        # with the labels being Category_name
        labels=df['Category_name'],
        # with one slide exploded out
        explode=(0, 0, 0, 0, 0.15,0),
        # with the start angle at 90%
        startangle=90,
        # with the percent listed as a fraction
        autopct='%1.1f%%',
    )
    plt.title('Percentage of daily water usage in different Categories')
    plt.show()

    bargraph = ggplot(df, aes(x="Category_name", weight="Category_Usage_gpd")) + geom_bar() + \
        labs("Category_name","Category_Usage_gpd") + \
        ggtitle("Total daily water usage in different Categories")

    bargraph.show()

    df2[['Toilet_multiplier','Shower_multiplier','Washing_Machine_multiplier','Dishwasher_multiplier','Faucet_multiplier','Bath_multiplier']].plot()
    plt.title('Hourly variation of demand multiplier in different Categories')
    plt.show()


    df2[['Toilet','Shower','Washing_Machine','Dishwasher','Faucet','Bath']].plot()
    plt.title('Hourly variation of water usage in different Categories')
    plt.show()

    df3[['Toilet','Shower','Washing_Machine','Dishwasher','Faucet','Bath']].plot()
    plt.title('Monthly variation of water usage in different Categories')
    plt.show()                           

    df3.plot('Month', 'total',title='Monthly variation of total water usage', color='r')    

    plt.show()                               


else:
    print(" lo g")
    print("\n")
    print("\n")   
    a4 = float(raw_input("Enter flushes per person per day ")) # Frequency of Flushes per day
    a5 = float(raw_input("Enter gallons flushed per flush ")) # Gallons Flushed per Flush
    print("\n")
    print("\n")    
    b4 = float(raw_input("Enter avergae shower use in minutes ")) # Shower Usage_ Minutes Per day
    b5 = float(raw_input("Enter Enter Flow rate from Shower per minute ")) # Flow rate per minute
    print("\n")
    print("\n")    
    c4 = float(raw_input("Enter loads per person per day ")) # Loads per person per day
    c5 = float(raw_input("Enter gallons per load per day ")) # Gallons per load per day
    print("\n")
    print("\n")    
    d4 = float(raw_input("Enter loads per person per day")) # Loads per person per day
    d5 = float(raw_input("Enter flushes per person per day ")) # Gallons per load per day
    print("\n")
    print("\n")    
    e4 = float(raw_input("Enter Faucet usage in gpd per person per day ")) # Faucet usage
    print("\n")
    print("\n")    
    f4 = float(raw_input("Enter number of baths per person per day ")) # Number of Baths taken per person per day
    f5 = float(raw_input("Enter number of gallons used per person per day ")) # Gallons used during baths

    print("\n")
    print("\n")    
    a6 = float (x * a4 * a5) #Total Toilet Usage
    print("Total Toilet Usage in gpd" + " " + str(float(a6)))
    print("\n")
    print("\n")       
    b6 = float (x * b4 * b5) #Total Shower Usage in gpd
    print("Total Shower Usage in gpd" + " " + str(float(b6)))    
    print("\n")
    print("\n")            
    c6 = float (x * c4 * c5) #Total Washing Machine Usage in gpd
    print("Total Washing Machine Usage in gpd" + " " + str(float(c6))) 
    print("\n")
    print("\n")        
    d6 = float (x * d4 * d5) #Total Dishwasher Usage in gpd
    print("Total Dishwasher Usage in gpd" + " " + str(float(d6)))            
    print("\n")
    print("\n")    
    e6 = float (e4) #Total Faucets Usage in gpd
    print("Total Faucets Usage in gpd" + " " + str(float(e6)))
    print("\n")
    print("\n")        
    f6 = float (x * f4 * f5) #Total bath Usage in gpd
    print("Total bath Usage in gpd" + " " + str(float(f6)))     
    print("\n")
    print("\n")    
    print("Total INDOOR usage is" + " " + str(float(a6+b6+c6+d6+e6+f6)) + " " + "gpd")


    a6_1= round((a6 / (a6+b6+c6+d6+e6+f6)) * 100,2)
    b6_1 = round((b6 / (a6+b6+c6+d6+e6+f6)) * 100,2)
    d6_1 = round((d6/ (a6+b6+c6+d6+e6+f6)) * 100,2)
    c6_1 = round((c6 / (a6+b6+c6+d6+e6+f6)) * 100,2)
    e6_1 = round((e6 / (a6+b6+c6+d6+e6+f6)) * 100,2)
    f6_1 = round((f6 / (a6+b6+c6+d6+e6+f6)) * 100,2)
    print(a6_1)
    print(b6_1)
    print(c6_1)
    print(d6_1)
    print(e6_1)
    print(f6_1)
    print(a6_1 + b6_1 + c6_1 + d6_1 + e6_1 + f6_1)

    raw_data1={ 'Category_name': ['Toilet' , 'Shower' , 'Washing_Machine' , 'Dishwasher' , 'Faucet' , 'Bath'],              
                'Category_Usage_gpd':[a6, b6, c6, d6, e6, f6],
                'Category_percent': [a6_1 , b6_1 , c6_1 , d6_1 , e6_1 , f6_1]}
    df=pd.DataFrame(raw_data1, columns=['Category_name','Category_Usage_gpd','Category_percent'])
    df

    df2=pd.DataFrame(raw_data2, columns=['Hour','Toilet_multiplier','Shower_multiplier','Washing_Machine_multiplier','Dishwasher_multiplier','Faucet_multiplier','Bath_multiplier'])
    df2

    df2['total']=(df2['Toilet_multiplier']*a6) + (df2['Shower_multiplier']*b6)+(df2['Washing_Machine_multiplier']*c6)+ (df2['Dishwasher_multiplier']*d6)+(df2['Faucet_multiplier']*e6)+ (df2['Bath_multiplier']*f6)


    df2['Toilet']=df2['Toilet_multiplier']*a6*100/df2['total']
    df2['Shower']=df2['Shower_multiplier']*b6*100/df2['total']
    df2['Washing_Machine']=df2['Washing_Machine_multiplier']*c6*100/df2['total']
    df2['Dishwasher']=df2['Dishwasher_multiplier']*d6*100/df2['total']
    df2['Faucet']=df2['Faucet_multiplier']*e6*100/df2['total']
    df2['Bath']=df2['Bath_multiplier']*f6*100/df2['total']





    df3=pd.DataFrame(raw_data3, columns=['Month','Toilet_Month','Shower_Month','Washing_Machine_Month','Dishwasher_Month','Faucet_Month','Bath_Month'])
    df3

    df3['total']=(df3['Toilet_Month']*a6) + (df3['Shower_Month']*b6)+(df3['Washing_Machine_Month']*c6)+ (df3['Dishwasher_Month']*d6)+(df3['Faucet_Month']*e6)+ (df3['Bath_Month']*f6)




    df3['Toilet']=df3['Toilet_Month']*a6
    df3['Shower']=df3['Shower_Month']*b6
    df3['Washing_Machine']=df3['Washing_Machine_Month']*c6
    df3['Dishwasher']=df3['Dishwasher_Month']*d6
    df3['Faucet']=df3['Faucet_Month']*e6
    df3['Bath']=df3['Bath_Month']*f6



    plt.pie(
        # using data Category_per(gpd)cent
        df['Category_percent'],
        # with the labels being Category_name
        labels=df['Category_name'],
        # with one slide exploded out
        explode=(0, 0, 0, 0, 0.15,0),
        # with the start angle at 90%
        startangle=90,
        # with the percent listed as a fraction
        autopct='%1.1f%%',
    )
    plt.title('Percentage of daily water usage in different Categories')
    plt.show()

    bargraph = ggplot(df, aes(x="Category_name", weight="Category_Usage_gpd")) + geom_bar() + \
        labs("Category_name","Category_Usage_gpd") + \
        ggtitle("Total daily water usage in different Categories")

    bargraph.show()

    df2[['Toilet_multiplier','Shower_multiplier','Washing_Machine_multiplier','Dishwasher_multiplier','Faucet_multiplier','Bath_multiplier']].plot()
    plt.title('Hourly variation of demand multiplier in different Categories')
    plt.show()


    df2[['Toilet','Shower','Washing_Machine','Dishwasher','Faucet','Bath']].plot()
    plt.title('Hourly variation of water usage in different Categories')
    plt.show()

    df3[['Toilet','Shower','Washing_Machine','Dishwasher','Faucet','Bath']].plot()
    plt.title('Monthly variation of water usage in different Categories')
    plt.show()                           

    df3.plot('Month', 'total',title='Monthly variation of total water usage', color='r')

    plt.show() 