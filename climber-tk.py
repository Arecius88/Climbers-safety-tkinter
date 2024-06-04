import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning, showinfo

# Configiration
root_window_title = "Climbers safety"
window_size = "250x150"
sandbag_weight = 15 # in kg

def validate_user_input(user_input: str) -> int:
    try:
        value = int(user_input)
        if _validate_above_zero(value):
            return value
    except ValueError:
        showwarning(title="Error", message="Weight must be a number")

def _validate_above_zero(user_input: str)-> int:
    if user_input > 0:
        return True
    else: 
        showwarning(title="Error", message="Weight must be over 0")

def submit_button() -> None:
    global amount_sandbags
    
    #Get value
    climber_weight: str = climber_var.get()
    belayer_weight: str = belayer_var.get()
    climber_weight: int = validate_user_input(climber_weight)
    belayer_weight: int = validate_user_input(belayer_weight)
    
    
    if climber_weight and belayer_weight:
        weight_diff: float = climber_weight / belayer_weight

        if weight_diff > 1.2:
            amount_sandbags: int = round((climber_weight - belayer_weight) / sandbag_weight)
            output_field.config(text=f"You need {amount_sandbags} sandbags")
        
        else: 
            showinfo(title="Number of sandbags", message="You don't need sandbags")
            
# Create a Window
root = tk.Tk()
root.title(root_window_title)
root.geometry(window_size)

# Set Entry variable
climber_var = tk.StringVar()
belayer_var = tk.StringVar()

# Set Entry default to empty string
climber_var.set("")
belayer_var.set("")

# Heading label - Climber
climber_label = ttk.Label(master=root, text="Insert Climbers Weight")
climber_label.pack()

# Create Entry field - Climber
climber_input_field = ttk.Entry(master=root, textvariable=climber_var)
climber_input_field.pack()

# Heading label - Belayer
belayer_label = ttk.Label(master=root, text="Insert Belayers Weight")
belayer_label.pack()

# Create Entry field - Belayer
belayer_input_field = ttk.Entry(master=root, textvariable=belayer_var)
belayer_input_field.pack()

# Button for calculate number of sanbags belayer needs. 
sandbag_button = ttk.Button(master=root, text="Calculate Sandbags", command= submit_button)
sandbag_button.pack()

# Output field
output_field = ttk.Label(text=f"You will need this many sandbags", font=("Helvetica", 12))
output_field.pack()

if __name__=="__main__":
    # Run
    root.mainloop()
