# 63
import acabsl
import random
import time

cs = [[255,255,000,000,000,255],[000,255,255,255,000,000],[000,000,000,255,255,255]]

def rc():
  return random.randint(0,5)

def rid():
    return [random.randint(0,8),random.randint(0,6)]


while 1:
# RESET ALL
    acabsl.send(0,0,0,0,0)
    acabsl.send(0,1,0,0,0)
    acabsl.send(0,2,0,0,0)
    acabsl.send(0,3,0,0,0)
    acabsl.send(0,4,0,0,0)
    acabsl.send(0,5,0,0,0)
    acabsl.send(1,0,0,0,0)
    acabsl.send(1,1,0,0,0)
    acabsl.send(1,2,0,0,0)
    acabsl.send(1,3,0,0,0)
    acabsl.send(1,4,0,0,0)
    acabsl.send(1,5,0,0,0)
    acabsl.send(2,0,0,0,0)
    acabsl.send(2,1,0,0,0)
    acabsl.send(2,2,0,0,0)
    acabsl.send(2,3,0,0,0)
    acabsl.send(2,4,0,0,0)
    acabsl.send(2,5,0,0,0)
    acabsl.send(3,0,0,0,0)
    acabsl.send(3,1,0,0,0)
    acabsl.send(3,2,0,0,0)
    acabsl.send(3,3,0,0,0)
    acabsl.send(3,4,0,0,0)
    acabsl.send(3,5,0,0,0)
    acabsl.send(4,0,0,0,0)
    acabsl.send(4,1,0,0,0)
    acabsl.send(4,2,0,0,0)
    acabsl.send(4,3,0,0,0)
    acabsl.send(4,4,0,0,0)
    acabsl.send(4,5,0,0,0)
    acabsl.send(5,0,0,0,0)
    acabsl.send(5,1,0,0,0)
    acabsl.send(5,2,0,0,0)
    acabsl.send(5,3,0,0,0)
    acabsl.send(5,4,0,0,0)
    acabsl.send(5,5,0,0,0)
    acabsl.send(6,0,0,0,0)
    acabsl.send(6,1,0,0,0)
    acabsl.send(6,2,0,0,0)
    acabsl.send(6,3,0,0,0)
    acabsl.send(6,4,0,0,0)
    acabsl.send(6,5,0,0,0)
    acabsl.send(7,0,0,0,0)
    acabsl.send(7,1,0,0,0)
    acabsl.send(7,2,0,0,0)
    acabsl.send(7,3,0,0,0)
    acabsl.send(7,4,0,0,0)
    acabsl.send(7,5,0,0,0)
    time.sleep(0.4)

#START
    acabsl.send(0,0,240,0,0)
    acabsl.send(0,1,240,0,0)
    acabsl.send(1,0,240,0,0)
    time.sleep(0.1)
    acabsl.send(1,1,240,16,0)
    acabsl.send(2,0,240,16,0)
    acabsl.send(2,1,240,16,0)
    time.sleep(0.1)
    acabsl.send(3,0,240,32,0)
    acabsl.send(3,1,240,32,0)
    acabsl.send(4,0,240,32,0)
    acabsl.send(4,1,240,32,0)
    time.sleep(0.1)
    acabsl.send(5,0,240,48,0)
    acabsl.send(5,1,240,48,0)
    acabsl.send(6,1,240,48,0)
    time.sleep(0.1)
    acabsl.send(5,0,240,64,0)
    acabsl.send(5,1,240,64,0)
    acabsl.send(6,1,240,64,0)
    time.sleep(0.1)
    acabsl.send(6,0,240,80,0)
    acabsl.send(7,0,240,80,0)
    acabsl.send(7,1,240,80,0)
    time.sleep(0.1)

