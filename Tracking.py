# -*- coding: utf-8 -*-
"""

@author: IbrahimD
"""

import math
import operator
import time

class Blob:   
    
    number= x = y = first_x = first_y = 0
    radius = 0
    create_time = update_time = 0
    total_disp = 0
    
    def __init__(self,number,x,y,radius):
        self.number = number
        self.first_x = self.x = x
        self.first_y = self.y = y
        self.radius = radius
        self.create_time = self.update_time = int(time.time())
    
    def update(self,x,y):
        self.x = x
        self.y = y
        self.update_time = int(time.time())
        self.total_disp = math.sqrt( pow((x-self.first_x),2) + pow((y-self.first_y),2) )


class Tracking:

    blob_list = [] 
    number_of_blobs=0
    min_dist_between_blobs=0
    track_counter = 0
    
    def __init__(self,min_dist_between_blobs):
        self.blob_list.clear()
        self.min_dist_between_blobs = min_dist_between_blobs
         
    def add_blob(self,b):
        self.blob_list.append(b)
       
    def getblobs(self):                       
       return self.blob_list    
        
   
    
    def track(self,x,y,radius):
                        
        self.track_counter +=1
        
        
        if len(self.blob_list)==0:
            self.number_of_blobs =1
            b1 = Blob(1,x,y,radius)
            self.blob_list.append(b1)
#            return
        
        distances = []
        for b in self.blob_list:
            dist = math.sqrt( pow((x-b.x),2) + pow((y-b.y),2) )
            distances.append(dist)


        min_index, min_value = min(enumerate(distances), key=operator.itemgetter(1))
#        print(min_index,min_value)

        if min_value < self.min_dist_between_blobs :
            self.blob_list[min_index].update(x,y)       
        else:
            self.number_of_blobs += 1
            b1 = Blob(self.number_of_blobs,x,y,radius)
            self.blob_list.append(b1)
        
        
        timenow = int(time.time())
        # delete no updated elements for some time
        deleted_elements=[]
        for i in range (0,len(self.blob_list)):
            
            blob = self.blob_list[i] 
#            print("blob: ",blob.x,blob.y)
#            print("blob[",i,"].total_displacement: ",blob.total_displacement)
            if (timenow-blob.update_time)>1:
                deleted_elements.append(i)
                
            if (timenow-blob.create_time)>1 and blob.total_disp<10 :
                deleted_elements.append(i)


        
        print("len(deleted_elements) ",len(deleted_elements))
        
        self.blob_list = [x for i,x in enumerate(self.blob_list) if i not in deleted_elements]
        
#        self.number_of_blobs -= len(deleted_elements)
                     
        print("number_of_blobs ", self.number_of_blobs )
#        print("len(self.blob_list) ", len(self.blob_list) )
                   
                