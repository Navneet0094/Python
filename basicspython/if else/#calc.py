import tkinter as tk

def calculate():
    a = float(entry_a.get())
    b = float(entry_b.get())
    operator = entry_operator.get()

    result_var.set("")  # Clear previous result

    try:
        if operator == '+':
            result_var.set("Addition is: {:.2f}".format(a + b))
        elif operator == '-':
            result_var.set("Subtraction is: {:.2f}".format(a - b))
        elif operator == '*':
            result_var.set("Multiplication is: {:.2f}".format(a * b))
        elif operator == '/':
            if b != 0:
                result_var.set("Division is: {:.2f}".format(a / b))
            else:
                result_var.set("Cannot divide by zero")
        elif operator == '%':
            result_var.set("Remainder is: {:.2f}".format(a % b))
        elif operator == '**':
            result_var.set("a to the power b is: {:.2f}".format(a ** b))
        elif operator == '//':
            if b != 0:
                result_var.set("Floor Division is: {:.2f}".format(a // b))
            else:
                result_var.set("Cannot divide by zero")
        else:
            result_var.set("Enter a valid operator")
    except ValueError:
        result_var.set("Invalid input. Please enter valid numbers.")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create input fields
label_a = tk.Label(window, text="Enter a:")
label_a.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
entry_a = tk.Entry(window)
entry_a.grid(row=0, column=1, padx=5, pady=5)

label_b = tk.Label(window, text="Enter b:")
label_b.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
entry_b = tk.Entry(window)
entry_b.grid(row=1, column=1, padx=5, pady=5)

label_operator = tk.Label(window, text="Enter operator:")
label_operator.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
entry_operator = tk.Entry(window)
entry_operator.grid(row=2, column=1, padx=5, pady=5)

# Create a button to trigger the calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create a label to display the result
result_var = tk.StringVar()
result_label = tk.Label(window, textvariable=result_var)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
window.mainloop()
