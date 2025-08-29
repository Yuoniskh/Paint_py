from tkinter import * 
from tkinter import messagebox as mb
root=Tk("paint")
root.title("paint")
root.geometry("660x560+300+100")
def paint(event,color,size):
    x1,y1=(event.x-4*size),(event.y-4*size)
    x2,y2=(event.x+4*size),(event.y+4*size)
    paint_space.create_oval(x1,y1,x2,y2,fill=color,outline="")
def red():
    global color
    color = "#F00"

def blue():
    global color
    color = "#00F"

def yellow():
    global color
    color = "#FF0"

def green():
    global color
    color="#0F0"

def white():
    global color
    color = "#FFF"

def black():
    global color
    color = "#000"

def clear_canvas():
    paint_space.delete("all")
    paint_space.create_rectangle(2,2,550,550)

def call_block():
    if mb.askyesno("verify close","if you want close this program press yes!!"):
        root.quit()
        mb.showinfo("yesss","you have cancelled this program . succesfuly!")
    else:
        mb.showinfo("noooo","quit has been cancelled")

color="#000"
paint_space=Canvas(root,height=550,width=550,background="#FFF")    
paint_space.place(x=100,y=0)
paint_space.create_rectangle(2,2,550,550)
paint_space.bind('<B1-Motion>',lambda e:paint(e,color,size_br.get()))
frame=Frame(root,height=300,width=50)
frame.place(x=0,y=10)
red=Button(frame,height=2, width=8,command=red,background="red")
red.pack()
blue=Button(frame,height=2, width=8,command=blue,background="blue")
blue.pack()
yellow=Button(frame,height=2, width=8,command=yellow,background="yellow")
yellow.pack()
green=Button(frame,height=2, width=8,command=green,background="green")
green.pack()
white=Button(frame,height=2, width=8,command=white,background="white")
white.pack()
black=Button(frame,height=2, width=8,command=black,background="black")
black.pack()
clear_btn = Button(frame, height=2, width=8, text="Clear", command=clear_canvas, background="gray")
clear_btn.pack()
size_br=Scale(frame,from_=1,to=5,orient="horizontal")
size_br.pack()
exit_btn = Button(frame, height=2, width=8, text="X", command=call_block, background="#F02")
exit_btn.pack()


root.mainloop()