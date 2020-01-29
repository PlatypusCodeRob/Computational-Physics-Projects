
from math import pi,sqrt,asin,sin,cos,exp
import random





def degrees_to_radians(x):
     
     return x*pi/180
        
     
def distance_in_km_between_points(lat1,long1,lat2,long2):
     """Get distance with Haversine formula."""
     
     r=6371  #earth's avg. radius
     var_lat   = degrees_to_radians(lat2-lat1)
     var_long  = degrees_to_radians(long2-long1)
     dist = 2*r*asin( sqrt( abs(sin(var_lat/2)*sin(var_lat/2)+cos(degrees_to_radians(lat1))*cos(degrees_to_radians(lat2))*sin(var_long/2)*sin(var_long/2) )  ))
     
     return float("{0:.1f}".format(dist))


def arc_coord_to_deg(string):
     """Converting string '54 05 23 N' to 54.09 (deg)"""
     
     winkel = 0
     string = string.lstrip()                     #remove leading empty characters
     for i in range(len( string.split(' ',3)) ):  #split string of several numbers to list with numbers
          try:
               winkel+=int(string.split(' ',3)[i])/(60**i)
          except ValueError:
               pass
     
     return winkel
          

def calculate_path_length(list_of_random_towns):
     """Calculate total length of path between list of towns"""
     length = 0
     for i in range(len(list_of_random_towns)):
          if i <= len(list_of_random_towns)-2:
               step = distance_in_km_between_points(list_of_random_towns[i][1],list_of_random_towns[i][2],list_of_random_towns[i+1][1],list_of_random_towns[i+1][2])
               length += step
          else:
               pass
     return float("{0:.1f}".format(length))

     
def switch_two_elements(liste):
     """Switch two elements of a list (of random towns) (NOT switching start point/end point)"""
     while True:
          a=random.randint(1,len(liste)-2)
          b=random.randint(1,len(liste)-2)
          if a==b:
               continue                                # try again for new values if a==b
          else:
               break
     #print(a,b)
     help_value=liste[a]
     liste[a]=liste[b]
     liste[b]=help_value
     
     return liste
     
def revert_one_path(liste):
     """[1,2,3,4,5,6,7,8,9,10] -> [1,2, 9,8,7,6,5,4,3, 10]"""
     
     
     a=random.randint(1,len(liste)-3)
     b=random.randint(a+2,len(liste)-1)
     help_value=liste[a:b][::-1]
     #print("a=",a)
     #print("b=",b)
     #print(help_value)
     
     return liste[:a]+help_value+liste[b:] #liste[b:] ist inklusiv -> Endpunkt der Liste wird nie verändert
     
     

































"""Beispiele"""
#help_list=[towns[43],towns[40],towns[31],towns[46],towns[4],towns[43]]
##print(help_list)
#names=[help_list[i][0] for i in range(len(help_list)-1)]
#lats=[help_list[i][1] for i in range(len(help_list))]
#longs=[help_list[i][2] for i in range(len(help_list))]
#print(calculate_path_length(help_list))
#print("{0:.3f}".format(arc_coord_to_deg("54 05 23 N")),"deg")                                                     #54.09°
#print("{0:.3f}".format(distance_in_km_between_points(52.52,13.2975,53.5492,9.9919)),"km")                        #Berlin, Hamburg    ~250km

#print(distance_in_km_between_points(towns[4][1],towns[4][2],towns[30][1] ,towns[30][2]))      #Berlin, Hamburg
#for i in range(len(towns)):
#    print(i)
#    print(towns[i])

#print(degrees_to_radians(360))              #Funktioniert.


