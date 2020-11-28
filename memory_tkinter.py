# this memory_game is my first project for the course

# I imported tkinter, PIL and random
import tkinter as tk
from PIL import Image, ImageTk
import random

root = tk.Tk(screenName= 'Memory')
root.title('Memory Game')
root.resizable(False, False)

# These are eight images that I used for cards in the game, there are two cards with the same image on it
image1 = ImageTk.PhotoImage(Image.open('C:/Users/Korisnik/Documents/uvod_u_programiranje/predavanje-04/images/—Pngtree—beautiful red poinsettia flower christmas_5566767.png'))
image2 = ImageTk.PhotoImage(Image.open('C:/Users/Korisnik/Documents/uvod_u_programiranje/predavanje-04/images/—Pngtree—happy thanksgiving with pumpkin corn_5512176.png'))
image3 = ImageTk.PhotoImage(Image.open('C:/Users/Korisnik/Documents/uvod_u_programiranje/predavanje-04/images/butterfly.jpg'))
image4 = ImageTk.PhotoImage(Image.open('C:/Users/Korisnik/Documents/uvod_u_programiranje/predavanje-04/images/—Pngtree—cartoon squirrel_1474628.png'))
image5 = ImageTk.PhotoImage(Image.open('C:/Users/Korisnik/Documents/uvod_u_programiranje/predavanje-04/images/—Pngtree—cute yellow flat islamic mosque_5512716.png'))
image6 = ImageTk.PhotoImage(Image.open('C:/Users/Korisnik/Documents/uvod_u_programiranje/predavanje-04/images/39091.jpg'))
image7 = ImageTk.PhotoImage(Image.open('C:/Users/Korisnik/Documents/uvod_u_programiranje/predavanje-04/images/—Pngtree—red vintage camera vector clipart_4236390.png'))
image8 = ImageTk.PhotoImage(Image.open('C:/Users/Korisnik/Documents/uvod_u_programiranje/predavanje-04/images/—Pngtree—winter beautiful symmetrical dark blue_5527848.png'))

# Background is the image on the wrongside of every card
background = ImageTk.PhotoImage(Image.open('C:/Users/Korisnik/Documents/uvod_u_programiranje/predavanje-04/predavanje_9/snake.png'))

# The list of images (16 elements), there are two elements of every image, which are afterwards shuffled
images_list = [image1, image2, image3, image4, image5, image6, image7, image8, image1, image2, image3, image4, image5, image6, image7, image8]
random.shuffle(images_list)

# I created these variables below because they will need me in the folded_card function
picks_list = []
counter = 0
disabled_buttons = []

# this represents some kind of message to a player that says whether the combitation matches or not, or the game is over
game_over = tk.Label(root, text = ' ', font = ('Helvetica', '20','bold'), fg = '#163A1F')

