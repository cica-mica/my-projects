"""this memory_game is my first project for the course"""

# I imported tkinter, PIL and random
import tkinter as tk
import random
from PIL import Image, ImageTk

root = tk.Tk(screenName= 'Memory')
root.title('Memory Game')
root.resizable(False, False)

# Images that I used for cards in the game, there are two cards with the same image on it
image1 = ImageTk.PhotoImage(Image.open('./images/red_flower.png'))
image2 = ImageTk.PhotoImage(Image.open('./images/pumpkin.png'))
image3 = ImageTk.PhotoImage(Image.open('./images/butterfly.jpg'))
image4 = ImageTk.PhotoImage(Image.open('./images/squirrel.png'))
image5 = ImageTk.PhotoImage(Image.open('./images/islamic_mosque.png'))
image6 = ImageTk.PhotoImage(Image.open('./images/39091.jpg'))
image7 = ImageTk.PhotoImage(Image.open('./images/camera.png'))
image8 = ImageTk.PhotoImage(Image.open('./images/snowflake.png'))

# Background is the image on the wrongside of every card
background = ImageTk.PhotoImage(Image.open('./images/snake.png'))

# The list of images (16 elements) used as cards
images_list_1 = [image1, image2, image3, image4, image5, image6, image7, image8]
IMAGES_LIST = images_list_1 + images_list_1
random.shuffle(IMAGES_LIST)

# I created these variables below because they will need me in the folded_card function
PICKS_LIST = []
COUNTER = 0
DISABLED_BUTTONS = []

GAME_OVER = tk.Label(root, text = ' ', font = ('Helvetica', '20','bold'),\
    fg = '#163A1F')

SCORE = tk.Label(root, text = 'Matched pairs: ' + str(len(DISABLED_BUTTONS)//2),\
     font = ('Helvetica', '14','bold'), fg = '#163A1F')

def restart():
    """
    this function restarts the game
    """
    global COUNTER, PICKS_LIST, DISABLED_BUTTONS, IMAGES_LIST
    #RESTART_GAME.config(state = 'enabled')
    COUNTER = 0
    PICKS_LIST = []
    random.shuffle(IMAGES_LIST)
    for card in DISABLED_BUTTONS:
        card.config(image = background)
        card.config(state = 'active')
    DISABLED_BUTTONS = []

# This is the command that allows cards to turn over, turn back, freeze when the images are the same
def folded_card(button, number):
    """
    this function turns the cards upside-down
    """
    global IMAGES_LIST, PICKS_LIST, COUNTER, DISABLED_BUTTONS, GAME_OVER, RESTART_GAME, SCORE
    if COUNTER < 2:

        button['image'] = IMAGES_LIST[number]
        PICKS_LIST.append(button)
        COUNTER +=1
    # when counter = 2 is the perfect time to check if the cards match
    else:
        if PICKS_LIST[0] == PICKS_LIST[1]:
            COUNTER -=1
            PICKS_LIST.remove(PICKS_LIST[1])
            GAME_OVER.config(text = 'Oooops')
        else:
            if PICKS_LIST[0]['image'] == PICKS_LIST[1]['image']:
                for but in PICKS_LIST:
                    but['state'] = 'disabled'
                    DISABLED_BUTTONS.append(but)
                    SCORE.config(text = 'Matched pairs: ' + str(len(DISABLED_BUTTONS)//2))

                    if len(DISABLED_BUTTONS) == 16:
                        GAME_OVER.config(text = 'GAME OVER!')
                    else:
                        GAME_OVER.config(text = 'MATCH!')
                COUNTER = 0
                PICKS_LIST = []
            else:
                for but in PICKS_LIST:
                    but['image'] = background
                COUNTER = 0
                PICKS_LIST = []
                GAME_OVER.config(text = 'Wrong Match! Try again.')

# there are 16 cards turned upside-down
card1 = tk.Button(root, bg = '#AEE7BA',image = background,command = lambda:folded_card(card1, 0))
card2 = tk.Button(root, bg = '#AEE7BA',image = background,command = lambda:folded_card(card2, 1))
card3 = tk.Button(root, bg = '#AEE7BA',image = background,command = lambda:folded_card(card3, 2))
card4 = tk.Button(root, bg = '#AEE7BA',image = background,command = lambda:folded_card(card4, 3))
card5 = tk.Button(root, bg = '#AEE7BA',image = background,command = lambda:folded_card(card5, 4))
card6 = tk.Button(root, bg = '#AEE7BA',image = background,command = lambda:folded_card(card6, 5))
card7 = tk.Button(root, bg = '#AEE7BA',image = background,command = lambda:folded_card(card7, 6))
card8 = tk.Button(root, bg = '#AEE7BA',image = background,command = lambda:folded_card(card8, 7))
card9 = tk.Button(root, bg = '#AEE7BA',image = background,command = lambda:folded_card(card9, 8))
card10 = tk.Button(root, bg = '#AEE7BA',image = background,command = lambda:folded_card(card10, 9))
card11 = tk.Button(root, bg = '#AEE7BA',image = background,command = lambda:folded_card(card11, 10))
card12 = tk.Button(root, bg = '#AEE7BA',image = background,command = lambda:folded_card(card12, 11))
card13 = tk.Button(root, bg = '#AEE7BA',image = background,command = lambda:folded_card(card13, 12))
card14 = tk.Button(root, bg = '#AEE7BA',image = background,command = lambda:folded_card(card14, 13))
card15 = tk.Button(root, bg = '#AEE7BA',image = background,command = lambda:folded_card(card15, 14))
card16 = tk.Button(root, bg = '#AEE7BA',image = background,command = lambda:folded_card(card16, 15))

# This is the button that, besides X, allows you to quit the game
exit_game = tk.Button(root, text = 'EXIT', font = ('Helmetica', '16', 'bold'),\
    fg = '#163A1F', bg = '#9FAFA3', command = root.destroy)
RESTART_GAME = tk.Button(root, text = 'RESTART', font = ('Helvetica', '16', 'bold'),\
    fg = '#163A1F', bg = '#9FAFA3', relief = 'ridge', command = restart)

card1.grid(row = 0, column = 0)
card2.grid(row = 0, column = 1)
card3.grid(row = 0, column = 2)
card4.grid(row = 0, column = 3)
card5.grid(row = 1, column = 0)
card6.grid(row = 1, column = 1)
card7.grid(row = 1, column = 2)
card8.grid(row = 1, column = 3)
card9.grid(row = 2, column = 0)
card10.grid(row = 2, column = 1)
card11.grid(row = 2, column = 2)
card12.grid(row = 2, column = 3)
card13.grid(row = 3, column = 0)
card14.grid(row = 3, column = 1)
card15.grid(row = 3, column = 2)
card16.grid(row = 3, column = 3)

GAME_OVER.grid(row = 4, column = 0, padx = 8, pady = 20, columnspan = 4)

SCORE.grid(row = 5, column = 2, pady = 15, columnspan = 2)

exit_game.grid(row = 5, column = 0, columnspan = 2, padx = 8, pady = 13, sticky = tk.W)

RESTART_GAME.grid(row = 6, column = 0, pady = 10, padx = 8)

root.mainloop()
