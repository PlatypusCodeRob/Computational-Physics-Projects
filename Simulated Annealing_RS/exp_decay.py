

import matplotlib.pyplot as plt



def exponential_decay1(n):
    
    
     return 0.995**n*1000

     
range_of_iterations=1000  
factor= range_of_iterations/0.0025    

def exponential_decay2(n):
    
    
     return 0.991**n*1000
 
def exponential_decay3(n):
    
    
     return 0.987**n*1000
 

    
list_x1=[i for i in range(range_of_iterations)]
list_y1=[exponential_decay1(item) for item in list_x1]

list_x2=[i for i in range(range_of_iterations)]
list_y2=[exponential_decay2(item) for item in list_x2]

list_x3=[i for i in range(range_of_iterations)]
list_y3=[exponential_decay3(item) for item in list_x3]


fig = plt.figure(dpi=100)
ax=plt.gca()
ax.set_ylabel("Temperatur $T$")
ax.set_xlabel("Schritt $n$")
plt.plot(list_x1,list_y1,color="red",label="$(\\alpha_1)^n\cdot1000$")
plt.plot(list_x2,list_y2,color="blue",label="$(\\alpha_2)^n\cdot1000$")
plt.plot(list_x3,list_y3,color="orange",label="$(\\alpha_3)^n\cdot1000$")
plt.legend()
plt.show()
#

