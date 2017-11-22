from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)
temperature = round(sense.get_temperature(), 1)
sense.show_message(str(temperature))

# Colours
w = [255, 255, 255]
b = [0, 0, 0]
r = [255, 0, 0]
g = [0, 255, 0]
bl = blue = [0, 0, 255]
br = brown = [124, 74, 0]
pi = pink = [232, 66, 244]
pu = purple = [169, 65, 244]
ye = yellow = [232, 232, 32]

sense.show_message("Write your message here", scroll_speed=0.1)
sleep(1)

picture = [
  w, w, w, b, b, w, w, w,
  w, w, b, r, r, b, w, w,
  w, b, r, r, r, r, b, w,
  b, r, r, b, b, r, r, b,
  b, w, w, b, b, w, w, b,
  w, b, w, w, w, w, b, w,
  w, w, b, w, w, b, w, w,
  w, w, w, b, b, w, w, w,
]

sense.set_pixels(picture)
