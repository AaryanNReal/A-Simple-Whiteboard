from tkinter import *
from tkinter import ttk

from tkinter import filedialog


class WhiteboardApp:
    def __init__(self, hroot):
        self.hroot = hroot
        self.hroot.title("Simple Whiteboard")
        self.draw_mode = True

        self.canvas = Canvas(self.hroot, bg="white", width=600, height=400)
        self.canvas.pack(expand=YES, fill=BOTH)

        self.canvas.bind("<B1-Motion>", self.draw)

        self.clear_button = Button(self.hroot, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack(padx=10, pady=10, side=LEFT)

        self.draw_button = Button(self.hroot, text="DRAW", command=self.draw_mode)
        self.draw_button.pack(padx=10, pady=10, side=RIGHT)


        self.size_entry = Entry(self.hroot)
        self.size_entry.pack(side=RIGHT)
        self.size_button = Button(self.hroot, text="Enter Size", command=self.set_size)
        self.size_button.pack(side=RIGHT)

        self.color_dropdown = ttk.Combobox(self.hroot, values=["black", "red", "green", "blue", "yellow", "white"],
                                           state="readonly")
        self.color_dropdown.pack(side=LEFT)
        self.color_dropdown.set("black")  # Set default color

        self.export_button = Button(self.hroot, text="Export as Image", command=self.export_image)
        self.export_button.pack(padx=10, pady=10, side=BOTTOM)

    def draw_mode(self):
        self.draw_mode = True

    def erase_mode(self):
        self.draw_mode = False

    def draw(self, event):
        x, y = event.x, event.y
        try:
            size = int(self.size_entry.get())
            color = self.color_dropdown.get()
            if self.draw_mode:
                self.canvas.create_oval(x - size, y - size, x + size, y + size, fill=color,outline=color)
            else:
                self.canvas.create_oval(x - size, y - size, x + size, y + size, fill=self.canvas["bg"],
                                        outline=self.canvas["bg"])
        except ValueError:
            pass

    def clear_canvas(self):
        self.canvas.delete("all")

    def set_size(self):
        pass

    def export_image(self):
        filename = filedialog.asksaveasfilename(defaultextension=".png",
                                                filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
        if filename:
            x0 = self.hroot.winfo_rootx() + self.canvas.winfo_x()
            y0 = self.hroot.winfo_rooty() + self.canvas.winfo_y()
            x1 = x0 + self.canvas.winfo_width()
            y1 = y0 + self.canvas.winfo_height()
            self.canvas.postscript(file=filename, colormode="color", x=x0, y=y0, width=x1, height=y1)


root = Tk()
app = WhiteboardApp(root)
root.mainloop()
