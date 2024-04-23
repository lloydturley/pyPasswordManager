from tkinter import *
from tkinter import messagebox
import random
import pyperclip

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "K",
           "J", "L", "M", "P", "O", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password = [random.choice(letters) for _ in range(nr_letters)]
    password += [random.choice(numbers) for _ in range(nr_numbers)]
    password += [random.choice(symbols) for _ in range(nr_symbols)]
    random.shuffle(password)
    password = ''.join(str(x) for x in password)
    pyperclip.copy(password)

    password_input.delete(0,END)
    password_input.insert(0,password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get().strip()
    email = emun_input.get().strip()
    password = password_input.get().strip()

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Operational Error", message="An entry is empty and it can't be.  Fix it.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            line = f"{website} | {email} | {password}\n"
            with open("passwordFile.txt", "a") as file:
                file.write(line)

            website_input.delete(0, END)
            password_input.delete(0, END)
        website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width="200", height="200", highlightthickness=20)

background_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background_image)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:")
website_label.grid(row=2, column=0)
emun_label = Label(text="Email/Username:")
emun_label.grid(row=3, column=0)
password_label = Label(text="Password")
password_label.grid(row=4, column=0)

# entries
website_input = Entry(width=35, justify="left")
website_input.grid(row=2, column=1, columnspan=2, sticky=EW)
website_input.focus()
emun_input = Entry(width=35, justify="left")
emun_input.grid(row=3, column=1, columnspan=2, sticky=EW)
emun_input.insert(0, "lloydturley2@gmail.com")
password_input = Entry(width=21, justify="left")
password_input.grid(row=4, column=1, sticky=EW)

genpassword_button = Button(text="Generate Password", justify="right", command=generate_password)
genpassword_button.grid(row=4, column=2, sticky=EW)

add_button = Button(text="Add", width=36, justify="left", command=save_password)
add_button.grid(row=5, column=1, columnspan=2, sticky=EW)

window.mainloop()
