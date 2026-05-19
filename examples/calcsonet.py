## Sonet 4.5
import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("400x550")
        self.master.resizable(False, False)
        self.master.configure(bg='#2C3E50')
        
        # Variables
        self.expression = ""
        self.input_text = tk.StringVar()
        
        # Create widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.master, bg='#2C3E50')
        display_frame.pack(expand=True, fill='both')
        
        # Entry field
        input_field = tk.Entry(
            display_frame,
            textvariable=self.input_text,
            font=('Arial', 24, 'bold'),
            justify='right',
            bd=10,
            bg='#ECF0F1',
            fg='#2C3E50',
            insertwidth=4,
            relief=tk.FLAT
        )
        input_field.pack(fill='both', expand=True, padx=10, pady=20)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.master, bg='#2C3E50')
        buttons_frame.pack(expand=True, fill='both')
        
        # Button layout
        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '']
        ]
        
        # Button colors
        special_color = '#E74C3C'  # Red for clear
        operator_color = '#3498DB'  # Blue for operators
        equals_color = '#27AE60'  # Green for equals
        number_color = '#34495E'  # Dark gray for numbers
        
        for i, row in enumerate(buttons):
            for j, button in enumerate(row):
                if button == '':
                    continue
                    
                # Determine button color
                if button == 'C':
                    bg_color = special_color
                elif button == '=':
                    bg_color = equals_color
                elif button in ['/', '*', '-', '+', '%', '⌫']:
                    bg_color = operator_color
                else:
                    bg_color = number_color
                
                btn = tk.Button(
                    buttons_frame,
                    text=button,
                    font=('Arial', 18, 'bold'),
                    bg=bg_color,
                    fg='white',
                    activebackground=bg_color,
                    activeforeground='white',
                    bd=0,
                    relief=tk.FLAT,
                    cursor='hand2'
                )
                
                # Special width for 0 button
                if button == '0':
                    btn.grid(row=i, column=j, columnspan=2, sticky='nsew', padx=2, pady=2)
                else:
                    btn.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)
                
                # Bind button actions
                if button == '=':
                    btn.config(command=self.evaluate)
                elif button == 'C':
                    btn.config(command=self.clear)
                elif button == '⌫':
                    btn.config(command=self.backspace)
                else:
                    btn.config(command=lambda x=button: self.click(x))
        
        # Configure grid weights for responsive buttons
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.grid_columnconfigure(j, weight=1)
    
    def click(self, value):
        """Handle button clicks"""
        self.expression += str(value)
        self.input_text.set(self.expression)
    
    def clear(self):
        """Clear the display"""
        self.expression = ""
        self.input_text.set("")
    
    def backspace(self):
        """Delete last character"""
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)
    
    def evaluate(self):
        """Evaluate the mathematical expression"""
        try:
            # Replace % with /100 for percentage
            expression = self.expression.replace('%', '/100')
            result = str(eval(expression))
            self.input_text.set(result)
            self.expression = result
        except ZeroDivisionError:
            self.input_text.set("Error: Div by 0")
            self.expression = ""
        except:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()