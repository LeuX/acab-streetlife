# 41
import acabsl
import random
import time

cs = [[255,255,000,000,000,255],[000,255,255,255,000,000],[000,000,000,255,255,255]]

def rc():
  return random.randint(0,5)

def rid():
    return [random.randint(0,8),random.randint(0,6)]


while 1:
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
    acabsl.speedfade(0,0,0,126,255,107)
    acabsl.speedfade(0,1,0,126,255,107)
    acabsl.speedfade(1,0,0,126,255,107)
    acabsl.speedfade(1,1,0,174,255,116)
    acabsl.speedfade(2,0,0,174,255,116)
    acabsl.speedfade(2,1,0,174,255,116)
    acabsl.speedfade(3,0,0,216,255,125)
    acabsl.speedfade(3,1,0,216,255,125)
    acabsl.speedfade(4,0,0,216,255,125)
    acabsl.speedfade(4,1,0,216,255,125)
    acabsl.speedfade(5,0,0,255,246,137)
    acabsl.speedfade(5,1,0,255,246,137)
    acabsl.speedfade(6,1,0,255,246,137)
    acabsl.speedfade(6,0,0,255,198,151)
    acabsl.speedfade(7,0,0,255,198,151)
    acabsl.speedfade(7,1,0,255,198,151)
    acabsl.speedfade(0,2,0,255,156,167)
    acabsl.speedfade(0,3,0,255,156,167)
    acabsl.speedfade(1,2,0,255,156,167)
    acabsl.speedfade(1,3,0,255,108,188)
    acabsl.speedfade(2,2,0,255,108,188)
    acabsl.speedfade(2,3,0,255,108,188)
    acabsl.speedfade(3,2,0,255,60,215)
    acabsl.speedfade(3,3,0,255,60,215)
    acabsl.speedfade(4,2,0,255,60,215)
    acabsl.speedfade(4,3,0,255,60,215)
    acabsl.speedfade(5,2,0,255,18,251)
    acabsl.speedfade(5,3,0,255,18,251)
    acabsl.speedfade(6,3,0,255,18,251)
    acabsl.speedfade(6,2,30,255,0,302)
    acabsl.speedfade(7,2,30,255,0,302)
    acabsl.speedfade(7,3,30,255,0,302)
    acabsl.speedfade(0,4,78,255,0,377)
    acabsl.speedfade(0,5,78,255,0,377)
    acabsl.speedfade(1,5,78,255,0,377)
    acabsl.speedfade(1,4,120,255,0,503)
    acabsl.speedfade(2,4,120,255,0,503)
    acabsl.speedfade(2,5,120,255,0,503)
    acabsl.speedfade(3,4,168,255,0,755)
    acabsl.speedfade(3,5,168,255,0,755)
    acabsl.speedfade(4,4,168,255,0,755)
    acabsl.speedfade(4,5,168,255,0,755)
    acabsl.speedfade(5,4,216,255,0,1000)
    acabsl.speedfade(5,5,216,255,0,1000)
    acabsl.speedfade(6,4,216,255,0,1000)
    acabsl.speedfade(7,4,255,42,0,1000)
    acabsl.speedfade(6,5,255,42,0,1000)
    acabsl.speedfade(7,5,255,42,0,1000)
    time.sleep(0.3)
    acabsl.speedfade(5,4,255,90,0,1000)
    acabsl.speedfade(5,5,255,90,0,1000)
    acabsl.speedfade(6,4,255,90,0,1000)
    acabsl.speedfade(7,4,0,78,255,107)
    acabsl.speedfade(6,5,0,78,255,107)
    acabsl.speedfade(7,5,0,78,255,107)
    time.sleep(0.3)
    acabsl.speedfade(3,4,255,138,0,1000)
    acabsl.speedfade(3,5,255,138,0,1000)
    acabsl.speedfade(4,4,255,138,0,1000)
    acabsl.speedfade(4,5,255,138,0,1000)
    acabsl.speedfade(5,4,0,78,255,116)
    acabsl.speedfade(5,5,0,78,255,116)
    acabsl.speedfade(6,4,0,78,255,116)
    time.sleep(0.3)
    acabsl.speedfade(1,4,255,180,0,1000)
    acabsl.speedfade(2,4,255,180,0,1000)
    acabsl.speedfade(2,5,255,180,0,1000)
    acabsl.speedfade(3,4,0,78,255,125)
    acabsl.speedfade(3,5,0,78,255,125)
    acabsl.speedfade(4,4,0,78,255,125)
    acabsl.speedfade(4,5,0,78,255,125)
    time.sleep(0.3)
    acabsl.speedfade(0,4,255,228,0,1000)
    acabsl.speedfade(0,5,255,228,0,1000)
    acabsl.speedfade(1,5,255,228,0,1000)
    acabsl.speedfade(1,4,0,78,255,137)
    acabsl.speedfade(2,4,0,78,255,137)
    acabsl.speedfade(2,5,0,78,255,137)
    time.sleep(0.3)
    acabsl.speedfade(6,2,234,255,0,1000)
    acabsl.speedfade(7,2,234,255,0,1000)
    acabsl.speedfade(7,3,234,255,0,1000)
    acabsl.speedfade(0,4,0,78,255,151)
    acabsl.speedfade(0,5,0,78,255,151)
    acabsl.speedfade(1,5,0,78,255,151)
    time.sleep(0.3)
    acabsl.speedfade(5,2,192,255,0,1000)
    acabsl.speedfade(5,3,192,255,0,1000)
    acabsl.speedfade(6,3,192,255,0,1000)
    acabsl.speedfade(6,2,0,78,255,167)
    acabsl.speedfade(7,2,0,78,255,167)
    acabsl.speedfade(7,3,0,78,255,167)
    time.sleep(0.3)
    acabsl.speedfade(3,2,144,255,0,1000)
    acabsl.speedfade(3,3,144,255,0,1000)
    acabsl.speedfade(4,2,144,255,0,1000)
    acabsl.speedfade(4,3,144,255,0,1000)
    acabsl.speedfade(5,2,0,78,255,188)
    acabsl.speedfade(5,3,0,78,255,188)
    acabsl.speedfade(6,3,0,78,255,188)
    time.sleep(0.3)
    acabsl.speedfade(1,3,96,255,0,1000)
    acabsl.speedfade(2,2,96,255,0,1000)
    acabsl.speedfade(2,3,96,255,0,1000)
    acabsl.speedfade(3,2,0,78,255,215)
    acabsl.speedfade(3,3,0,78,255,215)
    acabsl.speedfade(4,2,0,78,255,215)
    acabsl.speedfade(4,3,0,78,255,215)
    time.sleep(0.3)
    acabsl.speedfade(0,2,54,255,0,1000)
    acabsl.speedfade(0,3,54,255,0,1000)
    acabsl.speedfade(1,2,54,255,0,1000)
    acabsl.speedfade(1,3,0,78,255,251)
    acabsl.speedfade(2,2,0,78,255,251)
    acabsl.speedfade(2,3,0,78,255,251)
    time.sleep(0.3)
    acabsl.speedfade(6,0,6,255,0,1000)
    acabsl.speedfade(7,0,6,255,0,1000)
    acabsl.speedfade(7,1,6,255,0,1000)
    acabsl.speedfade(0,2,0,78,255,302)
    acabsl.speedfade(0,3,0,78,255,302)
    acabsl.speedfade(1,2,0,78,255,302)
    time.sleep(0.3)
    acabsl.speedfade(5,0,0,255,42,1000)
    acabsl.speedfade(5,1,0,255,42,1000)
    acabsl.speedfade(6,1,0,255,42,1000)
    acabsl.speedfade(6,0,0,78,255,377)
    acabsl.speedfade(7,0,0,78,255,377)
    acabsl.speedfade(7,1,0,78,255,377)
    time.sleep(0.3)
    acabsl.speedfade(3,0,0,255,84,1000)
    acabsl.speedfade(3,1,0,255,84,1000)
    acabsl.speedfade(4,0,0,255,84,1000)
    acabsl.speedfade(4,1,0,255,84,1000)
    acabsl.speedfade(5,0,0,78,255,503)
    acabsl.speedfade(5,1,0,78,255,503)
    acabsl.speedfade(6,1,0,78,255,503)
    time.sleep(0.3)
    acabsl.speedfade(1,1,0,255,132,1000)
    acabsl.speedfade(2,0,0,255,132,1000)
    acabsl.speedfade(2,1,0,255,132,1000)
    acabsl.speedfade(3,0,0,78,255,755)
    acabsl.speedfade(3,1,0,78,255,755)
    acabsl.speedfade(4,0,0,78,255,755)
    acabsl.speedfade(4,1,0,78,255,755)
    time.sleep(0.3)
    acabsl.speedfade(0,0,0,255,180,1000)
    acabsl.speedfade(0,1,0,255,180,1000)
    acabsl.speedfade(1,0,0,255,180,1000)
    acabsl.speedfade(1,1,0,78,255,1000)
    acabsl.speedfade(2,0,0,78,255,1000)
    acabsl.speedfade(2,1,0,78,255,1000)
    time.sleep(0.3)