# LOOP 1
    acabsl.send(5,2,240,96,0)
    acabsl.send(5,3,240,96,0)
    acabsl.send(6,3,240,96,0)
    acabsl.send(0,0,0,0,0)
    acabsl.send(0,1,0,0,0)
    acabsl.send(1,0,0,0,0)
    time.sleep(0.1)
    acabsl.send(6,2,240,112,0)
    acabsl.send(7,2,240,112,0)
    acabsl.send(7,3,240,112,0)
    acabsl.send(1,1,0,0,0)
    acabsl.send(2,0,0,0,0)
    acabsl.send(2,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(5,4,240,128,0)
    acabsl.send(5,5,240,128,0)
    acabsl.send(6,4,240,128,0)
    acabsl.send(3,0,0,0,0)
    acabsl.send(3,1,0,0,0)
    acabsl.send(4,0,0,0,0)
    acabsl.send(4,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(3,4,240,144,0)
    acabsl.send(3,5,240,144,0)
    acabsl.send(4,4,240,144,0)
    acabsl.send(4,5,240,144,0)
    acabsl.send(5,0,0,0,0)
    acabsl.send(5,1,0,0,0)
    acabsl.send(6,1,0,0,0)
    time.sleep(0.1)

    acabsl.send(1,4,240,160,0)
    acabsl.send(2,4,240,160,0)
    acabsl.send(2,5,240,160,0)
    acabsl.send(6,0,0,0,0)
    acabsl.send(7,0,0,0,0)
    acabsl.send(7,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(0,2,240,176,0)
    acabsl.send(0,3,240,176,0)
    acabsl.send(1,2,240,176,0)
    acabsl.send(5,2,0,0,0)
    acabsl.send(5,3,0,0,0)
    acabsl.send(6,3,0,0,0)
    time.sleep(0.1)
    acabsl.send(1,3,240,192,0)
    acabsl.send(2,2,240,192,0)
    acabsl.send(2,3,240,192,0)
    acabsl.send(6,2,0,0,0)
    acabsl.send(7,2,0,0,0)
    acabsl.send(7,3,0,0,0)
    time.sleep(0.1)
    acabsl.send(0,0,240,208,0)
    acabsl.send(0,1,240,208,0)
    acabsl.send(1,0,240,208,0)
    acabsl.send(5,4,0,0,0)
    acabsl.send(5,5,0,0,0)
    acabsl.send(6,4,0,0,0)
    time.sleep(0.1)

    acabsl.send(1,1,240,224,0)
    acabsl.send(2,0,240,224,0)
    acabsl.send(2,1,240,224,0)
    acabsl.send(3,4,0,0,0)
    acabsl.send(3,5,0,0,0)
    acabsl.send(4,4,0,0,0)
    acabsl.send(4,5,0,0,0)
    time.sleep(0.1)
    acabsl.send(3,0,240,240,0)
    acabsl.send(3,1,240,240,0)
    acabsl.send(4,0,240,240,0)
    acabsl.send(4,1,240,240,0)
    acabsl.send(1,4,0,0,0)
    acabsl.send(2,4,0,0,0)
    acabsl.send(2,5,0,0,0)
    time.sleep(0.1)
    acabsl.send(5,0,224,240,0)
    acabsl.send(5,1,224,240,0)
    acabsl.send(6,1,224,240,0)
    acabsl.send(0,2,0,0,0)
    acabsl.send(0,3,0,0,0)
    acabsl.send(1,2,0,0,0)
    time.sleep(0.1)
    acabsl.send(6,0,208,240,0)
    acabsl.send(7,0,208,240,0)
    acabsl.send(7,1,208,240,0)
    acabsl.send(1,3,0,0,0)
    acabsl.send(2,2,0,0,0)
    acabsl.send(2,3,0,0,0)
    time.sleep(0.1)

# LOOP 2
    acabsl.send(5,2,192,240,0)
    acabsl.send(5,3,192,240,0)
    acabsl.send(6,3,192,240,0)
    acabsl.send(0,0,0,0,0)
    acabsl.send(0,1,0,0,0)
    acabsl.send(1,0,0,0,0)
    time.sleep(0.1)
    acabsl.send(6,2,176,240,0)
    acabsl.send(7,2,176,240,0)
    acabsl.send(7,3,176,240,0)
    acabsl.send(1,1,0,0,0)
    acabsl.send(2,0,0,0,0)
    acabsl.send(2,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(5,4,160,240,0)
    acabsl.send(5,5,160,240,0)
    acabsl.send(6,4,160,240,0)
    acabsl.send(3,0,0,0,0)
    acabsl.send(3,1,0,0,0)
    acabsl.send(4,0,0,0,0)
    acabsl.send(4,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(3,4,144,240,0)
    acabsl.send(3,5,144,240,0)
    acabsl.send(4,4,144,240,0)
    acabsl.send(4,5,144,240,0)
    acabsl.send(5,0,0,0,0)
    acabsl.send(5,1,0,0,0)
    acabsl.send(6,1,0,0,0)
    time.sleep(0.1)

    acabsl.send(1,4,128,240,0)
    acabsl.send(2,4,128,240,0)
    acabsl.send(2,5,128,240,0)
    acabsl.send(6,0,0,0,0)
    acabsl.send(7,0,0,0,0)
    acabsl.send(7,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(0,2,112,240,0)
    acabsl.send(0,3,112,240,0)
    acabsl.send(1,2,112,240,0)
    acabsl.send(5,2,0,0,0)
    acabsl.send(5,3,0,0,0)
    acabsl.send(6,3,0,0,0)
    time.sleep(0.1)
    acabsl.send(1,3,96,240,0)
    acabsl.send(2,2,96,240,0)
    acabsl.send(2,3,96,240,0)
    acabsl.send(6,2,0,0,0)
    acabsl.send(7,2,0,0,0)
    acabsl.send(7,3,0,0,0)
    time.sleep(0.1)
    acabsl.send(0,0,80,240,0)
    acabsl.send(0,1,80,240,0)
    acabsl.send(1,0,80,240,0)
    acabsl.send(5,4,0,0,0)
    acabsl.send(5,5,0,0,0)
    acabsl.send(6,4,0,0,0)
    time.sleep(0.1)

    acabsl.send(1,1,64,240,0)
    acabsl.send(2,0,64,240,0)
    acabsl.send(2,1,64,240,0)
    acabsl.send(3,4,0,0,0)
    acabsl.send(3,5,0,0,0)
    acabsl.send(4,4,0,0,0)
    acabsl.send(4,5,0,0,0)
    time.sleep(0.1)
    acabsl.send(3,0,48,240,0)
    acabsl.send(3,1,48,240,0)
    acabsl.send(4,0,48,240,0)
    acabsl.send(4,1,48,240,0)
    acabsl.send(1,4,0,0,0)
    acabsl.send(2,4,0,0,0)
    acabsl.send(2,5,0,0,0)
    time.sleep(0.1)
    acabsl.send(5,0,32,240,0)
    acabsl.send(5,1,32,240,0)
    acabsl.send(6,1,32,240,0)
    acabsl.send(0,2,0,0,0)
    acabsl.send(0,3,0,0,0)
    acabsl.send(1,2,0,0,0)
    time.sleep(0.1)
    acabsl.send(6,0,16,240,0)
    acabsl.send(7,0,16,240,0)
    acabsl.send(7,1,16,240,0)
    acabsl.send(1,3,0,0,0)
    acabsl.send(2,2,0,0,0)
    acabsl.send(2,3,0,0,0)
    time.sleep(0.1)

# LOOP 3
    acabsl.send(5,2,0,240,0)
    acabsl.send(5,3,0,240,0)
    acabsl.send(6,3,0,240,0)
    acabsl.send(0,0,0,0,0)
    acabsl.send(0,1,0,0,0)
    acabsl.send(1,0,0,0,0)
    time.sleep(0.1)
    acabsl.send(6,2,0,240,16)
    acabsl.send(7,2,0,240,16)
    acabsl.send(7,3,0,240,16)
    acabsl.send(1,1,0,0,0)
    acabsl.send(2,0,0,0,0)
    acabsl.send(2,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(5,4,0,240,32)
    acabsl.send(5,5,0,240,32)
    acabsl.send(6,4,0,240,32)
    acabsl.send(3,0,0,0,0)
    acabsl.send(3,1,0,0,0)
    acabsl.send(4,0,0,0,0)
    acabsl.send(4,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(3,4,0,240,48)
    acabsl.send(3,5,0,240,48)
    acabsl.send(4,4,0,240,48)
    acabsl.send(4,5,0,240,48)
    acabsl.send(5,0,0,0,0)
    acabsl.send(5,1,0,0,0)
    acabsl.send(6,1,0,0,0)
    time.sleep(0.1)

    acabsl.send(1,4,0,240,64)
    acabsl.send(2,4,0,240,64)
    acabsl.send(2,5,0,240,64)
    acabsl.send(6,0,0,0,0)
    acabsl.send(7,0,0,0,0)
    acabsl.send(7,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(0,2,0,240,80)
    acabsl.send(0,3,0,240,80)
    acabsl.send(1,2,0,240,80)
    acabsl.send(5,2,0,0,0)
    acabsl.send(5,3,0,0,0)
    acabsl.send(6,3,0,0,0)
    time.sleep(0.1)
    acabsl.send(1,3,0,240,96)
    acabsl.send(2,2,0,240,96)
    acabsl.send(2,3,0,240,96)
    acabsl.send(6,2,0,0,0)
    acabsl.send(7,2,0,0,0)
    acabsl.send(7,3,0,0,0)
    time.sleep(0.1)
    acabsl.send(0,0,0,240,112)
    acabsl.send(0,1,0,240,112)
    acabsl.send(1,0,0,240,112)
    acabsl.send(5,4,0,0,0)
    acabsl.send(5,5,0,0,0)
    acabsl.send(6,4,0,0,0)
    time.sleep(0.1)

    acabsl.send(1,1,0,240,128)
    acabsl.send(2,0,0,240,128)
    acabsl.send(2,1,0,240,128)
    acabsl.send(3,4,0,0,0)
    acabsl.send(3,5,0,0,0)
    acabsl.send(4,4,0,0,0)
    acabsl.send(4,5,0,0,0)
    time.sleep(0.1)
    acabsl.send(3,0,0,240,144)
    acabsl.send(3,1,0,240,144)
    acabsl.send(4,0,0,240,144)
    acabsl.send(4,1,0,240,144)
    acabsl.send(1,4,0,0,0)
    acabsl.send(2,4,0,0,0)
    acabsl.send(2,5,0,0,0)
    time.sleep(0.1)
    acabsl.send(5,0,0,240,160)
    acabsl.send(5,1,0,240,160)
    acabsl.send(6,1,0,240,160)
    acabsl.send(0,2,0,0,0)
    acabsl.send(0,3,0,0,0)
    acabsl.send(1,2,0,0,0)
    time.sleep(0.1)
    acabsl.send(6,0,0,240,176)
    acabsl.send(7,0,0,240,176)
    acabsl.send(7,1,0,240,176)
    acabsl.send(1,3,0,0,0)
    acabsl.send(2,2,0,0,0)
    acabsl.send(2,3,0,0,0)
    time.sleep(0.1)

# LOOP 4
    acabsl.send(5,2,0,240,192)
    acabsl.send(5,3,0,240,192)
    acabsl.send(6,3,0,240,192)
    acabsl.send(0,0,0,0,0)
    acabsl.send(0,1,0,0,0)
    acabsl.send(1,0,0,0,0)
    time.sleep(0.1)
    acabsl.send(6,2,0,240,208)
    acabsl.send(7,2,0,240,208)
    acabsl.send(7,3,0,240,208)
    acabsl.send(1,1,0,0,0)
    acabsl.send(2,0,0,0,0)
    acabsl.send(2,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(5,4,0,240,224)
    acabsl.send(5,5,0,240,224)
    acabsl.send(6,4,0,240,224)
    acabsl.send(3,0,0,0,0)
    acabsl.send(3,1,0,0,0)
    acabsl.send(4,0,0,0,0)
    acabsl.send(4,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(3,4,0,240,240)
    acabsl.send(3,5,0,240,240)
    acabsl.send(4,4,0,240,240)
    acabsl.send(4,5,0,240,240)
    acabsl.send(5,0,0,0,0)
    acabsl.send(5,1,0,0,0)
    acabsl.send(6,1,0,0,0)
    time.sleep(0.1)

    acabsl.send(1,4,0,224,240)
    acabsl.send(2,4,0,224,240)
    acabsl.send(2,5,0,224,240)
    acabsl.send(6,0,0,0,0)
    acabsl.send(7,0,0,0,0)
    acabsl.send(7,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(0,2,0,208,240)
    acabsl.send(0,3,0,208,240)
    acabsl.send(1,2,0,208,240)
    acabsl.send(5,2,0,0,0)
    acabsl.send(5,3,0,0,0)
    acabsl.send(6,3,0,0,0)
    time.sleep(0.1)
    acabsl.send(1,3,0,192,240)
    acabsl.send(2,2,0,192,240)
    acabsl.send(2,3,0,192,240)
    acabsl.send(6,2,0,0,0)
    acabsl.send(7,2,0,0,0)
    acabsl.send(7,3,0,0,0)
    time.sleep(0.1)
    acabsl.send(0,0,0,176,240)
    acabsl.send(0,1,0,176,240)
    acabsl.send(1,0,0,176,240)
    acabsl.send(5,4,0,0,0)
    acabsl.send(5,5,0,0,0)
    acabsl.send(6,4,0,0,0)
    time.sleep(0.1)

    acabsl.send(1,1,0,160,240)
    acabsl.send(2,0,0,160,240)
    acabsl.send(2,1,0,160,240)
    acabsl.send(3,4,0,0,0)
    acabsl.send(3,5,0,0,0)
    acabsl.send(4,4,0,0,0)
    acabsl.send(4,5,0,0,0)
    time.sleep(0.1)
    acabsl.send(3,0,0,144,240)
    acabsl.send(3,1,0,144,240)
    acabsl.send(4,0,0,144,240)
    acabsl.send(4,1,0,144,240)
    acabsl.send(1,4,0,0,0)
    acabsl.send(2,4,0,0,0)
    acabsl.send(2,5,0,0,0)
    time.sleep(0.1)
    acabsl.send(5,0,0,128,240)
    acabsl.send(5,1,0,128,240)
    acabsl.send(6,1,0,128,240)
    acabsl.send(0,2,0,0,0)
    acabsl.send(0,3,0,0,0)
    acabsl.send(1,2,0,0,0)
    time.sleep(0.1)
    acabsl.send(6,0,0,112,240)
    acabsl.send(7,0,0,112,240)
    acabsl.send(7,1,0,112,240)
    acabsl.send(1,3,0,0,0)
    acabsl.send(2,2,0,0,0)
    acabsl.send(2,3,0,0,0)
    time.sleep(0.1)

# LOOP 5
    acabsl.send(5,2,0,96,240)
    acabsl.send(5,3,0,96,240)
    acabsl.send(6,3,0,96,240)
    acabsl.send(0,0,0,0,0)
    acabsl.send(0,1,0,0,0)
    acabsl.send(1,0,0,0,0)
    time.sleep(0.1)
    acabsl.send(6,2,0,80,240)
    acabsl.send(7,2,0,80,240)
    acabsl.send(7,3,0,80,240)
    acabsl.send(1,1,0,0,0)
    acabsl.send(2,0,0,0,0)
    acabsl.send(2,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(5,4,0,64,240)
    acabsl.send(5,5,0,64,240)
    acabsl.send(6,4,0,64,240)
    acabsl.send(3,0,0,0,0)
    acabsl.send(3,1,0,0,0)
    acabsl.send(4,0,0,0,0)
    acabsl.send(4,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(3,4,0,48,240)
    acabsl.send(3,5,0,48,240)
    acabsl.send(4,4,0,48,240)
    acabsl.send(4,5,0,48,240)
    acabsl.send(5,0,0,0,0)
    acabsl.send(5,1,0,0,0)
    acabsl.send(6,1,0,0,0)
    time.sleep(0.1)

    acabsl.send(1,4,0,32,240)
    acabsl.send(2,4,0,32,240)
    acabsl.send(2,5,0,32,240)
    acabsl.send(6,0,0,0,0)
    acabsl.send(7,0,0,0,0)
    acabsl.send(7,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(0,2,0,16,240)
    acabsl.send(0,3,0,16,240)
    acabsl.send(1,2,0,16,240)
    acabsl.send(5,2,0,0,0)
    acabsl.send(5,3,0,0,0)
    acabsl.send(6,3,0,0,0)
    time.sleep(0.1)
    acabsl.send(1,3,0,0,240)
    acabsl.send(2,2,0,0,240)
    acabsl.send(2,3,0,0,240)
    acabsl.send(6,2,0,0,0)
    acabsl.send(7,2,0,0,0)
    acabsl.send(7,3,0,0,0)
    time.sleep(0.1)
    acabsl.send(0,0,16,0,240)
    acabsl.send(0,1,16,0,240)
    acabsl.send(1,0,16,0,240)
    acabsl.send(5,4,0,0,0)
    acabsl.send(5,5,0,0,0)
    acabsl.send(6,4,0,0,0)
    time.sleep(0.1)

    acabsl.send(1,1,32,0,240)
    acabsl.send(2,0,32,0,240)
    acabsl.send(2,1,32,0,240)
    acabsl.send(3,4,0,0,0)
    acabsl.send(3,5,0,0,0)
    acabsl.send(4,4,0,0,0)
    acabsl.send(4,5,0,0,0)
    time.sleep(0.1)
    acabsl.send(3,0,48,0,240)
    acabsl.send(3,1,48,0,240)
    acabsl.send(4,0,48,0,240)
    acabsl.send(4,1,48,0,240)
    acabsl.send(1,4,0,0,0)
    acabsl.send(2,4,0,0,0)
    acabsl.send(2,5,0,0,0)
    time.sleep(0.1)
    acabsl.send(5,0,64,0,240)
    acabsl.send(5,1,64,0,240)
    acabsl.send(6,1,64,0,240)
    acabsl.send(0,2,0,0,0)
    acabsl.send(0,3,0,0,0)
    acabsl.send(1,2,0,0,0)
    time.sleep(0.1)
    acabsl.send(6,0,80,0,240)
    acabsl.send(7,0,80,0,240)
    acabsl.send(7,1,80,0,240)
    acabsl.send(1,3,0,0,0)
    acabsl.send(2,2,0,0,0)
    acabsl.send(2,3,0,0,0)
    time.sleep(0.1)

# END
    acabsl.send(0,0,0,0,0)
    acabsl.send(0,1,0,0,0)
    acabsl.send(1,0,0,0,0)
    time.sleep(0.1)
    acabsl.send(1,1,0,0,0)
    acabsl.send(2,0,0,0,0)
    acabsl.send(2,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(3,0,0,0,0)
    acabsl.send(3,1,0,0,0)
    acabsl.send(4,0,0,0,0)
    acabsl.send(4,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(5,0,0,0,0)
    acabsl.send(5,1,0,0,0)
    acabsl.send(6,1,0,0,0)
    time.sleep(0.1)
    acabsl.send(6,0,0,0,0)
    acabsl.send(7,0,0,0,0)
    acabsl.send(7,1,0,0,0)
    time.sleep(0.1)

#DONE