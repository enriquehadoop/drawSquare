#function to draw a triangle
import time
def triangle(size):
  d = "*"
  total = ""
  for x in range(size):
    time.sleep(1)
    print(x*d)
triangle(20)