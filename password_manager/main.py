from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random


def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    ent_password.delete(0, END)
    ent_password.insert(0, password)
    pyperclip.copy(password)
    return password
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = ent_website.get()
    email = ent_email.get()
    password = ent_password.get()
    if not website or not email or not password:
        return messagebox.showerror("Error", "Please don't leave any fields empty!")

    is_ok = messagebox.askokcancel(
        website, f"These are details entered: \nWebsite: {website}\nEmail: {email}\nPassword: {password}\nIs it ok to save?")
    if is_ok:
        with open("./password_manager/data.txt", mode="a") as file:
            file.write(f"{website} | {email} | {password}\n")
        ent_website.delete(0, END)
        ent_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
image = PhotoImage(file="./password_manager/logo.png")
canvas = Canvas(bg="white", highlightthickness=0, width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

lbl_website = Label(text="Website:")
lbl_website.grid(row=1, column=0)
lbl_email = Label(text="Email/Username:")
lbl_email.grid(row=2, column=0)
lbl_password = Label(text="Password:")
lbl_password.grid(row=3, column=0)

ent_website = Entry(width=53, highlightthickness=1)
ent_website.grid(row=1, column=1, columnspan=2)
ent_email = Entry(width=53, highlightthickness=1)
ent_email.insert(0, "hantn16@gmail.com")
ent_email.grid(row=2, column=1, columnspan=2)
ent_password = Entry(width=34)
ent_password.grid(row=3, column=1)
btn_genpass = Button(text="Generate Password", command=gen_password)
btn_genpass.grid(row=3, column=2)
btn_add = Button(text="Add", width=45, command=save)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
