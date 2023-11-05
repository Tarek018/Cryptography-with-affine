import string
import tkinter as tk
from tkinter import ACTIVE, DISABLED, NORMAL, filedialog, messagebox, simpledialog
import os
import re
import subprocess
import math




class decrypteAffine :
    cipherText:string
   


    def __init_(self):
        self.cipherText = ""
        
        
    
    def open_file(self):
        global decrypt_btn
        
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
                    decrypt_btn.config(state=DISABLED)
                    self.open_file()
                else:
                    text = text.upper()
                    print(text)
                    self.cipherText = text
                    decrypt_btn.config(state=ACTIVE)

    def decrypte(self):
        plainText = ""
        alphabet = []
        possible_case = []
        for letter in range(ord('A'), ord('Z') + 1):
            alphabet.append(chr(letter))
        
        for a in range(1,26):
            if math.gcd(a,26) == 1:
                for b in range(1,27):
                    possible_case.append((a,b))
        for case in possible_case:
            plainText = plainText + '\n'
            plainText = plainText + '- Pour a = '+str(case[0])+' et b = '+str(case[1])+':\n'
            for char in self.cipherText:
                    alphabet = string.ascii_lowercase
                    char = char.lower()
                    if char in alphabet:
                                index = alphabet.index(char)
                                new_index = pow(case[0],-1,26) * (index - case[1]) % 26
                                plainText = plainText + alphabet[new_index]  
                    else:
                        if char == ' ':
                            plainText = plainText+ ' '
        new_file_path = "decrypted_file.txt"
        with open(new_file_path, 'w') as file:
                # Write content to the file
                    file.write(plainText)
                    subprocess.Popen(['notepad.exe', new_file_path])
    def UI(self, root):
        page2_window = tk.Toplevel(root)
        page2_window.geometry("800x800")  # Set the size of the window
        page2_window.title("Encrypt")
        page2_window.grab_set()

        global decrypt_btn

        selected_button = tk.Button(page2_window, text="Select File", command=self.open_file, height=5, width=20, cursor="hand2")
        selected_button.pack(padx=50, pady=50)

        decrypt_btn = tk.Button(page2_window, text="decrypt", command=self.decrypte, state=DISABLED, height=5, width=20, cursor="hand2")
        decrypt_btn.pack(padx=50, pady=50)

        


        
        
        
        