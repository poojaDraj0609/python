#digital clock

import time
import sys

h = 5
m = 3
s = 0

while(True):
    sys.stdout.write("\r {:02d}:{:02d}:{:02d}".format(h,m,s))
    sys.stdout.flush()
    time.sleep(1)
    
    s = s+1
    if (s == 60):
        m = m+1
        s = 0
        
    if (m == 60):
        s = 0
        m = 0
        h = h+1
            
    if(h == 12):
        s = 0
        m = 0
        h = 0


            
            
   
