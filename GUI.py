from tkinter import *
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

class GUI :
    def __init__(self,master):
        master.geometry(str(screensize[0])+"x"+str(screensize[1]))
        self.canvas = Canvas(master)
        root.attributes('-transparentcolor','#f0f0f0')
        root.overrideredirect(True)
        #self.Refresh = Button(root, text = "Refresh Status" , fg = "black", command = self.refresh)
        root.bind("<Up>", self.up)
        root.bind("<Down>", self.down)
        root.bind("<Right>", self.right)
        root.bind("<Left>", self.left)

        self.photo = PhotoImage(file="DVSPypeWkAErqkB-removebg-preview.png")
        self.picture = self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        label = Label(image=self.photo)
        label.image = self.photo # keep a reference!
        label.pack()

    def up(self, event):
        self.canvas.move(self.picture,0,-10)
    def down(self, event):
        self.canvas.move(self.picture,0,10)
    def right(self, event):
        self.canvas.move(self.picture,10,0)
    def left(self, event):
        self.canvas.move(self.picture,-10,0)

root = Tk()
gui = GUI(root)
root.mainloop()
