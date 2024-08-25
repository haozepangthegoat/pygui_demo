from uri_template import expand

c20 = '#141F52'
hk45 = '#1DC9A4'
sg55 = '#F97A1F'


import tkinter as tk

window = tk.Tk()
window.columnconfigure(0, weight=1, minsize=250)
window.rowconfigure([0, 1], weight=1, minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0)

label2 = tk.Label(text="B")
label2.grid(row=1, column=0)

window.mainloop()