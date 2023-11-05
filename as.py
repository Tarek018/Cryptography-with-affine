import string
import math
import subprocess

possible_case = []
i=0

plainText = "wnv gbanf lv obln zd gbanf gazfz"
alphabet = []

for letter in range(ord('A'), ord('Z') + 1):
        alphabet.append(chr(letter))

def dycrypte():
        for char in plainText:
            alphabet = string.ascii_lowercase
            char = char.lower()
            new_text =""
            if char in alphabet:
                for case in possible_case:
                    index = alphabet.index(char)
                    new_index = pow(case[0],-1,26) * (index - case[1]) % 26
                    new_text += alphabet[new_index]   
            else:
                if char == ' ':
                    new_text = new_text+ ' '
                else:
                    return -1  # Character is not in the alphabet
            print(new_text)
            new_text = ""
            print("\n")


for a in range(1,26):
        if math.gcd(a,26) == 1:
            print(f"Combinaison  a={a}")
            print(a)
            for b in range(1,27):
                  possible_case.append((a,b))



new_text =""
i=0
for case in possible_case:
    new_text = new_text + '\n'
    new_text = new_text + '- Pour la cle='+str(case[0])+'et '+str(case[1])+':\n'
    for char in plainText:
            alphabet = string.ascii_lowercase
            char = char.lower()
            if char in alphabet:
                        index = alphabet.index(char)
                        new_index = pow(case[0],-1,26) * (index - case[1]) % 26
                        new_text = new_text + alphabet[new_index]  
            else:
                if char == ' ':
                    new_text = new_text+ ' '
    i+=1
print(i)    
new_file_path = "encrypted_file.txt"
with open(new_file_path, 'w') as file:
         # Write content to the file
            file.write(new_text)
            subprocess.Popen(['notepad.exe', new_file_path])
