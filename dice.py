import tkinter as tk

# Layout
window = tk.Tk()
window.title('Dice simulator')
window.rowconfigure([0, 1], weight=1, minsize=100)
window.columnconfigure(0, weight=1, minsize=250)

btn_roll = tk.Button(master=window, text='Roll')
lbl_dvalue = tk.Label(master=window, text='1')

btn_roll.grid(row=0, column=0, sticky='ewns')
lbl_dvalue.grid(row=1, column=0, sticky='ew')

window.mainloop()

