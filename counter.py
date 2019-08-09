#Count every 5 second using time
import time
x = 0

while True:
    x += 1    
    print("Count down -> ", x)
    time.sleep(5)