from PIL import Image as img
import math as m
import time


class pixelsort:
    def __init__(self,settings = [1,1,1,10,-1]):
        self.rconstant = settings[0]
        self.gconstant = settings[1]
        self.bconstant = settings[2]
        self.heightconstant = settings[3]
        self.flip = settings[4]
        self.lastpath = ""

    def changesettings(self,settings = [1,1,1,10,-1]):
        self.rconstant = settings[0]
        self.gconstant = settings[1]
        self.bconstant = settings[2]
        self.heightconstant = settings[3]
        self.flip = settings[4]
    
    def evalu(self,val):     #this determins how the sort works
        return ((val[0]*self.rconstant+val[1]*self.gconstant+val[2]*self.bconstant)*self.flip + val[3]*self.heightconstant)
    
    def bloodygo(self):      #main function
        while True:
            path = input("input a filepath, and get it right")
            if path == "":
                path = self.lastpath
            try:
                the_image = img.open(path)
                break
            except:
                pass
        
        self.lastpath = path

        
        time1 = time.time()#functions/initalisation things
        pixel_map = the_image.load()
        width, height = the_image.size

        frac_hgt = height #getting some constants in place
        fractions = height//frac_hgt
        remainda = height%fractions
        lastpercent = 0

        for i in range(width):#stepping across the x axis
            lizt = []
            offset = 0                                                 #should be toggleable
            frac_hgt = height                                          #round(height *  ((m.sin(i*2)/2.05) + 0.5))
            fractions = height//frac_hgt
            remainda = height%fractions

            for t in range(fractions):
                lizt = []
                for j in range(frac_hgt):
                    lizt.append((pixel_map[i,j+offset][0], pixel_map[i,j+offset][1] ,pixel_map[i,j+offset][2], j)) 

                lizt.sort(key = self.evalu)
                    
                for j in range(frac_hgt): 
                    pixel_map[i,j+offset] = lizt[j]    

                offset = offset + frac_hgt
            
            for j in range(remainda):#i dont think this code works but i dont think any of it is needed atm, i could be wrong tho, so ill keep it uncommented for now
                lizt.append((pixel_map[i,j+offset][0], pixel_map[i,j+offset][1] ,pixel_map[i,j+offset][2], j))    
                lizt.sort(key = self.evalu)

            for j in range(remainda):
                pixel_map[i,j+offset] = lizt[j]        

            if (round(i/width,2) > lastpercent):
                lastpercent = round(i/width,2)
                print(str(lastpercent*100))
        
        time2 = time.time()
        runtime = time2 - time1
        print(runtime)
        the_image.show()
        print("'done killing'")
        the_image.save("sorted/"+str(time.time()).replace(".","")+".png")

def getsomesettings():
    smallist = ("rconstant","gconstant","bconstant","heightconstant","flip")
    outlist = [1,1,1,10,-1]
    print("""Settings: rconstant,gconstant,bconstant,heightconstant,flip
To change a setting simply write its name and the value you want to change it to or write kill to leave:""")
    while True:
        input = input()
        input.strip()
        input.lower()

        for i in (smallist):
            if input.startswith(smallist(i)):
                try:
                    input = int(input.replace(smallist(i),""))
                    outlist[i] = input
                    print(" done!")
                except:
                    print("that was wrong somehow")
        if input.startswith("kill"):
            return outlist
        
        
            

lets = pixelsort()

while True:
    value = input("""1.pixel sort
2.change settings
3.exit""")
    if value == "1":
        lets.bloodygo()
    elif value == "2":
        settings = getsomesettings()
        lets.changesettings(settings)
    elif value =="3":
        exit()

