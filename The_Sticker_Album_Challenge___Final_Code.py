album_capacity = 600
purchased_stickers = 800

import random

random.randint(1,600)

album = []
random.seed(123)

for i in range(purchased_stickers):
    sticker = (random.randint(1,600))
    if sticker in album: 
        pass
    else: 
        album.append(sticker) 
        
        
         
sims = 10000  #Modify This number for Multiple Simulations

results =[]
random.seed(123)
for m in range(sims):
    album = []
    #random.seed(123)
    for i in range(purchased_stickers):
        sticker = (random.randint(1,600))
        if sticker in album:
            pass
        else:
            album.append(sticker)
    length = len(album)
    results.append(length)                
        
    
        
Min = min(results) 
Max = max(results)
Mean = sum(results)/len(results)     

def Med(lst):
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0
Median = Med(results)   


    
import matplotlib.pyplot as plt
plt.style.use("seaborn")    

plt.hist(results, bins = (Max-Min+1), density = False)
plt.vlines(Mean, 0, 50)
plt.xlabel("Number of Unique Stickers")
plt.ylabel("No. of Occurences")
plt.title("No. of unique Stickers with 800 Purchased Stickers")
plt.show()     



def StickerAlbum(album_capacity = 600, purchased_stickers = 800, sims = 1000, seed = 123):
    results =[]
    random.seed(seed)
    for m in range(sims):
        album = []
        for i in range(purchased_stickers):
            sticker = (random.randint(1,album_capacity))
            if sticker in album:
                pass
            else:
                album.append(sticker)
        length = len(album)
        results.append(length)
    Mean =  sum(results)/len(results)
    return Mean  



for i in range(1485, 1495):
    print(StickerAlbum(purchased_stickers=i))    

StickerAlbum(purchased_stickers=1491, sims = 10000)  

for i in range(10):
    print(StickerAlbum(purchased_stickers=1491, sims = 10000, seed = i))
    
    
    

while result < target:
    random_start+=1
    result = StickerAlbum(purchased_stickers=random_start, sims = 10)
    print(random_start, result)

random_start = 800
target = 550
learning_rate = 1

result = StickerAlbum(album_capacity = 600, purchased_stickers = int(random_start), sims = 10, seed = 123)

delta = (result-target)

random_start -= round(learning_rate * delta)
   
    

random_start = 800
target = 550
learning_rate = 7
epochs = 20
tolerance = 0.5 

for _ in range(epochs):
    result = StickerAlbum(album_capacity = 600, purchased_stickers = int(random_start), sims = 10, seed = 123)
    delta = (result-target)
    print(random_start, result)
    if abs(delta)<tolerance:
        break
    else:
        random_start -= round(learning_rate * delta)


   
def optimize(album_capacity = 600, random_start = 800, sims = 10, seed = 123, 
             target = 550, learning_rate = 7, epochs = 20, tolerance = 0.5):
    
    for _ in range(epochs):
        result = StickerAlbum(album_capacity = album_capacity, purchased_stickers = int(random_start), sims = sims, seed = seed)
        delta = (result-target)
        #print(random_start, result)
        if abs(delta)<tolerance:
            break
        else:
            random_start -= round(learning_rate * delta)
    return random_start, result

optimize(sims = 1000, tolerance = 0.1)

optimize(album_capacity= 471, target = 421, random_start = 200, sims = 100, tolerance = 0.2)
    
    

    
import matplotlib.pyplot as plt
plt.style.use("seaborn")

StickerAlbum(purchased_stickers= 1000)

y2 = []
for i in range(1, 2001, 20):
    result = StickerAlbum(purchased_stickers=i, sims = 10)
    y2.append(result)

#print(len(y2))

xmin, xmax = 0 , 2000
ymin, ymax = 0 , 600

plt.figure(figsize = (12,6))
#plt.plot(range(1, 2001, 1),y)
plt.plot(range(1, 2001, 20),y2)
plt.axis((xmin,xmax,ymin,ymax))
plt.hlines(550, xmin, xmax, color = "red", linestyle = "--")
plt.vlines(1491, ymin, ymax, color = "green", linestyle = "--")
plt.xlabel("Purchased Stickers")
plt.ylabel("Unique Stickers")
plt.title("Sticker Album Simulation (capacity = 600)", fontsize = 15)
plt.show()
    
    

 #Fine Tuning Default Parameters

optimize(album_capacity=600, target = 300, random_start= 800, learning_rate = 2) #does not work for smaller targets   

optimize(album_capacity=600, target = 595, random_start= 800, learning_rate = 10, epochs = 20) #flat part of the curve

optimize(album_capacity=600, target = 595, random_start= 800, learning_rate = 7, epochs = 50) #flat part of the curve

optimize(album_capacity=600, target = 595, random_start= 3000, learning_rate= 10) #random start at very flat part



#Stress Tests

optimize(album_capacity= 600, target = 599, learning_rate = 10) #very flat point of the curve

optimize(album_capacity= 600, target = 550, learning_rate = 4) #moderate point of the curve

optimize(album_capacity=600, target = 10, learning_rate = 1) #steep point of the curve

optimize(album_capacity=20, target = 19, tolerance = 0.2, learning_rate = 4) #small album, flat point

optimize(album_capacity=20, target = 15, tolerance = 0.2, learning_rate = 4) # small album, moderate point

optimize(album_capacity=20, target = 3, tolerance = 0.2, learning_rate= 1, sims = 10000) #small album, steep point

optimize(album_capacity=2000, target = 1990, learning_rate=10) #large album, flat point

optimize(album_capacity=2000, target = 1800, learning_rate= 4) #large album, moderate point

optimize(album_capacity=2000, target = 100, learning_rate= 1) #large album, steep point



    
def optimize(album_capacity = 600, random_start_frac = 0.8, sims = 10, seed = 123, 
             target = 550, learning_rate = 4, epochs = 100, tolerance = 0.5):
    
    random_start = round(album_capacity * random_start_frac)
    
    for _ in range(epochs):
        result = StickerAlbum(album_capacity = album_capacity, purchased_stickers = int(random_start), sims = sims, seed = seed)
        delta = (result-target)
        #print(random_start, result)
        if abs(delta)<tolerance:
            break
        else:
            random_start -= round(learning_rate * delta)
    return random_start, result
    
    



    
    
    
    
    
    
    
    
    






       