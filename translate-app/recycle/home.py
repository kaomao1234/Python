import tkinter as tk

class Overlay(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.attributes("-topmost", True)
        self.overrideredirect(True)
        self.geometry("1920x1080")
        
        self.drag_start = None
        self.drag_rect = None
        self.show_rect = False
        self.transparency_enabled = False

        self.transparent_button = tk.Button(self, text="Toggle Transparency", command=self.toggle_transparency)
        self.transparent_button.place(x=10, y=10, width=150, height=30)

        self.canvas = tk.Canvas(self, width=1920, height=1080)
        self.canvas.pack()

        self.timer = self.after(500, self.toggle_rect)

    def toggle_rect(self):
        self.show_rect = not self.show_rect
        self.update_canvas()

    def toggle_transparency(self):
        self.transparency_enabled = not self.transparency_enabled
        self.attributes("-alpha", 0.5 if self.transparency_enabled else 1.0)

    def update_canvas(self):
        self.canvas.delete("all")
        
        if self.transparency_enabled:
            self.canvas.create_rectangle(0, 0, 1920, 1080, outline='', fill='')
        else:
            self.canvas.create_rectangle(0, 0, 1920, 1080, outline='', fill='white')

        if self.show_rect and self.drag_rect is not None:
            self.canvas.create_rectangle(*self.drag_rect, outline='red')

    def mouse_press(self, event):
        self.drag_start = event.x, event.y
        self.drag_rect = None
        self.update_canvas()

    def mouse_move(self, event):
        if self.drag_start is not None:
            self.drag_rect = (min(self.drag_start[0], event.x), min(self.drag_start[1], event.y),
                              abs(self.drag_start[0] - event.x), abs(self.drag_start[1] - event.y))
            self.update_canvas()

    def mouse_release(self, event):
        self.drag_rect = (min(self.drag_start[0], event.x), min(self.drag_start[1], event.y),
                          abs(self.drag_start[0] - event.x), abs(self.drag_start[1] - event.y))
        self.drag_start = None
        self.update_canvas()

if __name__ == '__main__':
    app = tk.Tk()
    overlay = Overlay()
    app.mainloop()
