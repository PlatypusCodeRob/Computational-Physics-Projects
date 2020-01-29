import matplotlib.pyplot as plt
import random
import time
import numpy as np
import distances_and_other_functions as own
import copy
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

from math import exp
from tqdm import tqdm

plt.tight_layout()

"""Get Germany Layout"""
f2=open("Germany.dat","r")
lines2=f2.readlines()
for x in lines2:
     list=x.split(' ',205)
     
list=[list[i] for i in range(len(list)) if list[i]!='' ]              #cut out empty '' elements
list.append(list[0])
list_lat=[float(list[i].split(',',1)[1].rsplit()[0]) for i in range(len(list))]
list_long=[float(list[i].split(',',1)[0].rsplit()[0]) for i in range(len(list))]
"""Lists of latitudes and longitudes for Germany Layout """


"""optimal_path_40 müsste so ziemlich der kürzeste Pfad durch diese 39 Städte sein (siehe Bild).
Rostock als Start und Ende des Pfades wird noch angefügt -> 40 Städte wie in Aufgabe.
Ziel war, diesen (oder was in der Größenordnung) wiederzufinden nach Mischen der Liste"""

def calculate_path_length_matrix(list_towns):

     list_help=[]
     dist=0
     
     for i in range(len(list_towns)):
          index_x=list_of_town_names.index(list_towns[i][0])
          list_help.append(index_x)
      
     for i in range(len(list_help)-1):
          dist += array_of_distances[list_help[i+1]][list_help[i]]
          
     return dist
 
def exponential_decay(n):
    #0.987
     return 0.987**n*1000      
     #return 0.9995**n*825   
 



def decision(probability):
    
    return random.random() < probability  # returns True/False

optimal_path_40=[
              ('Lübeck', 53.86944444444445, 10.686111111111112),
              ('Kiel', 54.32611111111112, 10.145),
              ('Flensburg', 54.78472222222222, 9.436666666666667),
              ('Wilhelmshaven', 53.51888888888889, 8.122222222222224),
              ('Oldenburg', 53.13916666666667, 8.2175),
              ('Osnabrück', 52.278888888888886, 8.045555555555556),
              ('Dortmund', 51.51611111111111, 7.468333333333334),
              ('Bochum', 51.48361111111111, 7.221388888888889),
              ('Essen', 51.456944444444446, 7.010555555555555),
              ('Duisburg', 51.43805555555555, 6.7619444444444445),
              ('Jülich', 50.92305555555555, 6.359444444444444),
              ('Aachen', 50.77611111111111, 6.084444444444444),
              ('Trier', 49.757222222222225, 6.643888888888888),
              ('Saarbrücken', 49.23222222222223, 6.992222222222222),
              ('Kaiserslautern', 49.44444444444444, 7.772222222222222),
              ('Worms', 49.63138888888889, 8.362499999999999),
              ('Ludwigshafen', 49.480555555555554, 8.444444444444445),
              ('Landau/Pfalz', 49.197222222222216, 8.116666666666667),
              ('Karlsruhe', 49.00555555555555, 8.405555555555557),
              ('Pforzheim', 48.89333333333333, 8.704166666666666),
              ('Freiburg', 47.99666666666667, 7.853055555555555),
              ('Konstanz', 47.65972222222222, 9.175833333333333),
              ('Reutlingen', 48.492222222222225, 9.214444444444444),
              ('Ulm', 48.39944444444444, 9.993055555555555),
              ('Augsburg', 48.37222222222222, 10.9),
              ('Eichstätt', 48.891666666666666, 11.191666666666666),
              ('Regensburg', 49.019444444444446, 12.1),
              ('Passau', 48.575, 13.469444444444445),
              ('Bayreuth', 49.94444444444444, 11.577777777777778),
              ('Ilmenau', 50.69694444444444, 10.91638888888889),
              ('Erfurt', 50.977222222222224, 11.025),
              ('Weimar', 50.981388888888894, 11.333333333333334),
              ('Jena', 50.930277777777775, 11.589166666666667),
              ('Gera', 50.882222222222225, 12.082777777777778),
              ('Zwickau', 50.719166666666666, 12.213055555555554),
              ('Chemnitz', 50.836111111111116, 12.922222222222222),
              ('Dresden', 51.05416666666667, 13.738888888888889),
              ('Cottbus', 51.759166666666665, 14.335277777777778),
              ('Berlin', 52.52222222222222, 13.2975)] # 2783.6 km 

