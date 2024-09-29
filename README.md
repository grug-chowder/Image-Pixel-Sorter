how to use:

1. sort
   input a filepath and the selected image will be sorted and then saved as a new file useing the current settings or default if there are non

   Alternitively you can enter nothing to input the last successful filepath(within runtime) for easy use

3. settings
   there are multiple settings that can be changed to any integer you like athough there are some values that may cause crashes here is a rundown

   rconstant,gconstant,bconstant:
     all of these modify how the pixels are sorted for example if rconstant is 1 and the others 0 the pixels with the most red will be moved upwards
     if they are all equal the brightest pixel will be moved upwards

   heightconstant
     this effectively modifys the "stickyness" of each pixel by factoring in there inital location to the sort you can change how close the new image is to the original
     
   flip
     this flips the direction in which the pixels are sorted (keep as either 1 or -1 for guaranteed* stability)

   heightdiv
     this one breaks the sort into multiple vertical slices in should in theory improve performace but at the cost of not looking very good
     (this sucks ass leave it as 1 or alternitvely fuck around and find out)

   sintoggle
     this one makes stuff wacky in ways i cant explain set to 1 for fun or 0 for not fun will probably break if set to anything other than 1 or 0

   
*nothing is guaranteed to be stable
