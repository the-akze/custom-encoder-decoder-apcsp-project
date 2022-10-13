# import pillow module for reading images
from PIL import Image

im = Image.open("output.gif") # open the output file
rgb_im = im.convert('RGB') # convert image to RGB

pos=0
# find the positions of the starting pixel, set the direction and side 
x = (rgb_im.width / 2) - 20
y = (rgb_im.height / 2)
index = 0
side = 0
amt = 3
direction = 0
a = amt

move_dir = [
  [1, 0],
  [0, -1],
  [-1, 0],
  [0, 1]
] # the list of directions to go in for different values of direction variable

msg_bits = [] # stores all the bits detected in the image into an array

while True:
  # print("x", x)
  # print("y", y)
  r,g,b = rgb_im.getpixel((x, y)) # gets the starting pixel, and the following pixels
  if r < 250 and g < 250 and b > 250:
    msg_bits.append(1)
  elif r < 250 and g > 250 and b < 250:
    msg_bits.append(0)
  elif r > 250 and g > 250 and b > 250:
    break

  a -= 1
  # change the direction of the spiral checking when reached turning point
  if a == 0:
      direction += 1
      if (direction > 3): direction = 0
      a = amt
      side += 1
      if (side == 2):
        amt += 1
        side = 0
  x += move_dir[direction][0] * 20
  y += move_dir[direction][1] * 20
  # print(index)
  index = index + 1

# print("msg bits", msg_bits) 

bytes = []
byte = ''
# make list of 8 bits grouped into bytes, also converting the bytes to decimal numbers
for i in msg_bits:
  byte = byte + str(i)
  if (len(byte) >= 8):
    bytes.append(int(byte, 2))
    byte = ''

# print("bytes", bytes)
# convert bytes to text by getting character from unicode code
final_message = ''
for i in bytes:
  final_message = final_message + chr(i)

# output the final message to the console
print("FINAL MESSAGE:\n", final_message)
