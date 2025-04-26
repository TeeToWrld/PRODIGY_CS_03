import tkinter as tk 

root = tk.Tk()
root.title("my first gui")
root.geometry("400x300")

label = tk.Label(root, text="Enter your password")
label.pack(pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)

show_password_var = tk.IntVar

def toggle_password():
    if show_password_var:
        password_entry.config(show='')
    else:
        password_entry.config(show='')



def check_password():
    strength_score = 0
    user_input = password_entry.get()
    message = []
    

    if len(user_input) > 8:
        strength_score += 1
    else:
         message.append("Password needs to be longer")
    
    if  any(char.isupper() for char in user_input):
        strength_score += 1
    else:
        message.append("Password should contain at least 1 uppercase")

    if  any(char.islower() for char in user_input):
        strength_score += 1
    else:
        message.append("Password should contain atleast 1 lowercase")

    
    if any(char.isdigit() for char in user_input):
        strength_score += 1
    else:
         message.append("Password contains an integer")


    special_characters = "!@#$%^&*()-_=+[{]}|;:',<.>/?`~"
    if any(char in special_characters for char in user_input):
        strength_score += 1
    else: 
         message.append("Password needs to contain a speciaql charcaters")
        
    

    if strength_score == 5:
        strength = "Strong Password"
    elif strength_score == 4:
        strength = "Moderate Password"
    elif strength_score >= 3:
        strength = "Weak Password"

    result.config(text="\n".join(message) + f'\n\nStrength: {strength}')








button = tk.Button(root, text="Check password", command=check_password)
button.pack(pady=10)

show_password_check = tk.Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_password)
show_password_check.pack(pady=10)

result = tk.Label(root, text="",  wraplength=350, justify='left')
result.pack(pady=10)




 

root.mainloop()