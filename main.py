from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():

    if password_entry.get() == '':
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


        password_letters = [choice(letters) for n in range(randint(8, 10))]
        password_symbols = [choice(symbols) for n in range(randint(2, 4))]
        password_numbers = [choice(numbers) for n in range(randint(2, 4))]

        password_list = password_letters + password_symbols + password_numbers

        shuffle(password_list)

        password = ''.join(password_list)
        password_entry.insert(0, password)
        pyperclip.copy(password)
        messagebox.showinfo(message='copied to the clipboard')
    else:
        password_entry.delete(0, END)
        generate_pass()


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()

    if website_data == '':
        messagebox.showinfo(title='website', message="Website is null")
    elif email_data == '':
        messagebox.showinfo(title='data', message="Email or username is null")
    elif password_data == '':
        messagebox.showinfo(title='password', message="Password is null")
    else:
        is_ok = messagebox.askokcancel(title=website_data, message=f'These are the details entered: \nEmail: {email_data}\nAddress: {website_data}\nPassword: {password_data}\nDo you want so save?')

        if is_ok:
            with open('data.txt', 'a') as f:
                f.write(f'{website_data}  |  {email_data}  |  {password_data}\n')
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.minsize(width=240, height=240)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

#Entry
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'aaa111@gmail.com')
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

#Buttons
generate_button = Button(text='Generate Password', command=generate_pass)
generate_button.grid(column=2, row=3)
add_button = Button(text='Add', width=42, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()