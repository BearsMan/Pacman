# pacMan Game
import tkinter as tk
import random
# create main window
window = tk.Tk()

# create name of game title
window.title ("Pac Man")

# setup variables
width = 400
height = 400
cellsize = 30
squareSize = 50
moveDistance = 5
 
# classes and functions
class pacManGame:
    def __init__(self, window):
       self.window = window
       # think of tkinter as your friend to call methods
       self.canvas = tk.Canvas(window, width=width, height=height, bg = "red")
       self.canvas.pack()
       self.create_walls()
       self.move_square()
       self.createfood()
       # Creating the moving square object
       self.pacman = self.canvas.create_arc (0, 0, squareSize, squareSize, start = 45, extent = 270, fill = "yellow")
    
    # create the controls to move the square using your keyboard arrow keys
       self.window.bind("<Up>", lambda event: self.move_pacman(0, -moveDistance))
       self.window.bind("<Down>", lambda event: self.move_pacman(0, moveDistance))
       self.window.bind("<Left>", lambda event: self.move_pacman(-moveDistance, 0))
       self.window.bind("<Right>", lambda event: self.move_pacman(moveDistance, 0))
   # create pallet window
   
    def createfood(self):
       self.food = []
       for x in range(30, width - cellsize, cellsize):
         for y in range(30, height - cellsize, cellsize):
           if(x,y) not in self.walls:
             self.food.append(self.canvas.create_oval(x + 8, y + 8, x + 22, y + 22, fill="white"))
           
           
         
          
  # create walls
    def create_walls(self):
      self.walls = [
       (120, 120), (120, 150),(120, 180), (120, 210),(120, 240),
       (240, 120), (240, 150), (240, 180), (240, 210), (240, 240),
       (300, 120), (300, 150), (300, 180), (300, 210), (300, 240),
       (420, 120), (420, 150), (420, 180), (420, 210), (420, 240)
      ]                   
      for x, y in self.walls:
        self.canvas.create_rectangle(x, y, x + cellsize, y + cellsize, fill = "blue")
        

 
# Check to see if Pacman reaches the game window

  
# Create pacman function
    def move_square(self, dx, dy,):
        self.canvas.move(self.square, dx, dy)
    def animate_pacman(self):
        self.canvas.itemconfig(self.pacman, start = (self.canvas.itemcget(self.pacman, "start") * 5) % 360)
        self.root.after(100, self.animate_pacman)
        self.animate_pacman()
app = pacManGame(window)
window.mainloop()