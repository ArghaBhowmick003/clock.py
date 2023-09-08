import time
from os import system, name

local_time = time.localtime() 
''''
Morning : 04.00 - 11.00
Noon : 12.00 - 15.00
After Noon : 16.00 - 17.00
Evening : 18.00 - 20.00
Night : 21.00 - 00.00
Late Night : 00.01 - 03.00
'''
def clear():
    if name=='nt':
        system('cls')
    else:
        system('clear')
    
def get_current_time():
    local_time = time.localtime()
    hr = local_time.tm_hour
    print(local_time.tm_hour, local_time.tm_min, local_time.tm_sec)
    if hr>=4 and hr <= 11:
        return 'Morning'
    elif hr >=12 and hr <= 15:
        return 'Noon'
    elif hr >= 16 and hr <= 17:
        return 'Afternoon'
    elif hr >= 18 and hr <= 20:
        return 'Evening'
    elif hr >= 21 and hr <= 23:
        if hr == 22:
            return 'Dinner Time'
        return 'Night'
    else:
        return 'Late night' 

if __name__=='__main__':
    try:
        while True:
            clear()
            print(get_current_time())
            time.sleep(1)
    except KeyboardInterrupt:
        clear()
        print("Thanks for using this code.")