optimal_path_20=[
              ('Lübeck', 53.86944444444445, 10.686111111111112),
              ('Kiel', 54.32611111111112, 10.145),
              ('Flensburg', 54.78472222222222, 9.436666666666667),
              ('Wilhelmshaven', 53.51888888888889, 8.122222222222224),
              ('Oldenburg', 53.13916666666667, 8.2175),
              ('Osnabrück', 52.278888888888886, 8.045555555555556),
              ('Dortmund', 51.51611111111111, 7.468333333333334),
              ('Bochum', 51.48361111111111, 7.221388888888889),
              ('Essen', 51.456944444444446, 7.010555555555555),
              ('Duisburg', 51.43805555555555, 6.7619444444444445),
              ('Jülich', 50.92305555555555, 6.359444444444444),
              ('Aachen', 50.77611111111111, 6.084444444444444),
              ('Trier', 49.757222222222225, 6.643888888888888),
              ('Saarbrücken', 49.23222222222223, 6.992222222222222),
              ('Kaiserslautern', 49.44444444444444, 7.772222222222222),
              ('Worms', 49.63138888888889, 8.362499999999999),
              ('Ludwigshafen', 49.480555555555554, 8.444444444444445),
              ('Landau/Pfalz', 49.197222222222216, 8.116666666666667),
              ('Karlsruhe', 49.00555555555555, 8.405555555555557),
              ('Pforzheim', 48.89333333333333, 8.704166666666666)]#,   1736.8 km

dpi=250   # für plots
alpha=0.987 # für plots

t=0
bestes = 0
alle_zeiten=[]



laengen = []
zeiten = []

while t<=50:     #der gesamte Prozess von pfad initialisieren bis hin zur ausgabe eines 
                    #optimierten ergebnisses wird 50 mal wiederholt um die mittlere laufzeit zu messen
                    
    print("\nt=",t)
    """Measure total runtime"""
    start_time = time.time()
               
    """Mischen und Anfang und Ende vom Pfad anfügen"""
    towns=random.sample(optimal_path_40,39)#len(optimal_path_20))   #40 aus der Liste 
    towns.insert(0,('Rostock', 54.08972222222222, 12.13361111111111))
    towns.append(('Rostock', 54.08972222222222, 12.13361111111111))
    
    
    
    
        
    """Matrix mit Distanzen basteln"""
    array_of_distances = np.empty((len(towns), len(towns)))
    for i, item in enumerate(towns):
         for j, item2 in enumerate(towns):
    
              if i==j:
                   array_of_distances[i][j]=0
              else:
                   array_of_distances[i][j]=own.distance_in_km_between_points(item[1],item[2],item2[1],item2[2]) 
     
    
    
    
    
    length_start=own.calculate_path_length(towns)
    print(length_start, "Kilometer Pfadlänge Anfang")
    if t==0:
        bestes = length_start
    
    # alle pfadlängen werden aufgezeichnet um die Entwicklung darstellen zu können
    all_lengths=[]
    all_lengths.append(length_start)                     
    
        
    probs=[]         
    list_of_town_names=[item[0] for item in towns] 
    
    
    
    
    
    
    
    
    
    
    
    # hier startet der wesentliche algorithmus    
    x=0
    range_of_iterations=1000
    
    save = copy.copy(towns)
    probs=[]
    for x in tqdm(range(1,range_of_iterations+1)):
        #print("\nx=",x)
        Temperature             = exponential_decay(x)
        subiteration            = 0
        
        current_best=all_lengths[-1]
        
        while subiteration <=len(towns)**2: #:
            
            """Iterating path"""
            
            
            saved_towns = copy.copy(save) #WICHTIG!
            
            
            new_towns   = own.switch_two_elements(save)
            
            #Oder die andere methode der Iteration:
            #new_towns   = own.revert_one_path(save)
            
            new_length = calculate_path_length_matrix(new_towns)
            DeltaL      = abs(new_length-current_best)
            Probability = 1*exp(1*(-1*DeltaL/(1*Temperature)))
            
            #print("Delta L:", DeltaL, "--", "Temp:",Temperature, "---> Probability of keeping longer path:",Probability)
            probs.append(Probability)
    
            if new_length>=current_best: 
                #path got longer
    
                if decision(Probability):
                    
                    # "keep longer path anyway!"
                    all_lengths.append(new_length)
                    save            = copy.copy(new_towns)
                    current_best    = new_length
                    #gespeicherter save vom kürzeren wird Überschrieben
                    
                else:
                    #print("keep shorter path from before")
                    #print("path still at:",current_best)
                    all_lengths.append(current_best)
                    save = copy.copy(saved_towns)
                    #zurück zum gespeicherten
            else:
                
                #print("path got shorter after iterating")
                all_lengths.append(new_length)    
                current_best    = new_length
                save            = copy.copy(new_towns)
                #gespeichertes wird Überschrieben
                
            subiteration += 1
            # das hier ist die Ebene wo die Temperatur momentan festgehalten wird und (Anzahl_Städte)^2 Versuche 
            # ausgeführt werden den Pfad zu optimieren
            continue
            
        # das hier ist die Schrittebene auf der die Temperatur geändert wird
        continue
        """Prozess von vorn mit geringerer Temperatur"""
        
    # """Algorithmus fertig, ab hier kommen plots und sowas"""    
    
    t_delta = float("{0:.2f}".format((time.time() - start_time)))
    laengen.append(float("{0:.1f}".format(all_lengths[-1])))
    zeiten.append(t_delta)
    
    print("\tLänge:",all_lengths[-1])
    if laengen[-1]<=bestes:
        "Plot all path lenghts recorded"
        fig2=plt.figure(figsize=(8,3),dpi=dpi)
        plt.grid()
        plt.gcf().subplots_adjust(bottom=0.15)
        plt.plot([i for i in range(len(all_lengths))],all_lengths)
        ax=plt.gca()
        props = dict(boxstyle='round',facecolor="white", alpha=1)  
        textstr = r"$\alpha$ = "+str(alpha)  
        ax.text(0.8, 0.85, textstr, transform=ax.transAxes, fontsize=14,
            verticalalignment='bottom', bbox=props)
        ax.set_ylabel("Pfadlänge $L$ [km]")
        ax.set_xlabel("Schritt $n$")
        fig2.savefig("bild2.png")
        #plt.show()
