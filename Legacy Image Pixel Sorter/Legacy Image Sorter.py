from PIL import Image as img
import math as m
import time

time1 = time.time()

the_image = img.open("shweeb yourself.jpg")

pixel_map = the_image.load()

width, height = the_image.size

def evalu(val):     #this determins how the sort works change the equasion to change what it is sorted by
    return ((val[2]+val[0]+val[1])*-1 + val[3]*10)

frac_hgt = height   #modify this to change the length of the sort section






##### dont touch anything bellow here and then conplain its broke #######

offset = 0
fractions = height//frac_hgt
remainda = height%fractions
lastpercent = 0

for i in range(width):#across
    lizt = []
    offset = 0
    #add these lines directly bellow the seccond instance of offset = 0 and before the next for loop
    frac_hgt = height#round(height *  ((m.sin(i*2)/2.05) + 0.5))
    fractions = height//frac_hgt
    remainda = height%fractions

    for t in range(fractions):
        lizt = []
        for j in range(frac_hgt):
            lizt.append((pixel_map[i,j+offset][0], pixel_map[i,j+offset][1] ,pixel_map[i,j+offset][2], j)) 

        lizt.sort(key = evalu)
            
        for j in range(frac_hgt): 
            pixel_map[i,j+offset] = lizt[j]    

        offset = offset + frac_hgt
    
    for j in range(remainda):
        lizt.append((pixel_map[i,j+offset][0], pixel_map[i,j+offset][1] ,pixel_map[i,j+offset][2], j))    
        lizt.sort(key = evalu)

    for j in range(remainda):
        pixel_map[i,j+offset] = lizt[j]        

    if (round(i/width,2) > lastpercent):
        lastpercent = round(i/width,2)
        print(str(lastpercent*100))


    
    #print(str(i) + " of " + str(width))
    #uncoment this if its takeing a long time otherwise dont



time2 = time.time()
runtime = time2 - time1
print(runtime)
the_image.show()
print("'done killing'")
the_image.save("sorted/"+str(time.time()).replace(".","")+".png")

