#Bismillahirehman_Nirraheeem

x = float(raw_input("Number of people in the building: ")) # Enter the Number of People in the buildings
print "\n"
print "\n"
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

if x1==1:
    a3 = float (x * a1 * a2) #Total Toilet Usage
    print "Total Toilet Usage in gpd" + " " + str(float(a3))
    print "\n"
    print "\n"    
    b3 = float (x * b1 * b2) #Total Shower Usage
    print "Total Shower Usage in gpd" + " " + str(float(b3))    
    print "\n"
    print "\n"        
    c3 = float (x * c1 * c2) #Total Washing Machine Usage in gpd
    print "Total Washing Machine Usage in gpd" + " " + str(float(c3)) 
    print "\n"
    print "\n"    
    d3 = float (x * d1 * d2) #Total Dishwasher Usage in gpd
    print "Total Dishwasher Usage in gpd" + " " + str(float(d3))            
    print "\n"
    print "\n"
    e3 = float (e2) #Total Faucets Usage in gpd
    print "Total Faucets Usage in gpd" + " " + str(float(e3))
    print "\n"
    print "\n"    
    f3 = float (x * f1 * f2) #Total bath Usage in gpd
    print "Total bath Usage in gpd" + " " + str(float(f3))    
    print "\n"
    print "\n"    
    print "Total INDOOR usage is" + " " + str(float(a3+b3+c3+d3+e3+f3)) + " " + "gpd"
    print "\n"
    print "\n"    
    
    #GRAPHS
    a3_1= round((a3 / (a3+b3+c3+d3+e3+f3)) * 100,2)
    b3_1 = round ((b3 / (a3+b3+c3+d3+e3+f3)) * 100,2)
    d3_1 = round((d3/ (a3+b3+c3+d3+e3+f3)) * 100,2)
    c3_1 = round((c3 / (a3+b3+c3+d3+e3+f3)) * 100,2)
    e3_1 = round((e3 / (a3+b3+c3+d3+e3+f3)) * 100,2)
    f3_1 = round((f3 / (a3+b3+c3+d3+e3+f3)) * 100,2)
    
    print a3_1
    print b3_1
    print c3_1
    print d3_1
    print e3_1
    print f3_1
    print (a3_1 + b3_1 + c3_1 + d3_1 + e3_1 + f3_1)
    
    
    
else:
    print " lo g"
    print "\n"
    print "\n"    
    a4 = float(raw_input("Enter flushes per person per day ")) # Frequency of Flushes per day
    a5 = float(raw_input("Enter gallons flushed per flush ")) # Gallons Flushed per Flush
    print "\n"
    print "\n"    
    b4 = float(raw_input("Enter avergae shower use in minutes ")) # Shower Usage_ Minutes Per day
    b5 = float(raw_input("Enter Enter Flow rate from Shower per minute ")) # Flow rate per minute
    print "\n"
    print "\n"    
    c4 = float(raw_input("Enter loads per person per day ")) # Loads per person per day
    c5 = float(raw_input("Enter gallons per load per day ")) # Gallons per load per day
    print "\n"
    print "\n"    
    d4 = float(raw_input("Enter loads per person per day")) # Loads per person per day
    d5 = float(raw_input("Enter flushes per person per day ")) # Gallons per load per day
    print "\n"
    print "\n"    
    e4 = float(raw_input("Enter Faucet usage in gpd per person per day ")) # Faucet usage
    print "\n"
    print "\n"    
    f4 = float(raw_input("Enter number of baths per person per day ")) # Number of Baths taken per person per day
    f5 = float(raw_input("Enter number of gallons used per person per day ")) # Gallons used during baths
    
    print "\n"
    print "\n"    
    a6 = float (x * a4 * a5) #Total Toilet Usage
    print "Total Toilet Usage in gpd" + " " + str(float(a6))
    print "\n"
    print "\n"        
    b6 = float (x * b4 * b5) #Total Shower Usage in gpd
    print "Total Shower Usage in gpd" + " " + str(float(b6))    
    print "\n"
    print "\n"            
    c6 = float (x * c4 * c5) #Total Washing Machine Usage in gpd
    print "Total Washing Machine Usage in gpd" + " " + str(float(c6)) 
    print "\n"
    print "\n"        
    d6 = float (x * d4 * d5) #Total Dishwasher Usage in gpd
    print "Total Dishwasher Usage in gpd" + " " + str(float(d6))            
    print "\n"
    print "\n"    
    e6 = float (e4) #Total Faucets Usage in gpd
    print "Total Faucets Usage in gpd" + " " + str(float(e6))
    print "\n"
    print "\n"        
    f6 = float (x * f4 * f5) #Total bath Usage in gpd
    print "Total bath Usage in gpd" + " " + str(float(f6))     
    print "\n"
    print "\n"    
    print "Total INDOOR usage is" + " " + str(float(a6+b6+c6+d6+e6+f6)) + " " + "gpd"
    
    #GRAPHS
    a6_1= round((a6 / (a6+b6+c6+d6+e6+f6)) * 100,2)
    b6_1 = round((b6 / (a6+b6+c6+d6+e6+f6)) * 100,2)
    d6_1 = round((d6/ (a6+b6+c6+d6+e6+f6)) * 100,2)
    c6_1 = round((c6 / (a6+b6+c6+d6+e6+f6)) * 100,2)
    e6_1 = round((e6 / (a6+b6+c6+d6+e6+f6)) * 100,2)
    f6_1 = round((f6 / (a6+b6+c6+d6+e6+f6)) * 100,2)
    
    print a6_1
    print b6_1
    print c6_1
    print d6_1
    print e6_1
    print f6_1
    print (a6_1 + b6_1 + c6_1 + d6_1 + e6_1 + f6_1)    