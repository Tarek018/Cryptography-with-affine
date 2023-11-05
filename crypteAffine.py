import string
import tkinter as tk
from tkinter import ACTIVE, DISABLED, NORMAL, OptionMenu, filedialog, messagebox, simpledialog
import os
import re
import subprocess



class crypteAffine :
    plainText:string
    keyOne:int
    keyTwo:int
    alphabet = []
    def __init_(self):
        self.plainText = ""
        self.keyOne = 0
        self.keyTwo = 0
        # Add each letter of the alphabet to the array using a for loop
        for letter in range(ord('A'), ord('Z') + 1):
            self.alphabet.append(chr(letter))

        
    
    def open_file(self):
        global key1_button
        # global chiffre_btn
        
        file_path = filedialog.askopenfilename()
        text = ''
        if os.path.getsize(file_path) == 0:
            messagebox.showwarning("Alert", "The file is empty!\nPlease try again.")
            return
        if file_path:
            with open(file_path, 'r') as file:
                text = file.read()
                # Check if the file contains numbers
                if re.search(r'\d', text):
                    messagebox.showwarning("Alert", "The file contains numbers!\nPlease try again.")
                    key1_button.config(state=DISABLED)
                    key2_button.config(state=DISABLED)
                    chiffre_btn.config(state=DISABLED)
                    self.open_file()
                else:
                    text = text.upper()
                    print(text)
                    self.plainText = text
                    key1_button.config(state=ACTIVE)
    def encrypte(self):
        cipher_text = ""
        for char in self.plainText:
            self.alphabet = string.ascii_lowercase
            char = char.lower()

            if char in self.alphabet:
                index = self.alphabet.index(char)
                new_index = (self.keyOne * index + self.keyTwo) % 26
                print(index)
                cipher_text += self.alphabet[new_index]   
            else:
                if char == ' ':
                    cipher_text = cipher_text+ ' '
                else:
                    return -1  # Character is not in the alphabet
        cipher_text = cipher_text.upper()
        print(cipher_text)
        new_file_path = "encrypted_file.txt"
        with open(new_file_path, 'w') as file:
            # Write content to the file
            file.write(cipher_text)
            subprocess.Popen(['notepad.exe', new_file_path])
    
    def enter_key_one(self,value):
        global chiffre_btn
        global key2_button

        self.keyOne = value
        key2_button.config(state=ACTIVE)   

    def enter_key_two(self):
        global chiffre_btn
        number = simpledialog.askinteger("Enter a Number", "Please enter a number:")
        print(number)
        if (number > 25 or number < 1):
            messagebox.showwarning("Alert", "The key should be between 1 and 25\nPlease try again.")
            chiffre_btn.config(state=DISABLED)
            self.enter_key_two()
        else:
            self.keyTwo = number
            chiffre_btn.config(state=ACTIVE)


    def UI(self, root):
        page1_window = tk.Toplevel(root)
        page1_window.geometry("800x800")  # Set the size of the window
        page1_window.title("Encrypt")
        page1_window.grab_set()

        global chiffre_btn
        global key2_button

        select_button = tk.Button(page1_window, text="Select File", command=self.open_file, height=5, width=20, cursor="hand2")
        select_button.pack(padx=50, pady=50)
        
       # Label to display the selected value
        label = tk.Label(page1_window, text="Click here to select the first key")
        label.pack()

        # Drop-down list options
        options = [1, 3, 5, 7 ,9,11,15,17,19,21,23,25]

        # Variable to store selection
        selected_value = tk.IntVar()

        # Creating the drop-down list
        option_menu = OptionMenu(page1_window, selected_value, *options)
        option_menu.pack()
        selected_value.trace("w", lambda *args: self.enter_key_one(selected_value.get()))



        key2_button = tk.Button(page1_window, text="Enter the second key", command=self.enter_key_two, state=DISABLED, height=5, width=20, cursor="hand2")
        key2_button.pack(padx=50, pady=50)

        chiffre_btn = tk.Button(page1_window, text="Encrypt", command=self.encrypte, state=DISABLED, height=5, width=20, cursor="hand2")
        chiffre_btn.pack(padx=50, pady=50)

        


        
        
        
        