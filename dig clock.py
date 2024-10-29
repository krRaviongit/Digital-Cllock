import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock with Date and Day")

# Function to update time, date, and day
def time():
    time_string = strftime('%H:%M:%S %p')  # Time in Hour:Minute:Second AM/PM
    date_string = strftime('%Y-%m-%d')     # Date in Year-Month-Day
    day_string = strftime('%A')            # Day of the week
    
    label_time.config(text=time_string)
    label_date.config(text=date_string)
    label_day.config(text=day_string)
    
    # Update the time every second
    label_time.after(1000, time)

# Label for displaying time
label_time = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label_time.pack(anchor='center')

# Label for displaying date
label_date = tk.Label(root, font=('calibri', 20), background='black', foreground='white')
label_date.pack(anchor='center')

# Label for displaying day
label_day = tk.Label(root, font=('calibri', 20), background='black', foreground='white')
label_day.pack(anchor='center')

# Call the time function to update the clock
time()

# Run the main loop
root.mainloop()
