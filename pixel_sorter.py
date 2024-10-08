from PIL import Image as img
import math as m
import time

#TODO TRANSPARANCY BUG
#TODO OTHER SETTINGS
#TODO VIDEO SUPPORT

class pixelsort:
    def __init__(self,settings = [1,1,1,10,-1,1,0]):
        self.rconstant = settings[0]
        self.gconstant = settings[1]
        self.bconstant = settings[2]
        self.heightconstant = settings[3]
        self.flip = settings[4]
        self.heightdivconstant = settings[5]           
        self.funsintoggle = settings[6]   
        self.lastpath = ""

    def changesettings(self,settings = [1,1,1,10,-1,1,0]):
        self.rconstant = settings[0]                   #constant for red
        self.gconstant = settings[1]                   #constant for green
        self.bconstant = settings[2]                   #constant for blue
        self.heightconstant = settings[3]              #constant for the "pixel stickyness"
        self.flip = settings[4]                        #used to flip the direction of the sort with either -1 or 1
        self.heightdivconstant = settings[5]           #height subdevide, 1 for deactive greater for active dont use less than one or bigger than the image size will cause a crash
        self.funsintoggle = settings[6]                #weird sin thing make equal to one to activate or 0 to deactivate other values will have unexpected results

    
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
            frac_hgt = round((height/self.heightdivconstant)*(((m.sin(i*2)/2.05) + 0.5)**self.funsintoggle))                                          #round(height *  ((m.sin(i*2)/2.05) + 0.5))
            fractions = height//frac_hgt
            remainda = height%fractions

            for t in range(fractions):
                lizt = []
                for j in range(frac_hgt):
                    lizt.append((pixel_map[i,j+offset][0], pixel_map[i,j+offset][1] ,pixel_map[i,j+offset][2], j)) 

                lizt.sort(key = self.evalu)
                    
                for j in range(frac_hgt): 
                    pixel_map[i,j+offset] = (lizt[j][0],lizt[j][1],lizt[j][2])    

                offset = offset + frac_hgt
            
            for j in range(remainda):#i dont think this code works but i dont think any of it is needed atm, i could be wrong tho, so ill keep it uncommented for now
                lizt.append((pixel_map[i,j+offset][0], pixel_map[i,j+offset][1] ,pixel_map[i,j+offset][2], j))    
                lizt.sort(key = self.evalu)

            for j in range(remainda):
                pixel_map[i,j+offset] = lizt[j]        

            if (round(i/width,2) > lastpercent):
                lastpercent = round(i/width,2)
                print(str(round(lastpercent*100)))
        
        time2 = time.time()
        runtime = time2 - time1
        print(runtime)
        the_image.show()
        print("'done killing'")
        the_image.save("sorted/"+str(time.time()).replace(".","")+".png")

def getsomesettings():
    smallist = ("rconstant","gconstant","bconstant","heightconstant","flip","heightdiv","sintoggle")
    outlist = [1,1,1,10,-1,1,0]
    
    print("""Settings: rconstant,gconstant,bconstant,heightconstant,flip,heightdiv,sintoggle
To change a setting simply write its name and then the value you want to change or write kill to go back:""")
    while True:
        values = str(input("input:"))
        values.strip()
        values.lower()
        if values.startswith("kill") or values.startswith("exit") or values.startswith("die"):
            return outlist

        for i in range(len(smallist)):#steps through every thing in the settings lists checking the input
            if values.startswith(smallist[i]):
                try:
                    values = int(values.replace(smallist[i],""))
                    outlist[i] = values
                    print(" done!")
                    break
                except:
                    print("that was wrong somehow")
        
        
            

lets = pixelsort()

while True:
    value = input("""1.pixel sort
2.change settings
3.exit
""")
    if value == "1":
        lets.bloodygo()
    elif value == "2":
        settings = getsomesettings()
        lets.changesettings(settings)
    elif value =="3":
        exit()

