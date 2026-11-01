
import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#20232A")

# Display
expression = ""

display = tk.Entry(
    root,
    font=("Arial", 25),
    bg="#303640",
    fg="white",
    justify="right",
    bd=0
)
display.pack(fill="x", padx=15, pady=25, ipady=15)

# Button functions
def click(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Cannot divide by zero")
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Invalid Input")

def square_root():
    try:
        number = float(display.get())
        if number < 0:
            raise ValueError
        result = number ** 0.5
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Invalid Input")

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "√", "+"],
    ["C", "⌫", "%", "="]
]

def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

# Create buttons
for row in buttons:
    frame = tk.Frame(root, bg="#20232A")
    frame.pack(expand=True, fill="both", padx=10)

    for item in row:
        if item == "=":
            command = calculate
            color = "#00A86B"
        elif item == "C":
            command = clear
            color = "#D9534F"
        elif item == "⌫":
            command = backspace
            color = "#D97706"
        elif item == "√":
            command = square_root
            color = "#4A90E2"
        elif item in ["+", "-", "*", "/", "%"]:
            command = lambda x=item: click(x)
            color = "#4A90E2"
        else:
            command = lambda x=item: click(x)
            color = "#3B414B"

        tk.Button(
            frame,
            text=item,
            font=("Arial", 18, "bold"),
            bg=color,
            fg="white",
            bd=0,
            command=command
        ).pack(
            side="left",
            expand=True,
            fill="both",
            padx=4,
            pady=4
        )

# Run application
root.mainloop()
