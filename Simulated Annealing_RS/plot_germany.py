
"""
Created on Sun Nov 12 16:19:01 2017
@author: Rob
"""

import matplotlib.pyplot as plt

f2=open("Germany.dat","r")
lines2=f2.readlines()
for x in lines2:
     #print(x)
     list=x.split(' ',205)
     #print(    x.split(' ',205)         )
     
list=[list[i] for i in range(len(list)) if list[i]!='' ]

#print(list)

list_lat=[float(list[i].split(',',1)[1].rsplit()[0]) for i in range(len(list))]
list_long=[float(list[i].split(',',1)[0].rsplit()[0]) for i in range(len(list))]

print(list_lat, "Latitudes")
print("\n",list_long, "Longitudes")


fig = plt.figure(figsize=(6,7.5))
plt.plot(list_long,list_lat,"red")



     
     