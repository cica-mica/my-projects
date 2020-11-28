import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Fashion Couture')
root.resizable(False, False)

background = tk.Label(root, bg = '#D9C0E9')

my_frame = tk.LabelFrame(background, bg = '#173667', bd = 3, highlightthickness = 10)

image1 = ImageTk.PhotoImage(Image.open('C:/Users/Korisnik/Documents/uvod_u_programiranje/predavanje-04/images/IMG_20190924_095956.jpg'))
image2 = ImageTk.PhotoImage(Image.open('C:/Users/Korisnik/Documents/uvod_u_programiranje/predavanje-04/images/IMG-0ad45cb69ad5d2d25666041bc3c0c1fb-V.jpg'))
image3 = ImageTk.PhotoImage(Image.open('C:/Users/Korisnik/Documents/uvod_u_programiranje/predavanje-04/images/IMG-0f5dec5b650122e01ccb581e5d116a96-V.jpg'))
image4 = ImageTk.PhotoImage(Image.open('C:/Users/Korisnik/Documents/uvod_u_programiranje/predavanje-04/images/IMG-1bf99cf349c0d4960b2c89a17bacf81f-V.jpg'))
image5 = ImageTk.PhotoImage(Image.open('C:/Users/Korisnik/Documents/uvod_u_programiranje/predavanje-04/images/IMG-a60610cf791627af96168212380ac2b5-V.jpg'))

images_list = [image1,image2, image3, image4, image5]

status = tk.Label(background, text = 'Image 1 of '+ str(len(images_list)), bg = '#4C2366', fg = '#ffffff', font = 'Monospaced', bd = 1, relief = tk.SUNKEN, anchor = tk.E)

label_image = tk.Label(my_frame, image = image1)

def forward(number):
    global label_image
    global back_button
    global forward_button
    global status

    label_image.grid_forget()
    status.grid_forget()

    label_image = tk.Label(my_frame ,image = images_list[number - 1])
    forward_button = tk.Button(background, text = 'Next', command = lambda: forward(number + 1))
    back_button = tk.Button(background, text = 'Back', command = lambda:back(number - 1))
    
    if number == len(images_list): 
        
        forward_button = tk.Button(background, text = 'Next', state = tk.DISABLED)
    
    my_frame.grid(padx = 50, pady = 5, rowspan = 3)
    label_image.grid(row = 0, column = 0, rowspan = 3)
    forward_button.grid(row = 1, column = 1)
    back_button.grid(row = 2, column = 1)

    status = tk.Label(background, text = 'Image ' + str(number) + ' of '+ str(len(images_list)), bd = 1,bg = '#4C2366', fg = '#ffffff', relief = tk.SUNKEN, anchor = tk.E)
    status.grid(row = 3, column = 0, columnspan = 3, sticky = tk.E + tk.W)

def back(number):
    global back_button
    global forward_button
    global label_image
    global status

    label_image.grid_forget()
    status.grid_forget()

    label_image = tk.Label(my_frame ,image = images_list[number - 1])
    forward_button = tk.Button(background, text = 'Next', command = lambda: forward(number + 1))
    back_button = tk.Button(background, text = 'Back', command = lambda: back(number - 1))
    
    if number == 1: 
        back_button = tk.Button(background, text = 'Back', state = tk.DISABLED)
    
    my_frame.grid(padx = 50, pady = 5, rowspan = 3)
    label_image.grid(row = 0, column = 0, rowspan = 3)
    forward_button.grid(row = 1, column = 1)
    back_button.grid(row = 2, column = 1)

    status = tk.Label(background, text = 'Image ' + str(number) + ' of ' + str(len(images_list)), bd = 1, bg = '#4C2366', fg = '#ffffff', font = 'Monospaced', anchor =tk.E)
    status.grid(row = 3, column = 0, columnspan = 3, sticky = tk.E + tk.W)


exit_button = tk.Button(background, text = 'Exit Program', bg = '#BA2020', command = root.quit)
forward_button = tk.Button(background, text = 'Next', fg = '#176736', command = lambda: forward(2))
back_button = tk.Button(background, text = 'Back', fg = '#176736', state = tk.DISABLED, disabledforeground = '#A2FB98', command = back)


background.grid()
my_frame.grid(padx = 30, pady = 35, rowspan = 3)
label_image.grid(row = 0, column = 0, rowspan = 3)
exit_button.grid(row = 0, column = 1, pady = 5)
forward_button.grid(row = 1, column = 1)
back_button.grid(row = 2, column = 1)
status.grid(row = 3, column = 0, columnspan = 3, sticky = tk.E+ tk.W)

root.mainloop()