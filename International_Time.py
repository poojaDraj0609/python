# international time zone
from datetime import datetime
import pytz
 
a = pytz.timezone("asia/seoul")
b = datetime.now(a)
print(b)

            
            
   
