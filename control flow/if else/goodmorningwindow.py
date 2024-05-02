import tkinter as tk
import time

def greet():
    current_hour = int(time.strftime('%H'))

    if 5 <= current_hour < 12:
        return "Good Morning!"
    elif 12 <= current_hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

def update_greeting_label():
    greeting_message = greet()
    greeting_label.config(text=greeting_message)
    root.after(1000, update_greeting_label)  # Update every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Time-Based Greeting")

# Create a label to display the greeting
greeting_label = tk.Label(root, font=("Helvetica", 18))
greeting_label.pack(pady=20)

# Call the update_greeting_label function to start updating the label
update_greeting_label()

# Run the Tkinter event loop
root.mainloop()
