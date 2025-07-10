import tkinter as tk

root = tk.Tk()
root.title("Test Tkinter")
root.geometry("300x150")
label = tk.Label(root, text="Fenêtre test")
label.pack(pady=20)
root.mainloop()
