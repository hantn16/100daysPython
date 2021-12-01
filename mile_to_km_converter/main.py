from tkinter import *
FONT = ("Times New Roman", 12, "normal")
window = Tk()
window.title("Mile To Kilometre Converter")
window.minsize(width=120, height=100)
window.config(padx=10, pady=10)
# Mile entry
mile_entry = Entry(width=12, font=FONT)
mile_entry.focus()
mile_entry.grid(column=1, row=0)

# Mile unit label
mile_unit_label = Label(text="Miles", font=FONT)
mile_unit_label.grid(column=2, row=0)
# Km unit label
km_unit_label = Label(text="Km", font=FONT)
km_unit_label.grid(column=2, row=1)
# Km label
km_label = Label(text="0", font=FONT)
km_label.grid(column=1, row=1)
# Equal label
equal_unit_label = Label(text="is equal to", font=FONT)
equal_unit_label.grid(column=0, row=1)

# Calculate Button


def button_click():
    km_label.config(text=round(float(mile_entry.get())*1.609344, 2))


cal_button = Button(text="Calculate", command=button_click, font=FONT)
cal_button.grid(column=1, row=2)
cal_button.config(padx=20)


window.mainloop()
