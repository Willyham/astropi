from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)
temp = round(sense.get_temperature(), 1)
sense.show_message(str(temp))

sense.show_message("Throwing pokeball..", scroll_speed=0.05)
sleep(2)

b = [0,0,0]
w = [255,255,255]
r = [255,0,0]

top = [
  w,w,w,b,b,w,w,w,
  w,w,b,r,r,b,w,w,
  w,b,r,r,r,r,b,w,
  b,r,r,b,b,r,r,b,
  b,w,w,b,b,w,w,b,
  w,b,w,w,w,w,b,w,
  w,w,b,w,w,b,w,w,
  w,w,w,b,b,w,w,w,
]

left = [
  w,w,w,b,b,w,w,w,
  w,w,b,r,w,b,w,w,
  w,b,r,r,w,w,b,w,
  b,r,r,b,b,w,w,b,
  b,r,r,b,b,w,w,b,
  w,b,r,r,w,w,b,w,
  w,w,b,r,w,b,w,w,
  w,w,w,b,b,w,w,w,
]

bottom = [
  w,w,w,b,b,w,w,w,
  w,w,b,w,w,b,w,w,
  w,b,w,w,w,w,b,w,
  b,w,w,b,b,w,w,b,
  b,w,w,b,b,w,w,b,
  w,b,r,r,r,r,b,w,
  w,w,b,r,r,b,w,w,
  w,w,w,b,b,w,w,w,
]

right = [
  w,w,w,b,b,w,w,w,
  w,w,b,w,w,b,w,w,
  w,b,w,w,w,r,b,w,
  b,w,w,b,b,r,r,b,
  b,w,w,b,b,r,r,b,
  w,b,w,w,w,r,b,w,
  w,w,b,w,w,b,w,w,
  w,w,w,b,b,w,w,w,
]

pictures = [top, left, bottom, right]

for i in range(1,20):
  sense.set_pixels(pictures[i % 4])
  sleep(0.1)

sense.show_message(".....Caught an Astromon!", scroll_speed=0.05)
