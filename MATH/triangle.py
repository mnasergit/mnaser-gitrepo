import tkinter as tk

def draw_triangle(canvas):
    height = 200
    width = 400
    for i in range(height):
        #canvas.create_line(width/2 - i, height - i, width/2 + i, height - i)
        canvas.create_line(width/2 - i, i, width/2 + i, i, fill='green')

root = tk.Tk()
root.title("Triangle GUI")

canvas = tk.Canvas(root, height=200, width=400)
canvas.pack()

draw_triangle(canvas)

root.mainloop()