score = tk.Label(root, text = 'Matched pairs: ' + str(len(disabled_buttons)//2), font = ('Helvetica', '14','bold'), fg = '#163A1F')

# This is the command that allows cards to turn over, turn back, freeze when the images are the same
def folded_card(button, number):
    global images_list
    global picks_list
    global counter
    global disabled_buttons
    global game_over
    global score
    
    game_over.grid_forget()
    game_over = tk.Label(root, text = ' ', font = ('Helvetica', '20','bold'), fg = '#163A1F')
    game_over.grid(row = 4, column = 0, pady = 20, columnspan = 4)
    
    # first condition is if the counter is less than two because a player is allowed to turn over only two cards at once
    if counter < 2:

        game_over.grid_forget()
        game_over = tk.Label(root, text = ' ', font = ('Helvetica', '20','bold'), fg = '#163A1F')
        game_over.grid(row = 4, column = 0, pady = 20, columnspan = 4)

        button['image'] = images_list[number]
        picks_list.append(button)
        counter +=1
    
    # when counter = 2 is the perfect time to check if the cards match
    elif counter == 2:
        game_over.grid_forget()
        if picks_list[0] == picks_list[1]:
            counter -=1
            picks_list.remove(picks_list[1])
            game_over = tk.Label(root, text = 'Oooops!', font = ('Helvetica', '20','bold'), fg = '#163A1F')
            game_over.grid(row = 4, column = 0, pady = 20, columnspan = 4)
        else:
            if picks_list[0]['image'] == picks_list[1]['image']:
                for b in picks_list:
                    b['state'] = 'disabled'
                    disabled_buttons.append(b)

                    score = tk.Label(root, text = 'Matched pairs: ' + str(len(disabled_buttons)//2), font = ('Helvetica', '14','bold'), fg = '#163A1F')
                    score.grid(row = 5, column = 2, pady = 15, columnspan = 2)

                    if len(disabled_buttons) == 16:
                        game_over = tk.Label(root, text = 'GAME OVER!', font = ('Helvetica', '20', 'bold'), fg = '#163A1F')
                        game_over.grid(row = 4, column = 0, pady = 20, columnspan = 4)
                    else:
                        game_over = tk.Label(root, text = 'MATCH!', font = ('Helvetica', '20','bold'), fg = '#163A1F')
                        game_over.grid(row = 4, column = 0, pady = 20, columnspan = 4)
                counter = 0
                picks_list = []
            else:
                for b in picks_list:
                    b['image'] = background
                counter = 0
                picks_list = []
                game_over = tk.Label(root, text = 'Wrong Match! Try Again.', font = ('Helvetica', '20','bold'), fg = '#163A1F')
                game_over.grid(row = 4, column = 0, pady = 20, columnspan = 4)
    else:
        for b in picks_list:
           b['image'] = background
        counter = 0
        picks_list = []       

# quit command exits the window
def quit():
    root.destroy()
    
# there are 16 cards turned upside-down
card1 = tk.Button(root, bg = '#AEE7BA',image = background, command = lambda:folded_card(card1, 0))
card2 = tk.Button(root, bg = '#AEE7BA',image = background, command = lambda:folded_card(card2, 1))
card3 = tk.Button(root, bg = '#AEE7BA',image = background, command = lambda:folded_card(card3, 2))
card4 = tk.Button(root, bg = '#AEE7BA',image = background, command = lambda:folded_card(card4, 3))
card5 = tk.Button(root, bg = '#AEE7BA',image = background, command = lambda:folded_card(card5, 4))
card6 = tk.Button(root, bg = '#AEE7BA',image = background, command = lambda:folded_card(card6, 5))
card7 = tk.Button(root, bg = '#AEE7BA',image = background, command = lambda:folded_card(card7, 6))
card8 = tk.Button(root, bg = '#AEE7BA',image = background, command = lambda:folded_card(card8, 7))
card9 = tk.Button(root, bg = '#AEE7BA',image = background, command = lambda:folded_card(card9, 8))
card10 = tk.Button(root, bg = '#AEE7BA',image = background, command = lambda:folded_card(card10, 9))
card11 = tk.Button(root, bg = '#AEE7BA',image = background, command = lambda:folded_card(card11, 10))
card12 = tk.Button(root, bg = '#AEE7BA',image = background, command = lambda:folded_card(card12, 11))
card13 = tk.Button(root, bg = '#AEE7BA',image = background, command = lambda:folded_card(card13, 12))
card14 = tk.Button(root, bg = '#AEE7BA',image = background, command = lambda:folded_card(card14, 13))
card15 = tk.Button(root, bg = '#AEE7BA',image = background, command = lambda:folded_card(card15, 14))
card16 = tk.Button(root, bg = '#AEE7BA',image = background, command = lambda:folded_card(card16, 15))

# This is the button that, besides X, allows you to quit the game
exit_game = tk.Button(root, text = 'EXIT', font = ('Helmetica', '16', 'bold'), fg = '#163A1F', bg = '#9FAFA3', command = quit)

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

game_over.grid(row = 4, column = 0, padx = 8, pady = 20, columnspan = 4)

score.grid(row = 5, column = 2, pady = 15, columnspan = 2)

exit_game.grid(row = 5, column = 0, columnspan = 2, padx = 8, pady = 13, sticky = tk.W)

root.mainloop()