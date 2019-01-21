
#Sticker Album Challenge

#Udemy Course - Simulating Real World Problems with Python

#Your Sticker Album has a capacity of 600 unique Stickers (consecutively numbered from 1 to 600) 
#and your budget allows you to buy 800 stickers, hoping to complete the album with max 200 duplicates.

#We assign:
#600 to the variable album_capacity
#800 to the variable purchased_stickers

#1. Getting started...one simulation
#2. Getting probabilistic...with many simulations
#3. Analyzing results and calculating statistics
#4. Automation by writing a Function
#5. Solving (some) advanced Problems / Optimization

#Assumption 1: 
#The stickers are uniformly distributed. This means that all stickers are produced and sold in equal quantities. 
#Hence, the probability of getting a sticker is the same for each sticker (1/600 if we have 600 unique stickers and buy 1 sticker).

#Assumption 2:
#Typically, we can directly order a certain amount of stickers from the vendor of the album/stickers. 
#Let´s assume that, finally, we are still missing the stickers no. 243 and no. 576. 
#Then we can directly order them. However, this option is typically limited to e.g. 50 stickers.

#Assumption 3:
#Stickers are typically sold in packs of e.g. 5 stickers. And there is the guarantee that there are no duplicates within packs.
#We are neglecting this fact and assume that we are buying single stickers, sticker per sticker.





#1. Getting started...one simulation

album_capacity = 600
purchased_stickers = 800

import random

random.randint(1,600)
#simulate the purchase of one sticker. Chooses a random number between 1 and 600, including 1 and 600.
#print(random.randint(1,600))

#Now repeat the process 800 times - For Loop

album = []
random.seed(123) #Set Random Seed to replicate numbers

#for i in range(purchased_stickers):
#    sticker = random.randint(1,600)
#    album.append(sticker)
    
    #800 times create a random integer between 1 and 600
    #Assign to Variable "Sticker"
    #Append to Album
    
#print(album)   
#len(album)
    
#unique = set(album) #Set removes all duplicates from Length
#len(unique) = 451 Unique Count

#duplicates = album.copy()
#for i in unique:
#    duplicates.remove(i)

#len(duplicates) = 349 Duplicates    

for i in range(purchased_stickers):
    sticker = (random.randint(1,600))
    if sticker in album: 
        pass
    else: 
        album.append(sticker)    
        #If the sticker is in the album, pass, else pass into album
    
    
    
    
    
#2. Getting probabilistic...with many simulations    
        
sims = 1000  #Modify This number for Multiple Simulations

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
        
   
#Nested Loop
#For loop inside For Loop    
    
    
    
    
    
#3. Analyzing results and calculating statistics    
    
Min = min(results)
#print(Min)    

Max = max(results)
#print(Max) 
    
Mean = sum(results)/len(results)
#print(Mean)
    
def Med(lst):
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0
Median = Med(results)
#print(Median)    
    

#Plot the results
    
import matplotlib.pyplot as plt
plt.style.use("seaborn")    

plt.hist(results, bins = (Max-Min+1), density = False)
plt.vlines(Mean, 0, 50)
plt.xlabel("Number of Unique Stickers")
plt.ylabel("No. of Occurences")
plt.title("No. of unique Stickers with 800 Purchased Stickers")
plt.show()    
    




#4. Automation by writing a Function

#Let´s define (def) a function called StickerAlbum() with the following parameters and default values inside the parentheses:

#  album_capacity = 600
#  purchased_stickers = 800
#  sims = 1000
#  seed = 123

#def StickerAlbum(album_capacity = 600, purchased_stickers = 800, sims = 1000, seed = 123):
#    return "This is the result of StickerAlbum()"

#print(StickerAlbum())
    
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
    
print(StickerAlbum(purchased_stickers=1491))

#To Automate - Introduce a For Loop

for i in range(1485, 1495):
    print(StickerAlbum(purchased_stickers=i))    
    
#To reduce random noise we need to increase the number of simulations. 
#In statistics 10,000 simulations is a widely used number of simulations that results in acceptable variability of results.    
    
StickerAlbum(purchased_stickers=1491, sims = 10000)    
    
for i in range(10):
    print(StickerAlbum(purchased_stickers=1491, sims = 10000, seed = i))





#5. Solving (some) advanced Problems / Optimization

#  We figured out that, on average, we need to purchase 1,491 stickers in order to receive 550 unique stickers. 
#  However this was solved manually by trial and error. 
#  Now it´s up to you to create an algorithm that solves for the number of required stickers. 
#  Start with simple/inefficient solutions and then try to increase smartness/complexity to improve performance. 

target = 550
random_start = 800

result = StickerAlbum(purchased_stickers=random_start, sims = 10)
#print(result)

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



#Automation

random_start = 800
target = 550
learning_rate = 7
epochs = 20

for _ in range(epochs):
    result = StickerAlbum(album_capacity = 600, purchased_stickers = int(random_start), sims = 10, seed = 123)
    delta = (result-target)
    print(random_start, result)
    random_start -= round(learning_rate * delta)



#Fine Tuning - Add Parameter "tolerance"
    
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

#800   444.7
#1537  553.6
#1512  554.6
#1480  549.9

print(random_start)

#1,480

#RESULTS - WE SHOULD BUY 1,480 STICKERS TO HAVE EXPECTED UNIQUENESS OF 550



#Writing a Solver Function

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


#Optimize Explained

#If I want to get 550 unique stickers (target = 550), how many stickers do I have to buy?

#Section 4, Lecture 43 (For My Reference)




#Visualization

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




  
def optimize(album_capacity = 600, random_start = 800, sims = 10, seed = 123, 
             target = 550, learning_rate = 7, epochs = 20, tolerance = 0.5):
    
    for _ in range(epochs):
        result = StickerAlbum(album_capacity = album_capacity, purchased_stickers = int(random_start), sims = sims, seed = seed)
        delta = (result-target)
        print(random_start, result)
        if abs(delta)<tolerance:
            break
        else:
            random_start -= round(learning_rate * delta)
    return random_start, result


 #Fine Tuning Default Parameters

optimize(album_capacity=600, target = 300, random_start= 800, learning_rate = 2) #does not work for smaller targets   

optimize(album_capacity=600, target = 595, random_start= 800, learning_rate = 10, epochs = 20) #flat part of the curve

optimize(album_capacity=600, target = 595, random_start= 800, learning_rate = 7, epochs = 50) #flat part of the curve

optimize(album_capacity=600, target = 595, random_start= 3000, learning_rate= 10) #random start at very flat part




def optimize(album_capacity = 600, random_start_frac = 0.8, sims = 10, seed = 123, 
             target = 550, learning_rate = 4, epochs = 100, tolerance = 0.5):
    
    random_start = round(album_capacity * random_start_frac)
    
    for _ in range(epochs):
        result = StickerAlbum(album_capacity = album_capacity, purchased_stickers = int(random_start), sims = sims, seed = seed)
        delta = (result-target)
        print(random_start, result)
        if abs(delta)<tolerance:
            break
        else:
            random_start -= round(learning_rate * delta)
    return random_start, result


optimize(target = 550, learning_rate= 4)


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


optimize(album_capacity= 376, target= 326, sims = 1000, tolerance = 0.1)














