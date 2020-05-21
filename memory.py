# implementation of card game - Memory

import simpleguitk as simplegui
import random

# helper function to initialize globals
def new_game():
    global numbers, exposed, turns, paired, count
    numbers = [x//2 for x in range(16)]
    random.shuffle(numbers)
    exposed = [False for _ in range(16)]
    turns = 0
    label.set_text("Turns = "+str(turns))
    paired = [False for _ in range(16)]
    count = 0

     
# define event handlers
def mouseclick(pos):
    global exposed, turns, prev, count
    if exposed[pos[0]//50]==True:
        return
    if count==0:
        count = 1
        exposed[pos[0]//50]=True
        prev = pos[0]//50
    elif count==1:
        count = 2
        exposed[pos[0]//50]=True
        turns += 1
        label.set_text("Turns = "+str(turns))
        if (numbers[prev]==numbers[pos[0]//50]):
            paired[prev] = True
            paired[pos[0]//50] = True
    else:
        count = 1
        prev = pos[0]//50
        exposed = list(paired)
        exposed[pos[0]//50]=True
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(numbers)):
        if (exposed[i]):
            canvas.draw_text(str(numbers[i]), (12+50*i, 70), 48, 'white')
        else:
            canvas.draw_polygon(((50*i, 0), (50*(i+1), 0), (50*(i+1), 100), (50*i, 100)), 1, 'black','green')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
