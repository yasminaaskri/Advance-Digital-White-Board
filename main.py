from tkinter import * 
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageTk

current_x =0
current_y =0
color = "black"

def locat_xy(event):
    global current_x , current_y 
    current_x = event.x
    current_y = event.y     

def addline(event):
    global current_x , current_y 
    canvas.create_line(current_x,current_y,event.x,event.y,width=get_current_value(),fill=color,capstyle=ROUND,smooth=TRUE)
    current_x , current_y = event.x , event.y

def new_canvas():   
    canvas.delete("all")
    display_palette()

def show_color(new_color):
    global color
    color = new_color
    

def insertimage():
    global filename 
    global f_image  

    filename= filedialog.askopenfilename(initialdir=os.getcwd(),title="select an image", filetype=(("png files","*.png"),("all files","*.*")))

    f_image =tk.PhotoImage(file=filename)
    my_img=canvas.create_image(180, 50 , image=f_image)
    root.bind("<B3-Motion>",mycallback)

def mycallback(event):
    global f_image
    

    f_image =tk.PhotoImage(file=filename)
    my_img = canvas.create_image(event.x,event.y,image=f_image)


def display_palette():
    id = colors.create_rectangle(10, 10, 30, 30, fill="black")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("black"))

    id = colors.create_rectangle(10, 40, 30, 60, fill="gray")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("gray"))

    id = colors.create_rectangle(10, 70, 30, 90, fill="red")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("red"))

    id = colors.create_rectangle(10, 100, 30, 120, fill="brown")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("brown"))

    id = colors.create_rectangle(10, 130, 30, 150, fill="yellow")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("yellow"))

    id = colors.create_rectangle(10, 160, 30, 180, fill="green")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("green"))

    id = colors.create_rectangle(10, 190, 30, 210, fill="blue")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("blue"))

    id = colors.create_rectangle(10, 220, 30, 240, fill="orange")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("orange"))
    



#colors 
color1="#f2f3f5"

root = Tk()
root.title("WHITE BOARD")
root.geometry("1050x570+150+10")
root.configure(bg=color1)
root.resizable(FALSE,FALSE)

#icon
image_photo= PhotoImage(file="logo.png")
root.iconphoto(False, image_photo)

#sidebar
color_box=PhotoImage(file="color-section.png")
color_section=Label(root,image=color_box,bg=color1)   
color_section.place(x=-200,y=20)

eraser_image=Image.open ("eraser.png")
eraser_image=eraser_image.resize((20,20))
eraser_image= ImageTk.PhotoImage(eraser_image)
eraser=Button(root, image=eraser_image,bg=color1,command=new_canvas)
eraser.place(x=37,y=400)


add_image3 = Image.open("add_image3.png")
add_image3 = add_image3.resize((20, 20))
add_image3 = ImageTk.PhotoImage(add_image3)
add_button = Button(root, image=add_image3, bg=color1 ,command=insertimage)
add_button.place(x=37, y=450)

colors=Canvas(root,bg="#fff",width=34,height=300 , bd=0)
colors.place(x=34,y=77)



#main screen
canvas = Canvas(root, bg='white', width=930, height=500 , cursor="hand2")
canvas.place(x=100,y=20)

canvas.bind("<Button-1>", locat_xy)
canvas.bind("<B1-Motion>", addline)
#slider 
current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_change(value):
    value_label.configure(text=get_current_value())

slider = ttk.Scale(root , from_=0 , to=100 , orient="horizontal" , command=slider_change , variable=current_value)
slider.place(x=37,y=530)

value_label = Label(root, text=get_current_value())
value_label.place(x=37,y=540)


display_palette()

root.mainloop()