# Import modules 
import turtle as trtl
from PIL import Image
import mss
import platform
import time

message = "made by akshat & yashmit"
# ^ Length limit 25 characters.

if (len(message) > 25): # this is because we saw the decode.py didn't decode characters after the 25th character correctly
  print("NOTE: After 25 characters, the characters don't decode correctly in decode.py, so try to limit the message to 25 characters!")

characters_as_ints = []
for cha in message:
    # convert letters to their unicode number code
    characters_as_ints.append(ord(cha))
print(characters_as_ints)

characters_as_bits = []
for integ in characters_as_ints:
    # convert the ints to bytes
    characters_as_bits.append('{0:08b}'.format(integ))
print(characters_as_bits)

bits_as_ints = []
for index in range(0, len(characters_as_bits)):
    for bit in characters_as_bits[index]:
        bits_as_ints.append(bit)
print(bits_as_ints)

# initialization of turtle, setup and draw the first shape
screen = trtl.getscreen()
painter = trtl.Turtle()
painter.speed(0)
print(screen.window_width(), " x ", screen.window_height())
painter.penup()
painter.goto(0, 0)
painter.shape("square")
painter.goto(-20, 0)
painter.color("red")
painter.stamp()
painter.goto(-20, 0)
painter.color("blue")

# draw the encoded message on the screen as a spiral of blue and green squares by looping through the 0's and 1's and drawing either blue or green based on that
message_length = len(bits_as_ints)
index = 0
side = 0
amt = 3
a = amt
while index < message_length:
    if bits_as_ints[index] == '1':
        painter.color("#0000ff")
        painter.stamp()
    else:
        painter.color("#00ff00")
        painter.stamp()
    a -= 1
    if a == 0:
        painter.left(90)
        a = amt
        side += 1
        if (side == 2):
            amt += 1
            side = 0
    painter.forward(21)
    index = index + 1

screen = painter.getscreen()
root = trtl.getcanvas().winfo_toplevel()


def create_image(widget):
    with mss.mss() as sct:
        # mon is the monitor number of the primary display. Change if capturing incorrect display.
        sct.shot(mon=1, output='fullscreen.gif')

        x = root.winfo_rootx()
        y = root.winfo_rooty()

        x1 = x+widget.window_width()
        y1 = y+widget.window_height()

        im = Image.open("fullscreen.gif")
        bounds = x, y, x1, y1
        # Retina displays require a coefficient of 2 for pixel numbers
        if platform.system() == 'Darwin':
            bounds = 2*x, 2*y, 2*x1, 2*y1
        print("Turtle bounding box: ", bounds)
        im = im.crop(box=bounds)
        im.save("output.gif")


# save the image in the folder
create_image(screen)

# wait a second so you can see the final image for an extra second before it automatically closes
time.sleep(1)
