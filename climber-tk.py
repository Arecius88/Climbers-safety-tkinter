import tkinter as tk
from tkinter import ttk

# Configiration
root_window_title = "Climbers saftey"
window_size = "250x150".v
sandbag_weight = 15


def submit_button():
    #Get value
    climber_weight = climber_var.get()
    belayer_weight = belayer_var.get()
    
    # Calculations 
    weight_diff = climber_weight / belayer_weight
    global amount_sandbags 
    
    if weight_diff > 1.2:
        amount_sandbags = round((climber_weight-belayer_weight)/sandbag_weight)
        output_field.config(text=f"You need {amount_sandbags} sandbags")
    
    else: 
        output_field.config(text=f"You don't need sandbags")

    
    

# Create a Window
root = tk.Tk()
root.title(root_window_title)
root.geometry(window_size)
climber_var = tk.IntVar()
belayer_var = tk.IntVar()

# Climber input
climber_label = ttk.Label(master=root, text="Insert Climbers Weight")
climber_label.pack()

climber_input_field = ttk.Entry(master=root, textvariable=climber_var)
climber_input_field.pack()

# Belayer input
belayer_label = ttk.Label(master=root, text="Insert Belayers Weight")
belayer_label.pack()

belayer_input_field = ttk.Entry(master=root, textvariable=belayer_var)
belayer_input_field.pack()

# Submit button
submit_button = ttk.Button(master=root, text="Calculate Sandbags", command= submit_button)
submit_button.pack()

# Output field
output_field = ttk.Label(text=f"You will need this many sandbags", font=("Helvetica", 12))
output_field.pack()





# Run
root.mainloop()