#    
#    
#    print("Lenght at end:",float("{0:.1f}".format(all_lengths[-1])))

#    
#    """Plot Temp"""
#    list_x=[i for i in range(range_of_iterations)]
#    list_y=[exponential_decay(item) for item in list_x]
#    ax=plt.gca()
#    ax.set_ylabel("Temperature $T$")
#    ax.set_xlabel("Iteration $i$")
#    plt.plot(list_x,list_y)
#    plt.show()   

    
    
        bestes = laengen[-1]
        names2=[save[i][0] for i in range(len(save)-1)]
        lats2=[save[i][1] for i in range(len(save))]
        longs2=[save[i][2] for i in range(len(save))]
        
        
        """Plot Germany Outline"""
        fig = plt.figure(figsize=(8,11.44),dpi=dpi)
        plt.plot(longs2,lats2,alpha=0.5)
        plt.scatter(longs2,lats2)
        plt.plot(list_long,list_lat,"red",alpha=0.8)                
        
        ax=plt.gca()
        ax.set_ylim(min(lats2)-0.5,max(lats2)+0.5)
        ax.set_xlim(min(longs2)-0.5,max(longs2)+0.5)
        plt.grid()
        ax.arrow(save[0][2], save[0][1], (save[1][2]-save[0][2])*0.92, (save[1][1]-save[0][1])*0.92, head_width=0.12, head_length=0.1, fc='r', ec='r')
        for label,x,y in zip(names2,longs2,lats2):
             ax.annotate(label,xy=(x, y),xytext=(0, 5),textcoords='offset points',fontsize=10)
             
        props = dict(boxstyle='round',facecolor="white", alpha=1)    
        textstr = "Pfadlänge: "+str(float("{0:.1f}".format(calculate_path_length_matrix(save))))+"km"   
        ax.text(0.6, 0.05, textstr, transform=ax.transAxes, fontsize=14,
                verticalalignment='bottom', bbox=props)
        ax.set_ylabel("Breitengrad in deg")
        ax.set_xlabel("Längengrad in deg")
        fig.savefig("bild1.png")
        print("dargestellter Pfad:",save)
        print("Länge:",all_lengths[-1])
        #plt.show()
        #print(3*"\n","--- %s seconds ---" % (t_delta))   
    
    t+=1 
    """Und alles nochmal von vorn"""
    

def func(liste):
    fig = plt.figure(dpi=dpi)
    ax=sns.distplot(liste, kde=True, hist=False,kde_kws={"color": "b", "lw": 2, "label": "KDE"})
    ax2 =ax.twinx()
    
    ax2=sns.distplot(liste, kde=False, hist=True,hist_kws={ "linewidth": 1,
                             "alpha": 0.6, "color": "g","rwidth":0.95,'edgecolor':'black',})
    textstr = r"$\alpha$ = "+str(alpha)  
    ax.text(0.77, 0.8, textstr, transform=ax.transAxes, fontsize=14,
                verticalalignment='bottom', bbox=props)
    ax.set(xlabel='Pfadlänge $P$ [km]', ylabel='KDE')
    ax2.set(xlabel='Pfadlänge $P$ [km]', ylabel='Anzahl der Werte')
    sns.despine(ax=ax, right=True, left=False)
    sns.despine(ax=ax2, left=True, right=False)
    fig.savefig("prob_of_lengths.png")
    plt.show()
    
func(laengen)

print(zeiten)



